def calc(data):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    from fourier import get_freq_and_phase

    V_PP = data.voltage.max() - data.voltage.min()
    I_PP = data.current.max() - data.current.min()

    freq, phase = get_freq_and_phase(data)
    T_period = 1/freq

    V_RMS = (V_PP/2)/np.sqrt(2)
    I_RMS = (I_PP/2)/np.sqrt(2)

    PF = np.cos(phase*np.pi/180)

    P_RMS = V_RMS*I_RMS*PF

    data['power'] = data.voltage*data.current

    P_MAX = data.power.max()
    P_MIN = data.power.min()

    V_rect = V_PP/np.pi
    I_rect = I_PP/np.pi

    return (V_PP, I_PP, V_RMS, I_RMS, V_rect, I_rect, P_RMS, P_MAX, P_MIN, PF, T_period, freq, phase)
