import numpy as np
import pandas as pd


def calculate(list):
  if len(np.array(list)) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    arr = np.array(list).reshape((3, 3))

    df = pd.Series(
      [[
        np.mean(arr, axis=0).tolist(),
        np.mean(arr, axis=1).tolist(),
        np.mean(list).tolist()
      ],
       [
         np.var(arr, axis=0).tolist(),
         np.var(arr, axis=1).tolist(),
         np.var(list).tolist()
       ],
       [
         np.std(arr, axis=0).tolist(),
         np.std(arr, axis=1).tolist(),
         np.std(list).tolist()
       ],
       [
         np.max(arr, axis=0).tolist(),
         np.max(arr, axis=1).tolist(),
         np.max(list).tolist()
       ],
       [
         np.min(arr, axis=0).tolist(),
         np.min(arr, axis=1).tolist(),
         np.min(list).tolist()
       ],
       [
         np.sum(arr, axis=0).tolist(),
         np.sum(arr, axis=1).tolist(),
         np.sum(list).tolist()
       ]],
      index=['mean', 'variance', 'standard deviation', 'max', 'min', 'sum'])
    calculations = df.to_dict()
    return calculations
