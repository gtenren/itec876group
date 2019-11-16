import librosa
import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import librosa

def write_file(observation,output_path):

    if os.path.exists(output_path):
        with open(output_path, 'a') as output:
            output.write("\n%d" %int(observation[0]))
            for i in observation[1:]:
                output.write('\t%f' % float(i))
    else:
        with open(output_path, 'a') as output:
            output.write("%s" % int(observation[0]))
            for i in observation[1:]:
                output.write('\t%f' % float(i))


def pad(list, length):
    n = len(list)
    if n <length:
        list += ([0] * (length-n))
    return list


if __name__ == "__main__":
    path = 'data/data.tsv'
    with open(path, newline='') as f:
        reader = csv.reader(f,delimiter = '\t')
        row1 = next(reader)
        row2 = next(reader)
        row3 = next(reader)
        row4 = next(reader)
        row5 = next(reader)
    plt.plot(range(len(row5[1:])),row5[1:])
    plt.show()
    #     # list = []
        # count= 0
        # for row in reader:
        #     list = []
        #     list.append(row[0])
        #     list +=  pad(row[15000:15500],500)
        #     write_file(list, 'data/data_n.tsv')
        #     count+=1
        #     print(len(list))
    # y,sr = librosa.load('data/austalk/data.wav')
    # y = librosa.resample(y, 16000, 8000)
    # plt.plot(range(len(y)),y)
    # plt.show()