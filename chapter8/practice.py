# 
# l = ["ram", "sham","shekhar", "sidharth"]

# for name in l:
#     if(name.startswith("s")):
#         print(f"Hello {name}")

n = int(input("enter a number: "))

for i in range(2,n):
    if (n%i)==0:
        print("Number is not a prime number")
        break
else:
    ("Number is prime ")
    
