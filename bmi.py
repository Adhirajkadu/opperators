height=float(input("enter height in m: "))
weight=float(input("enter weight in kg:  "))

bmi=weight/height**2
print("your bmi is ",bmi)

if bmi <=18.4:
    print("you are under weight." )
elif bmi <=24.9:
    print("your are healthy")
elif bmi <=29.9:
    print("your are over weight")
elif bmi <=34.9:
    print("your are obese")
else :
    print ("you are severly obese") 