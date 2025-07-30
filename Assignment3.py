# 1.Write a function that returns the square of a number.

# def num_1(square):
#        result=square**2
#        print(result)
# num_1(5)


# 2. Write a function that checks if a number is even or odd.

# def num_1(num):
#     if num %2==0:

#         print(f"{num},is even")
#     else:
#         print(f"{num},is odd")
# num_1(1)


# 3. Write a function that adds two numbers.

# def num_1(a,b):
#     sum=a+b
#     print("sum:",sum)
# num_1(a=2,b=3)


# 4. Write a function that returns the factorial of a number.

# def num_1(x):
#     fact=1
#     for i in range(1,x+1):

#         fact *=i

#     print("fact:",fact)

# num_1(6)


# 5. Write a function to check if a string is a palindrome.





# 6. Write a function to find the maximum number in a list.

# def max_num(*nums):
#  max_value = nums[0]

#  for num in nums:
#         if num > max_value:
#             max_value = num

#             print("Max_num:", max_value)
# max_num(67,90,87)








# x=lambda a,b,c:a+b+c
# print(x(2,4,6))


# def myfun(n):
#     return lambda a:a*n
# result=myfun(2)
# print(result(22))

# n=(2,3,5,6)
# def square(n):
#     return n*n
# squared=map(square,n)
# result=tuple(squared)
# print(result)

# n=(3,6,5,1)
# result=map(lambda x:x*x,n)
# print(result)
# print(set(result))


# def even(n):
#     if n%2==0:
#         return True
#     return False
# n=(3,6,5,2)
# result=filter(even,n)
# result1=list(result)
# print(result1)


# from functools import reduce
# def add(x,y):
#     return x+y
# a=(94,7,5,8)
# res=reduce(add,a)
# print(res)

