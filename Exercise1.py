IntrestRate = 0.08
Principal = 10000
NPaymentsPY = 12
NofYears = 5
A = IntrestRate * (Principal/NPaymentsPY)
B = 1-(((IntrestRate/NPaymentsPY)+1)**(-NPaymentsPY*NofYears))
Payment = A/B
print(Payment)
