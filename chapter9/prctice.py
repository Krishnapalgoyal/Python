def gretest_number(a,b,c):
    if a>b and a>c:
      print("a is gretest")
    elif b>c and b>a:
      print("b is gretest")
    elif c>a and c>b:
       print("c is gretest")
    else:
       print(" all areeqal")

a = int(input("Please inter no a :"))
b = int(input("Please inter no b :"))
c = int(input("Please inter no c :"))


gretest_number(a,b,c)
