import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

def full_amplitude_fft(t, x):
    full_amplitude_spectrum = np.abs(np.fft.fft(x))
    N = len(full_amplitude_spectrum)
    full_amplitude_spectrum = full_amplitude_spectrum/N
    full_freqs = np.fft.fftfreq(x.size, np.mean(np.ediff1d(t)))
    return full_freqs, full_amplitude_spectrum

def one_sided_fft(t,x):
    full_amplitude_spectrum = np.abs(np.fft.fft(x))/x.size
    full_freqs = np.fft.fftfreq(x.size, np.mean(np.ediff1d(t)))
    oneinds = np.where(full_freqs >=0.0)
    one_sided_freqs = full_freqs[oneinds]
    one_sided_amplitude_spectrum=2*full_amplitude_spectrum[oneinds]
    return one_sided_freqs, one_sided_amplitude_spectrum

def power_spectrum(t,x):
    onef, oneamps = one_sided_fft(t,x)
    return onef, oneamps**2

def lomb_scargle_pspec(t, x):
    tstep = np.mean(np.ediff1d(t))
    freqs = np.fft.fftfreq(x.size, tstep)
    idxx = np.argsort(freqs)
    freqs2 = freqs[idxx]
    freqs2 = freqs2[freqs2>0]
    try:
        pgram = sp.lombscargle(t, x, freqs2*2*np.pi)
    except:
        #slightly perturb frequencies to prevent crashes
        #in case of perfectly evenly spaced data
        #print "Warning: perturbed frequencies a bit to avoid bug in scipy"
        #freqs2=freqs2*(1+0.00001*np.random.random(freqs2.size))
        pgram = sp.lombscargle(t, x, freqs2*2*np.pi)
    return freqs2, (pgram/(t.size/4))

def lomb_scargle_ampspec(t, x):
    tstep = np.mean(np.ediff1d(t))
    freqs = np.fft.fftfreq(x.size, tstep)
    idxx = np.argsort(freqs)
    freqs2 = freqs[idxx]
    freqs2 = freqs2[freqs2>0]
    try:
        pgram = sp.lombscargle(t, x, freqs2*2*np.pi)
    except:
        #slightly perturb frequencies to prevent crashes
        #in case of perfectly evenly spaced data
        #print("Warning: perturbed frequencies a bit to avoid bug in scipy")
        #freqs2=freqs2*(1+0.00001*np.random.random(freqs2.size))
        pgram = sp.lombscargle(t, x, freqs2*2*np.pi)
    return freqs2, np.sqrt(pgram/(t.size/4))

if __name__ == "__main__":

    fs = 200.0
    fund_freq=15
    ampl = 10
    t = np.arange(0,10,1/fs)
    x = ampl*np.cos(2*np.pi*fund_freq*t)+ ampl*2*np.sin(2*np.pi*fund_freq/2.0*t)
    

    #Calculate the FFTs/power spectra using different methods
    fullf, fullampspec = full_amplitude_fft(t,x)
    onef, oneampspec = one_sided_fft(t,x)     
    powerf, powerspec = power_spectrum(t,x)    
    lsf, lspspec = lomb_scargle_pspec(t,x)
    lsf2, lsaspec = lomb_scargle_ampspec(t,x)

    #Plot the results
    fig, ((ax0, ax1), (ax2, ax3), (ax4, ax5)) = plt.subplots(nrows=3, ncols=2)
    ax0.plot(t, x)
    ax0.set_title('Input Data, '+str(fund_freq)+
                  ', '+str(fund_freq/2.0)+
                  ' Hz; '+
                  '\nAmplitude: '+str(ampl)+
                  ', '+str(ampl*2.0)+
                  '; Fs = '+str(fs)+' Hz')
    ax0.set_ylabel('Volts')
    ax0.set_xlabel('Time[s]')
    
    ax1.plot(fullf, fullampspec)
    ax1.set_title('Full Amplitude Spectrum')
    ax1.set_ylabel('Volts')
    ax1.set_xlabel('Freq[Hz]')
    
    ax2.plot(onef, oneampspec)
    ax2.set_title('One-sided Amplitude Spectrum')
    ax2.set_ylabel('Volts')
    ax2.set_xlabel('Freq[Hz]')
    
    ax3.plot(powerf, powerspec)
    ax3.set_title('FFT Power Spectrum')
    ax3.set_ylabel('Volts**2')
    ax3.set_xlabel('Freq[Hz]')
    
    ax4.plot(lsf, lspspec)
    ax4.set_title('Lomb Scargle Power Spectrum')
    ax4.set_ylabel('Volts**2')
    ax4.set_xlabel('Freq[Hz]')
    
    ax5.plot(lsf2, lsaspec)
    ax5.set_title('Lomb Scargle Amplitude Spectrum')
    ax5.set_ylabel('Volts')
    ax5.set_xlabel('Freq[Hz]')
    
    fig.tight_layout()
    plt.subplots_adjust(hspace=.72)    
    plt.subplots_adjust(wspace=.72)    
    plt.show()


