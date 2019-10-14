last updated: 28/9/2019

The following document record the changes need to run the code

##  1. Set-up environment

```
cd utils/
```

```
pip3 install -r pip-requirements.txt
```

will fail installing tensor flow-gpu use (need to resolve this)

```bash
pip3 install --no-cache-dir tensorflow
```

```bash
pip3 install git+https://www.github.com/keras-team/keras-contrib.git
```

This will install the require package to run the code on the VM

## 2. Modified Code

main.py

- *line76* change the **root_dir** to the existing project directory
- if an existing result for the set up exist, the code will print "already done"



utility.py

- change '\_TRAIN' and '\_TEST' to '\_TRAIN.tsv' and '\_TEST.tsv'
- *line357* change 'archive_name'



constants.py

- *line16* change 'ARCHIVE_NAME' to you data folder
- root_dir set to the path of the existing project folder
- if "/results" contains results of the current experiment, the code will print "already done". Need to remove the file for the code to run. 

    

```
rm -r <dir>
```

## 3. Run code

This code allow the training run into the background of VM

```
nohup <command> &
# for example:
nohup python3 main.py UCRArchive_2018 Coffee fcn _itr8_ &
```

check if the task is running

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

All model checked.

# Austalk

data preprocessing complete, 2391 row of data

3 classes: hins, hine, hinge