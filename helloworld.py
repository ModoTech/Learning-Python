import random
if 5 > 2:
    print("Five is greater than 2")

s = 8
y = "Hello world"
print (y)
print(s)
 
c = 7
c = "string"

print(c)

d = "Python"
e = "Is"
h = "Awesome"

print(d,e,h)
print (d+" "+ e+" "+h)

print (random.randrange(1,10000))

t = "RB44WCNLC4 Confirmed.on 4/2/23 at 6:10 PMKsh1,500.00 received from 254720527128 GEORGE N KAMAU. New Account balance is Ksh9,492.62. Transaction cost, Ksh7.50"
code = t[1]
date = t[3]
fname = t[10]
phoneNumber = t[9]

print(fname + "paid for his subscription on " + date + "," + " payment confirmation code is " + code + "." + "using phone number : "  + phoneNumber)
