import torch
import torch.nn
from torchtyping import TensorType

# Helpful functions:
# https://pytorch.org/docs/stable/generated/torch.reshape.html
# https://pytorch.org/docs/stable/generated/torch.mean.html
# https://pytorch.org/docs/stable/generated/torch.cat.html
# https://pytorch.org/docs/stable/generated/torch.nn.functional.mse_loss.html


# Round your answers to 4 decimal places using torch.round(input_tensor, decimals = 4)
class Solution:
    def reshape(self, to_reshape: TensorType[float]) -> TensorType[float]:
        # torch.reshape() will be useful - check out the documentation
        row = to_reshape.shape[0] * to_reshape.shape[1] // 2
        reshaped = torch.reshape(to_reshape, (row, 2))
        return torch.round(reshaped, decimals=4)

    def average(self, to_avg: TensorType[float]) -> TensorType[float]:
        # torch.mean() will be useful - check out the documentation
        mean = torch.mean(to_avg, dim=0)  # 0 is col, so avg of each col
        return torch.round(mean, decimals=4)

    def concatenate(
        self, cat_one: TensorType[float], cat_two: TensorType[float]
    ) -> TensorType[float]:
        # torch.cat() will be useful - check out the documentation
        concat = torch.cat((cat_one, cat_two), dim=1)  # 1 is row, so concat rows
        return torch.round(concat, decimals=4)

    def get_loss(
        self, prediction: TensorType[float], target: TensorType[float]
    ) -> TensorType[float]:
        # torch.nn.functional.mse_loss() will be useful - check out the documentation
        mse_loss = torch.nn.functional.mse_loss(prediction, target)
        return torch.round(mse_loss, decimals=4)
