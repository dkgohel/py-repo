num = input("Enter a number : ")

originalNum = int(num)

n= len(num)

sum = 0

for i in range(n):
    sum+=(int(num[i])**n)

if sum==originalNum:
    print("Armstrong !")
else:
    print("Not armstrong !")
