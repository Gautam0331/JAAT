# from gautamrana import Gautam
# print(Gautam())
# def william(name):
#     print(f"{name} hello ")

# william("john")    
# def william(name):
#     print(name,"says hello ")

# # william("john")   
# def william(name):
#     print(name,"says hello ")

# name_1=input("enter a name:")
# name_2=input("enter a name:")
# william(name_1)
# william(name_2)

# def even():
#     numb=int(input("Enter "))
#     if numb%2==0:
#         return numb," is even"
#     else:
#         return numb,'is odd'
# print(even())
# def even():
#     numb=int(input("enter: "))
#     for i in range(12):
#         if numb%2==0:
#             return " is even"
#         else:
#             return 'is aaaa' 
# print(even())
# def check(lst):
#     first_type=type(lst[3])
#     for item in lst:
#         if first_type==type(item):
#             return "these are same"
#         else:
#             return "these are not same"
# print(check([10,34,23,"anuj",234,"gautam"])) 
# try:
#     num=int(input("Enter a numer: "))
#     print("number is", num)
# except ValueError:
#     print("Please enter a valid number")
# def safe_divide(a, b):
#     if b == 0:
#         print("Cannot divide by zero")
#     else:
#         return a / b
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
def find_max(a=13,b=16,c=19):
    if a >= b and a >= c:
        return True
    elif b >= a and b >= c:
        return False
    else:
        return "Gandu"

print(find_max())









