# nnsvs_natsume_singing

[NN-SVS](https://github.com/r9y9/nnsvs) recipe of Yuuri Natsume's singing voice database (51 songs).
Almost all codes are derived from [kiritan_singing](https://github.com/r9y9/kiritan_singing).

## Requirements
- nnsvs
- pysinsy
- nnmnkwii
- librosa
- soundfile
- scipy
- numpy
- tqdm
- jaconv

## How to use
Due to the licensing issue, this recipe does not include data nor helper scripts for downloading automatically. First of all, you need to get Natsume_Singing_DB.zip from [夏目悠李/男声歌声データベース配布、始めました！【2020/7/5 23:53更新】](https://amanokei.hatenablog.com/entry/2020/04/30/230003) (the terms of service are written in Japanese). Next, clone this repository and change `db_root` in `00-svs-world/run.sh` according to your environment. Then move to `00-svs-world` directory and run:

    run.sh --stage 0 --stop-stage 6

The directory structure made by this recipe is the same as kiritan_singing does.

## Known issues
There are mismatches between muxicxml files and HTS mono-phone labels in songs 2, 3, 13, 27, 43. Currently these songs are excluded from training in this recipe.

## Resources
- 夏目悠李/男声歌声データベース配布、始めました！【2020/7/5 23:53更新】: https://amanokei.hatenablog.com/entry/2020/04/30/230003
