# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi=float((float(weight))/height **2)

if (bmi < 18.5):
    weight = "underweight"
elif bmi > 18.5 and bmi < 25:
    weight="normal weight"
elif bmi > 25 and bmi < 30:
    weight="slightly overweight"
elif bmi > 30 and bmi < 35:
    weight="obese"
else:
    weight="clinically obese"


print(f"Your BMI is {bmi}, you are {weight}.")