import torch
import numpy as np

def collate_fn_irregular_cutouts(batch):
    # Convert tuple of (x,y) tuples to tuple of x and y lists.
    x, y = list(zip(*batch))
    y = torch.as_tensor(np.concatenate([target.astype(np.float32) for target in y]))
    x = [torch.as_tensor(sample) for sample in x]
    return x, y