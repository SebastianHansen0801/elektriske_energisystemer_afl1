import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from standard_calc import calc
import os
from plot import do_plotz

series = '7.2'
data_file = os.path.join(os.path.dirname(os.getcwd()), 'data', 'OSCsampl' + series + '.csv')
result_file = os.path.join(os.path.dirname(os.getcwd()), 'results', 'result' + series + '.txt')

data = pd.read_csv(data_file, delimiter=',')

I_null = (data.current_null.max() - data.current_null.min())/(2*np.sqrt(2))

k = 13
j = 7

result = open(result_file, 'w')
result.write('Serie ' + series + '\n')
result.write('------------------------------' + '\n')
result.write('I_null:'.ljust(k) + str(round(I_null, 2)).ljust(j) + 'A' + '\n')
result.write('------------------------------' + '\n')
result.close()   