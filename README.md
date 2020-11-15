# nnsvs_natsume_singing

[NNSVS](https://github.com/r9y9/nnsvs) recipe of Yuuri Natsume's singing voice database (51 songs).
Almost all codes are derived from [kiritan_singing](https://github.com/r9y9/kiritan_singing).

## Important Notice
**The recipe of Yuuri Natsume's singing voice database is merged into NNSVS repository on 04 Nov 2020.  Please use the official one.**

This repository is maintained only for the experimental purpose.

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
- pyyaml

## How to use
Due to the licensing issue, this recipe does not include data nor helper scripts for downloading automatically. First of all, you need to get Natsume_Singing_DB.zip from [夏目悠李/男声歌声データベース配布、始めました！【2020/9/1更新】](https://amanokei.hatenablog.com/entry/2020/04/30/230003) (the terms of service are written in Japanese). Next, clone this repository and change `db_root` in `00-svs-world/config.yaml` according to your environment. Then move to `00-svs-world` directory and run:

    run.sh --stage 0 --stop-stage 6

The directory structure made by this recipe is the same as kiritan_singing does.

## Sample code
- [Jupyter Notebook](https://gist.github.com/taroushirani/feb702386388188c7821f1a705a8f6b6) (Google Colaboratory, comments are written in Japanese)

## Resources
- 夏目悠李/男声歌声データベース配布、始めました！【2020/9/1更新】: https://amanokei.hatenablog.com/entry/2020/04/30/230003
