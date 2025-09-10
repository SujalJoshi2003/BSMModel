import math 
def inputBasedCalculator(S, K, T, r, sigma):
    d1 = (math.log(S / K)+(r + 0.5*sigma**2)*T)/(sigma*(T**0.5))
    d2 = d1 - sigma*(T**0.5)
    N_d1 = 0.5 * (1 + math.erf(d1 /(2**0.5)))
    N_d2 = 0.5 * (1 + math.erf(d2 /(2**0.5)))

    call = S*N_d1 - K*math.exp(-r*T)*N_d2
    put = K*math.exp(-r*T)*(1-N_d2) - S*(1-N_d1)

    return call,put

