# Rotowire-modified

Script for generating the rotowire-modified dataset for Learning to Select, Track, and Generate for Data-to-Text (Iso et al; ACL 2019).

## Data
This script generates the dataset "rotowire-modified" by extracting required data from the original rotowire dataset. 
We are not allowed to distribute the dataset itself due to the copyright issue, so we distribute only the script. 
The new dataset generated by this script is almost the same as, but not identical to the dataset used in the paper (Iso et al; ACL 2019). 
ACL's dataset contains 14 games that do not appear in the original rotowire and have to be obtained from https://www.rotowire.com and https://www.nba.com. 
Further information of the 14 games is listed in additional_games.txt.
In addition, there are a number of slight differences in data records due to the update of the original pages. 
For empirical comparison by other researchers, we also distribute the experimental result on this new rotowire-modified dataset at the [sports-reporter](https://github.com/aistairc/sports-reporter) repo.

#### Statistic of the datasets
|Data|Train|Validation|Test|Total|
|----|-----|----------|----|-----|
|rotowire (Wiseman'2017)|3398|727|728|4853|
|rotowire-modified (Iso et al; ACL 2019)|2714|534|500|3748|
|rotowire-modified (This repo)|2705|532|497|3734|

## Format

Since this script simply removed duplicate records from the original dataset, the data format is the same as that of the original rotowire dataset.
Please refer to [boxscore-data](https://github.com/harvardnlp/boxscore-data) repo.

## Usage

You can download the original dataset (Wiseman'2017) from the [boxscore-data](https://github.com/harvardnlp/boxscore-data) repo, 
and then, transform it as bellow.
The script will create a directory "rotowire-modified", which contains train.json, valid.json, and test.json files. 
~~~
DATA_PATH=<path to the locally downloaded original dataset>
python script/generate_rotowire_modified.py --src_dir $DATA_PATH
~~~


