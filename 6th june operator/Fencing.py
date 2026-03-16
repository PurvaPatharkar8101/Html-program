''' wap to find the cost of fencing the given area based on the length,breadth,
     no. of time fencing and cost of fencing and cost of fencing.   '''

l=int(input("Enter the length :"))
b=int(input("Enter the breadth:"))
num=int(input("Enter number of times fencing:"))
cost=int(input("Enter the cost of fencing:"))
peri= l + b + l + (22*b)/(7*2)
total_cost= peri*cost*num
print("Total cost of fencing is: ",total_cost)
