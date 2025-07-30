# Write a program to read a text file and display its contents.
# # • File: sample.txt


# f=open('sample.txt','x')
# with open('sample.txt','w')as f:
#     f.write('hey hello')
# f=open('sample.txt','r')
# print(f.read())



# • Write a program to count the number of lines, words, and characters in a file.



# with open('sample.txt', 'r') as f:
#     data = f.read() 
# lines = data.split('\n')
# words = data.split()
# characters = len(data)
# print("Number of lines:", len(lines))
# print("Number of words:", len(words))
# print("Number of characters:", characters)




# • Write a program to append a new line of text to an existing file.



# f=open('sample.txt','a')
# f.writelines(['/n hi godly','/n hello'])
# f.close




# • Write a program to create a new file and write user input into it until the user types
# "exit".


# with open('input.txt', 'w') as f:
#     while True:
#         text = input("enter the type ( 'exit' to stop): ")
#         if text.lower() == 'exit': 
#             break
#         f.write(text + '\n') 




# • Write a program that reads a file and prints only the lines that contain the word
# # "Python".




# with open('sample.txt','a')as f:
#     f.writelines(['\npython is easy',
#                   '\n python is famous',
#                   '\nhello everyone'])
# with open('sample.txt', 'r') as file:
#     for line in file:
#         if 'python' in line.lower():
#             print(line, end='')



# • Write a program that tries to read a file and handles the FileNotFoundError.

# try:
#     with open('myfile.txt', 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found. Please check the filename and try again.")



# • Write a program that takes an integer input and handles ValueError if the input is
# # not valid.


# try:
#     number = int(input("Enter an integer: "))
#     print("You entered:", number)
# except ValueError:
#     print("not valid.")


# • Create a class Car with attributes like make, model, and year. Create an object and
# # print its attributes.


# class car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#     def printname(self):
#         print(self.make,self.model,self.year)
# x=car('hyundai','verna','1999')
# x.printname()



# • Write a class Rectangle with methods to compute area and perimeter. Create an
# object and display its area and perimeter.


# class reactangle:
#     def __init__(self,lenght,width):
#         self.lenght=lenght
#         self.width=width
#         self.area = self.lenght * self.width
#         self.perimeter = 2 * (self.lenght + self.width)
#     def printname(self):
#         print(self.area,self.perimeter)
# x=reactangle(lenght=20,width=3)
# x.printname()


# • Demonstrate constructor overriding in inheritance. Use super() to call the parent
# # constructor.



# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#         print("Vehicle constructor called")


# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)  
#         self.model = model
#         print("Car constructor called")

#     def display_info(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
# my_car = Car("Toyota", "Corolla")
# my_car.display_info()
      