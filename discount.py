# input sales and offer discount based on sales
#  if sales >= 10,000 -> discoun 10%
# otherwise discount is 5%

sales = int(input("Enter sales: "))

if sales >= 10000:
    discount = sales * 0.1
else:
    discount = sales * 0.05
print(discount)
