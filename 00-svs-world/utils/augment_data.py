import os
from os.path import basename, expanduser, join, splitext
from glob import glob
import shutil
from music21 import *
import pyworld
import librosa
import numpy as np
from tqdm import tqdm
import soundfile as sf

import yaml
with open('config.yaml', 'r') as yml:
    config = yaml.load(yml, Loader=yaml.FullLoader)


lab_out_dir = join(config["out_dir"], "augmented_lab")
xml_out_dir = join(config["out_dir"], "augmented_xml")
wav_out_dir = join(config["out_dir"], "augmented_wav")

for dst_dir in [lab_out_dir, xml_out_dir, wav_out_dir]:
    os.makedirs(dst_dir, exist_ok=True)

lab_files = sorted(glob(join(expanduser(config["db_root"]), "mono_label/*.lab")))
for lab_path in tqdm(lab_files):
    utt_id = splitext(basename(lab_path))[0]

    wav_path = join(expanduser(config["db_root"]), "wav", utt_id + ".wav")
    xml_path = join (expanduser(config["db_root"]), "xml", utt_id + ".xml")

    score_orig = converter.parse(xml_path)
    print("load {}".format(wav_path))
    wav_data, sr = librosa.load(wav_path, sr=int(config["sample_rate"]))
    assert sr == int(config["sample_rate"])

    wav_data = wav_data.astype(np.float64)
    print("Calculate f0")
    f0, timeaxis = pyworld.harvest(wav_data, sr, frame_period=int(config["frame_period"]),
                                   f0_floor=int(config["f0_floor"]), f0_ceil=int(config["f0_ceil"]))
    print("Calculate sp")    
    sp = pyworld.cheaptrick(wav_data, f0, timeaxis, sr)
    print("Calculate ap")        
    ap = pyworld.d4c(wav_data, f0, timeaxis, sr)

    for i in range(int(config["transpose_floor"]), int(config["transpose_ceil"])):
        lab_out_path = join(lab_out_dir, "{}_{}.lab".format(utt_id, i))
        print("Copy {} to {}".format(lab_path, lab_out_path))        
        shutil.copy(lab_path, lab_out_path)

        score_transposed = score_orig.transpose(i)
        xml_out_path = join(xml_out_dir,  "{}_{}.xml".format(utt_id, i))
        print("Write transposed score: {}".format(xml_out_path))
        score_transposed.write('musicxml', xml_out_path)
        
        modified_f0 = f0 * 2 ** (1 / 12.0 * i)

        wav_data_transposed = pyworld.synthesize(modified_f0, sp, ap, sr)
        wav_out_path = join(wav_out_dir,  "{}_{}.wav".format(utt_id, i))
        print("Write transposed wav: {}".format(wav_out_path))
        sf.write(wav_out_path, wav_data_transposed, sr)
        
