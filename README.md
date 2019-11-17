last updated: 16/11/2019

# Files

austalk - contains files that download and preprocess Austalk data set.

dl-4-tsc - the modified code from the original paper

financial distress - code for preprocess financial distress data

Jena weather data pre-processing code.Rmd - R code for Jena weather data 

YearlyWeatherDataCleaning.R - Rcode for preprocessign Yearly Weather Data

# Rnning the Code

Please clone the repository and use the following steps to run the code. 

##  1. Set-up environment

change directory to dl-4-tsc and then set up the dependancies in order to run the code.

```
cd utils/
```

```
pip3 install -r pip-requirements.txt
```

If install tensor flow-gpu fail, please use the following command to solve the low memory issue.

```bash
pip3 install --no-cache-dir tensorflow
```

```bash
pip3 install git+https://www.github.com/keras-team/keras-contrib.git
```

This will install the require package to run the code on the VM

## 2. Modification done on dl-4-tsc 

main.py

- *line76* change the **root_dir** to the existing project directory
- if an existing result for the set up exist, the code will print "already done"
- line 341 mcdcnn, result, acc -> accuracy



utility.py

- change '\_TRAIN' and '\_TEST' to '\_TRAIN.tsv' and '\_TEST.tsv'
- *line357* change 'archive_name'



constants.py

- *line16* change 'ARCHIVE_NAME' to you data folder
- root_dir set to the path of the existing project folder

Note:

- if "/results" contains results of the current experiment, the code will print "already done". Need to remove the file for the code before rerunning the code.

    

```
rm -r <dir>
```

# 3. Original data set

Please refer to README.md in dl-4-tsc/archives.

## 4. Run code

This code allow the training run into the background of VM

```
nohup python3 main.py <archive_name> <data_set> <classifier> <which_iteration> &
# for example:
nohup python3 main.py UCRArchive_2018 Coffee fcn _itr8_ &
```

check if the task by running any one of the following

```
jobs
bg
top
```

Upload your file to VM

```
scp -i path/to/key file/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/file
```



To download all the results file, got to the local directory which stored your key, and use the following command: 

```
scp -i itec876project.pem -r ubuntu@ec2-100-26-35-101.compute-1.amazonaws.com:/home/ubuntu/itec876group/dl-4-tsc/results/ project/dl-4-tsc/results/
```



## Code checking log

All model checked.  (11/10/2019)
