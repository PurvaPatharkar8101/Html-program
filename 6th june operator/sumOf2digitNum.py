#wap to find sum of 2 digit number.

num=int(input("Enter 3 digit number:"))
sum=0

sum=sum+num%10
num=num//10

sum=sum+num%10
num=num//10

# sum=sum+num%10
# num=num//10

print("Sum=",sum)
