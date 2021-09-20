
name= input("enter your name")
print(f"Hi {name}, What is your Age?")

age = input("enter your age")
weight=float(input("enter your weight"))
height=float(input("enter your height in meter"))


def your_bmi(weight,height):
    bmi= round(weight/ (height * height), 1)
    return bmi
 

def find_condition_from_bmi(bmi):
    if bmi < 18.5:
        print(f"Your BMI is {bmi} which means you are underweight.")
    elif bmi > 18.5 and bmi < 24.9:
        print(f"Your BMI is {bmi} which means you are Normal.") 
    elif bmi > 25.00 and bmi < 29.9:
        print (f"Your BMI is {bmi} which means you are overweight") 
    else:
        print(f"Your BMI is {bmi} which means you are Obese.")  


bmi= your_bmi(weight,height) 
find_condition_from_bmi(bmi)