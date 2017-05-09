weight=float(input("Please input your weight(kg): "))
height=input('Please input your height(meter): ')
bmi=weight/height**2
def print_bmi(bmi):
    print("Your BMI is %.2f"%bmi)
if bmi<18.5:
    print_bmi(bmi)
    print "You are under weight"
elif bmi<24:
    print_bmi(bmi)
    print "You are fit !"
else:
    print_bmi(bmi)
    print "You are overweight!"
    
