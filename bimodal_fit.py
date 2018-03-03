from pylab import *
from scipy.optimize import curve_fit

#Histogram of the filtered signal
y,x,_ = hist(lowpass_signal,30,alpha=.3,label='data')
x=(x[1:]+x[:-1])/2 # for len(x)==len(y)

#A double - gaussian fit to the bistable histogram
def gauss(x,mu,sigma,A):
    return A*exp(-(x-mu)**2/2/sigma**2)

def bimodal(x,mu1,sigma1,A1,mu2,sigma2,A2):
    return gauss(x,mu1,sigma1,A1)+gauss(x,mu2,sigma2,A2)

#Ad hoc starting parameters for the fit
expected=(-0.003, 0.002, 60, 0.004, 0.0025, 50)

params,cov=curve_fit(bimodal,x,y, expected)

plot(x,bimodal(x,*params),color='red',lw=3,label='model')
for i in range(0, len(params)):
    print(params[i]) 
    
#In case of usefulness add lines to compute parameters' errors
