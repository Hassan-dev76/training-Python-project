# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"The name of the employee is {self.name} str"
    
#     def __repr__(self):
#         return f"Th name of the employee is {self.name} repr"
    



# obj = Employee("Hassan")

# print(obj)


class MyClass:
          def __call__(self, name):
              print(f"Hello, {name}")

class YourClass(MyClass):
       def __init__(self, name:str):
            #   super().__init__()
              self.name = name

       def __call__(self, age: int):
              super().__call__(self.name)
              print(f"{self.name}. Your are {age} years old")



obj = MyClass()
obj2 = YourClass("Hassan")
# obj("Hassan")  # work with the help of __call__ method
obj2(22)