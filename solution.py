import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2



chat_id = 728846853 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
  n = len(x)
  return np.sqrt(sum(x**2)/ (6*chi2.ppf((1+p)/2, df = 2n))), \
  np.sqrt(sum(x**2)/ (6*chi2.ppf((1 - p) / 2, df = 2n ))) 
