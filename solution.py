import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2
from math import sqrt


chat_id = 728846853 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
  n = len(x)
  return sqrt(sum(x**2)/ (6*chi2.ppf((1+p)/2, df = n))), \
  sqrt(sum(x**2)/ (6*chi2.ppf((1 - p) / 2, df = n ))) 
