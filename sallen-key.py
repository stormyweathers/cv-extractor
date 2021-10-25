from numpy import sqrt,pi
R=101e3
C=200e-6
R2=1e3

## These choices fix Q=1/sqrt(2)
## Giving a second order butterworth filter
R1,R2=R,R
C1,C2=2*C,C

w0=1/sqrt(R1*R2*C1*C2)
eta=1/C1 * (R1+R2)/(R1*R2)
Q=w0/eta


print("Design choices")
print("R1={:.0f} kOhm, R2={:.0f} kOhm, C1={:.0f} uF, C2={:.0f} uF".format(R1/1e3,R2/1e3,C1*1e6,C2*1e6))
print("cutoff freq: {:.2f} Hz, Q={:.2f}".format(w0*2*pi,Q))
