class Info:
    age = 18

    def __init__(self): ## dunder methods
        print("I am creating a methods")
    

    def getInfor(self):
        print(f"my age is  {self.age}")

    @staticmethod
    def grit():
        print("Good morning")
        

my = Info()
test = my.getInfor()
grit = my.grit()
print(test)
print(grit)