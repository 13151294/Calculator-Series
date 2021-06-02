import math
def lcmCal(a,b):
    return int((a * b)/math.gcd(a,b))
def gcdCal(a,b):
    return int(math.gcd(a,b))
listNum = list(map(int, input("Enter the Number : ").split()))
lcm = lcmCal(listNum[0],listNum[1])
gcd = gcdCal(listNum[0],listNum[1])
for i in range(2, len(listNum)):
    lcm = lcmCal(lcm, listNum[i])
for i in range(2, len(listNum)):
   gcd = gcdCal(gcd, listNum[i])
print("LCM is : ",lcm)
print("GCD is : ",gcd)