bill_amount = int(input("Enter bill amount = "))
if bill_amount > 50000:
    discount = 30
elif bill_amount >= 40000:
    discount = 25
elif bill_amount >= 30000:
    discount = 20
elif bill_amount >= 10000:
    discount = 10
else:
    discount = 0

discount_amount = bill_amount * discount / 100
final_amount = bill_amount - discount_amount
print(f"You got {discount*100}% discount")
print(f"Your final bill is Rs. {final_amount}")
