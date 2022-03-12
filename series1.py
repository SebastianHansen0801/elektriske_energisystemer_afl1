import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from standard_calc import calc
import os
from plot import do_plot

series = '1'
data_file = os.path.join(os.getcwd(), 'data', 'OSCsampl' + series + '.csv')
result_file = os.path.join(os.getcwd(), 'results', 'result' + series + '.txt')

data = pd.read_csv(data_file, delimiter=',')

V_PP, I_PP, V_RMS, I_RMS, V_rect, I_rect, P_RMS, P_MAX, P_MIN, PF, T_period, freq, phase =  calc(data)
k = 13
j = 7

result = open(result_file, 'w')
result.write('Serie ' + series + '\n')
result.write('------------------------------' + '\n')
result.write('V_PP:'.ljust(k) + str(round(V_PP, 2)).ljust(j) + 'V' + '\n')
result.write('I_PP:'.ljust(k) + str(round(I_PP, 2)).ljust(j) + 'A' + '\n')
result.write('Time Period:'.ljust(k) + str(round(T_period, 3)).ljust(j) + 's' + '\n')
result.write('Frequency:'.ljust(k) + str(round(freq, 2)).ljust(j) + 'Hz' + '\n')
result.write('Phase:'.ljust(k) + str(round(phase, 2)).ljust(j) + 'degrees' + '\n')
result.write('V_RMS:'.ljust(k) + str(round(V_RMS, 2)).ljust(j) + 'V' + '\n')
result.write('I_RMS:'.ljust(k) + str(round(I_RMS, 2)).ljust(j) + 'A' + '\n')
result.write('P:'.ljust(k) + str(round(P_RMS, 2)).ljust(j)  + 'W' + '\n')
result.write('PF'.ljust(k) + str(round(PF, 2)).ljust(j) + '\n')
result.write('P_MAX:'.ljust(k) + str(round(P_MAX, 2)).ljust(j) + 'W' + '\n')
result.write('P_MIN:'.ljust(k) + str(round(P_MIN, 2)).ljust(j) + 'W' + '\n')
result.write('V_rect:'.ljust(k) + str(round(V_rect, 2)).ljust(j) + 'V' + '\n')
result.write('I_rect:'.ljust(k) + str(round(I_rect, 2)).ljust(j) + 'A' + '\n')
result.write('------------------------------' + '\n')
result.close()   

do_plot(data, series)