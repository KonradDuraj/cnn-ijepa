import torch
import torch.nn.functional as F

class Predictor(torch.nn.Module):
    def __init__(self) -> None:
        super(Predictor, self).__init__()
        
        self.fc1 = torch.nn.Linear(
            in_features=512,
            out_features=512
        )
    
    def forward(self, x):
        return self.fc1(x)