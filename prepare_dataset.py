import os
import shutil
import random

DATASET_PATH = "D:/X/projekty/fun/datasets/Imagenet-Mini/raw"

def count_files():
    info = dict()
    directories = [os.path.join(DATASET_PATH, d) for d in os.listdir(DATASET_PATH)]
    for d in directories:
        info[os.path.basename(d)] = len(os.listdir(d))
    
    print("Number of files for each directory: ", info)

def split_dataset():
    train_dir = "D:/X/projekty/fun/datasets/Imagenet-Mini/train"
    test_dir = "D:/X/projekty/fun/datasets/Imagenet-Mini/test"

    os.mkdir(train_dir)
    os.mkdir(test_dir)

    directories = [os.path.join(DATASET_PATH, d) for d in os.listdir(DATASET_PATH)]
    for d in directories:
        filepaths = [os.path.join(d, f) for f in os.listdir(d)]
        for i,filepath in enumerate(filepaths):
            if i < 420:
                dest_dir = os.path.join(train_dir, os.path.basename(d))
            else:
                dest_dir = os.path.join(test_dir, os.path.basename(d))
            if os.path.exists(dest_dir) is False:
                os.mkdir(dest_dir)

            dest_filepath = os.path.join(dest_dir, os.path.basename(filepath))
            shutil.copy(filepath, dest_filepath)



if __name__ == "__main__":
    #count_files()
    split_dataset()