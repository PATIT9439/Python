name= input("enter your name")
print(f"Hi {name}, What is your Age?")

age = input("enter your age")
weight=float(input("enter your weight"))
height=float(input("enter your height in meter"))


def your_bmi(weight,height):
    bmi= round(weight/ (height * height), 1)
    return bmi
bmi = your_bmi(weight,height)

print(f"The BMI is{bmi}")