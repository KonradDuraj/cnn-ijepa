import os
import torch
from torch.utils.data import Dataset

class ImagenetMini_Pretrain(Dataset):
    def __init__(self, directory) -> None:
        self.data = dict()
        directories = [os.path.join(directory, d) for d in os.listdir(directory)]
        
        for directory in directories:
            filepaths = [os.path.join(directory, f) for f in os.listdir(directory)] # keys
            category = [os.path.basename(directory)] * len(filepaths) # values
            temp_dict = {f:c for f,c in zip(filepaths,category)}
            self.data.update(temp_dict)
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        filepath, category = list(self.data)[idx]
        

class ImagenetMini(Dataset):
    def __init__(self, directory) -> None:
        self.data = dict()
        directories = [os.path.join(directory, d) for d in os.listdir(directory)]
        
        for directory in directories:
            filepaths = [os.path.join(directory, f) for f in os.listdir(directory)] # keys
            category = [os.path.basename(directory)] * len(filepaths) # values
            temp_dict = {f:c for f,c in zip(filepaths,category)}
            self.data.update(temp_dict)
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        filepath, category = list(self.data)[idx]
