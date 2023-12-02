import torch
import torch.nn.functional as F

class Encoder(torch.nn.Module):
    def __init__(self) -> None:
        super(Encoder, self).__init__()
        
        self.conv1 = torch.nn.Conv2d(
            in_channels=3,
            out_channels=32,
            kernel_size=3
        )
        self.pool = torch.nn.MaxPool2d(2,2)
        self.conv2 = torch.nn.Conv2d(
            in_channels=32,
            out_channels=64,
            kernel_size=3
        )
        self.conv3 = torch.nn.Conv2d(
            in_channels=64,
            out_channels=128,
            kernel_size=3
        )
        self.conv4 = torch.nn.Conv2d(
            in_channels=128,
            out_channels=256,
            kernel_size=3
        )
        self.fc = torch.nn.Linear(
            in_features=10,
            out_features=512
        )

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.pool(F.relu(self.conv4(x)))
        x = torch.flatten(x, 1) 
        x = self.fc(x)
        return x
    