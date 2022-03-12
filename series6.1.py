import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from standard_calc import calc
import os
from plot import do_plot

series = '6.1'
data_file = os.path.join(os.getcwd(), 'data', 'OSCsampl' + series + '.csv')
result_file = os.path.join(os.getcwd(), 'results', 'result' + series + '.txt')

data = pd.read_csv(data_file, delimiter=',')

V_RMS = (data.voltage.max() - data.voltage.min())/(2*np.sqrt(2))
I_RMS = (data.current1.max() - data.current1.min())/(2*np.sqrt(2))

P_RMS = V_RMS*I_RMS

k = 13
j = 7

result = open(result_file, 'w')
result.write('Serie ' + series + '\n')
result.write('------------------------------' + '\n')
result.write('V_RMS:'.ljust(k) + str(round(V_RMS, 2)).ljust(j) + 'V' + '\n')
result.write('I_RMS:'.ljust(k) + str(round(I_RMS, 2)).ljust(j) + 'A' + '\n')
result.write('P:'.ljust(k) + str(round(P_RMS, 2)).ljust(j)  + 'W' + '\n')
result.write('------------------------------' + '\n')
result.close()   