# f=open("filehandling.txt",'r')                  
# read=f.read()
# print(read)
# f.close()
# f=open("filehandling.txt","r")
# read=f.readlines()
# print(read)
# f.close()
# class Volleyball:
#     def anuj(self,name):
#         print(name)
#     def gautam(self,name):
#         print(name)
#     def nikhil(self,name):
#         print(name)
# object=Volleyball()
# object.anuj("defender")
# object.gautam("attack")
# object.nikhil("smash")
# class Volleyball:
#     team_name="AIPA Dehradun"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_details(self):
#         print(f"Player name is {self.name} and he is {self.age} old")
# a=Volleyball("Gautam",23)
# a.get_details()

# b=Volleyball("Anuj",20)
# b.get_details()
class Animal:
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    def dog(self):
        return(self.name,self.age ,self.breed)
    def cat(self):
        return(self.name,self.age,self.breed)
    def cow(self):
        return(self.name,self.age,self.breed)
    def get_deatail(self):
        print(f"its name is {self.name} and breed is {self.breed} age is {self.age}")
a=Animal("Johnny",3,"husky")
a.get_deatail()
b=Animal("Julie",5,"Persian")
b.get_deatail()
c=Animal("Basanti",7,"Panganur")
c.get_deatail()

