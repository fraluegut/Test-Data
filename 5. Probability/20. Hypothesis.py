import math

def normal_cdf(x, mu=0, sigma=1):
    return(1+math.erf(x-mu)/math.sqrt(2))/2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu!=0 or sigma!=1:
        return mu*sigma*inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0,0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z)/2
        mid_p = normal_cdf(mid_z)
        if mid_p <p:
            low_z, low_p = mid_z, mid_p
        elif mid_p>p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

normal_probability_below = normal_cdf

def normal_probability_above(lo, mu=0, sigma=1):
    return 1- normal_cdf(lo, mu, sigma)

def normal_probability_between(lo, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo, mu=0, sigma=1):
    return  1- normal_cdf(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(probability, mu, sigma)

