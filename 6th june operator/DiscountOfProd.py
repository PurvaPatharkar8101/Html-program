# wap to find price of the product based on discount?

original_price=int(input("Enter price of the product:"))
discount=int(input("Enter discount: "))
#discount=original_price*discount/100
total=original_price - original_price*discount/100
print("discounted price is:",total)