weight = float(input())
height = float(input())

bmi = weight / (height**2)

if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"

print(category)
