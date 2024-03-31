# while True:
#     age = input("How old are you? ")
#     try:
#         age = int(age)
#         if age >= 18:
#             print("Accept allowed")
#             break
#         else:
#             print("Accept denied")
#             break
#     except ValueError:
#         print(f"{age} is not number, please write number!")
#     finally:
#         print("-"*14)

a = "(25+48)**2-(46/2)"
b = "(45+48)"
print("c=a + b") 
print("c =", a, "+", b, "=", eval(a)+ eval(b))

a = 70>>3
b = ~a
c = a<<1
print(a, b, c)
