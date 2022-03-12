from numpy.fft import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_freq_and_phase(data):

    data = data.to_numpy()

    v = data[:,1]
    i = data[:,2]
    t = data[:,0]
    t_s = data[2,0]-data[1,0]
    f_s = 1/t_s

    v = np.pad(v, (0,len(v)*15))
    i = np.pad(i, (0,len(i)*15))

    V = fft(v)
    I = fft(i)
    N = len(V)
    n = np.arange(N)
    T = N/f_s
    freq = n/T 
    
    # plt.figure(1, figsize = (12, 6))
    # plt.plot(freq, np.angle(V))
    # plt.xlabel('Freq (Hz)')
    # plt.ylabel('FFT Amplitude |X(freq)|')
    # plt.xlim(0, 100)
    
    # plt.figure(2, figsize = (12, 6))
    # plt.plot(freq, np.angle(I))
    # plt.xlabel('Freq (Hz)')
    # plt.ylabel('FFT Amplitude |X(freq)|')
    # plt.xlim(0, 100)

    # plt.show()

    abs_V = np.abs(V)
    abs_I = np.abs(I)
    
    ang_V = np.angle(V)
    ang_I = np.angle(I)
    
    abs_V = pd.DataFrame(data=abs_V)
    abs_I = pd.DataFrame(data=abs_I)

    f_V = freq[abs_V[0][0:np.where(freq>100)[0][0]].idxmax()]
    f_I = freq[abs_I[0][0:np.where(freq>100)[0][0]].idxmax()]
    
    f0 = (f_V + f_I)/2
    phi = ang_V[np.where(freq==f_V)[0][0]] - ang_I[np.where(freq==f_I)[0][0]]
    phi *= 180/np.pi
    if phi > 180:
        phi -= 360

    return (f0, phi)

if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    from fourier import get_freq

    data = pd.read_csv('data\OSCsampl1.csv', delimiter=',')
    
    freq, phi = get_freq(data)
    print('Frequency:', freq)
    print('Phase:', phi)
    
    