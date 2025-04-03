# IF ELSE AND ELIF in pyhton 

age = int(input("age of the user: "))
print (age)
if (age>18):
    print("You are now able to vote")
elif(age>60):
    print("You are not allowed to vote over age")
else:
    print(f"you are under age {age}")

