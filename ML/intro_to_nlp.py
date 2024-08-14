from typing import List
import torch
import torch.nn as nn
from torchtyping import TensorType


# torch.tensor(python_list) returns a Python list as a tensor


def get_dataset(positive: List[str], negative: List[str]) -> TensorType[float]:
    vocabulary = set()
    # split up positive and negative sentence into words
    for sentence in positive:
        for word in sentence.split():
            vocabulary.add(word)
    for sentence in negative:
        for word in sentence.split():
            vocabulary.add(word)

    # convert set into a list then sort the list
    sorted_list = sorted(list(vocabulary))

    word_to_int = {}
    # build the word to int dict
    # smallest word to be 1, second smallest to be 2, etc
    for i in range(len(sorted_list)):
        word_to_int[sorted_list[i]] = i + 1

    # encode every sentence as a tensor of integers
    tensors = []  # 2*N x Tensor
    # convert every positive and negative sentence to a list of integers
    for sentence in positive:
        curr_list = []
        for word in sentence.split():
            curr_list.append(word_to_int[word])
        tensors.append(torch.tensor(curr_list))  # convert list into a tensor
    for sentence in negative:
        curr_list = []
        for word in sentence.split():
            curr_list.append(word_to_int[word])
        tensors.append(torch.tensor(curr_list))
    # pad tensors
    return nn.utils.rnn.pad_sequence(tensors, batch_first=True)


"""
Input:
positive = ["Dogecoin to the moon"]
negative = ["I will short Tesla today"]

Output: [
  [1.0, 7.0, 6.0, 4.0, 0.0],
  [2.0, 9.0, 5.0, 3.0, 8.0]
]

"""
