def Instalment(IntrestRate,NPaymentPY,NOYears,Principal):
       A= IntrestRate * (Principal/NPaymentPY)
       B= 1- (((IntrestRate/NPaymentPY)+1)** (-NPaymentPY * NOYears))
       payment = A/B
       return payment
var = Instalment(0.01,5,4,40000)
print(var)
