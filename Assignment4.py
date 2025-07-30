# Q1. Square a number using a lambda function

# x=lambda x:x**2
# print(x(6))


# Q2. Add two numbers using lambda

# x=lambda n,x:x+n
# print(x(7,10))


# Q3. Use lambda and map() to square all numbers in a list


# n=(5,9,10,55)
# result=map(lambda x:x*x,n)
# print(set(result))
# print(result)


# Q4. Use lambda and filter() to get even numbers


# def even(n):
#     if n%2==0:
#         return True
#     return False
# n=(5,8,3,4)
# result=filter(even,n)
# result1=set(result)
# print(result1)


# n=(4,5,7,8)
# result=filter(lambda x:x%2==0,n)
# result1=print(set(result))



# Q5. Sort a list of tuples based on the second value using lambda

# n=(3,5,7,4)
# # def value(n):
# #     return value
# result=lambda x:x
# print(list(result(n)))



# Q6. Use lambda with reduce() to compute the product of all elements


# from functools import reduce
# def prod(x,y):
#     return x*y
# a=(4,7)
# result=reduce(lambda x,y:x*y,a)
# print(result)



# Q7. Use lambda with map() to convert a list of strings to uppercase
# words = ['hello', 'world']

# words=['hello','world']
# def to_upper(words):
#     return words.upper()
# upper=map(to_upper,words)
# result=(list(upper))
# print(result)




# Q8. Sort a list of dictionaries by a key using a lambda
# people = [
# {"name": "Alice", "age": 30},
# {"name": "Bob", "age": 25},
# {"name": "Charlie", "age": 35}
# ]

# people = [
# {"name": "Alice", "age": 30},
# {"name": "Bob", "age": 25},
# {"name": "Charlie", "age": 35}
# ]

# sorted_list = sorted(people,key=lambda x: x['age'])
# print(sorted_list)


# Q9. Write a function that returns a lambda that multiplies by a given number

# def multiplier(n):
#     return lambda x:x*n
# times2=multiplier(2)
# times3=multiplier(3)
# num=int(input("entrer the number:"))
# print(times2(num))
# print(times3(num))



# Q10.Use lambda to sort a list of strings by the number of vowels
# words = ['apple', 'banana', 'grape', 'kiwi']



# words = ['apple', 'banana', 'grape', 'kiwi']
# sortedlist=sorted(words,key=lambda x: sum('c' in 'aeiou' for c in x.lower()))
# print(sortedlist)



# Q11.Use lambda and filter() to get palindromes from a list
# words = ['madam', 'hello', 'noon', 'python']


# words = ['madam', 'hello', 'noon', 'python']

# palindromes = list(filter(lambda words: words == words[::-1], words))

# print(palindromes)



# Q12. Use lambda with reduce() to concatenate only capitalized strings
# words = ['Hello', 'world', 'From', 'python']

# from functools import reduce

# words = ['Hello', 'world', 'From', 'python']

# result = reduce(lambda a, b: a + b, filter(lambda word: word.istitle(), words))

# print(result)



# Q13.Filter products by price range using filter() and lambda



# products = [
# {"name": "Laptop", "price": 900},
# {"name": "Phone", "price": 500},
# {"name": "Tablet", "price": 300},
# {"name": "Monitor", "price": 200}
# ]
# filtered_products = filter(lambda x: min_price <= x['price'] <= max_price, products)
# print(list(filtered_products))



# Q14. Categorize numbers into even or odd using map() and lambda


# numbers = [10, 15, 22, 33, 42]
# categories = map(lambda x: 'Even' if x % 2 == 0 else 'Odd', numbers)
# print(list(categories))


# Q15.Use lambda to extract domain names from emails

# emails = ['alice@example.com', 'bob@gmail.com', 'carol@yahoo.com']
# domains = map(lambda email: email.split('@')[1], emails)
# print(list(domains))