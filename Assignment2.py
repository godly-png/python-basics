# 1. Write a Python program to find the sum of all elements in a list.

# list1=[2+3]
# list2=[3+5]
# list3=list1+list2
# print(list3)


# list=[2,3,4,5,5]
# total=sum(list)
# print(total)


# 2 . Find the intersection and union of two lists.


# a=[2,4,5,7]
# b=[5,8,7,9]
# set_a=set(a)
# set_b=set(b)
# union=set_a | set_b
# intersection=set_a & set_b
# print("union",list(union))
# print("intersection",list(union))


# 3. Convert a list to a tuple and vice versa.

# x=('apple','orange','fruits','melon','guava')
# y=list(x)
# x=tuple(y)
# print(x)
# print(y)


# 4. Count occurrences of an element in a tuple.


# x=(2,5,7,9,8)
# y=x.count(5)
# print(y)


# x=(2,5,7,8,9,8)
# y=x.count(8)
# print(y)


# 5. Find the union, intersection, difference of two sets.

# union--------

# set1={1,2,3,4,5}
# set2={0,9,8,7,6}
# set3= set1 | set2
# print(set3)

# intersection---------

# set1={1,2,3,4,5}
# set2={0,9,4,7,6}
# set3= set1 & set2
# print(set3)


# Difference--------

# set1={1,2,3,4,5}
# set2={0,2,4,7,6}
# set3= set1 - set2
# print(set3)





# 6. Check if two sets are disjoint.


# a={'a','b','c','d'}
# b={'a','r','w','q'}
# result=a.isdisjoint(b)
# print(result)

# a={'a','b','c','d'}
# b={'n','r','w','q'}
# result=a.isdisjoint(b)
# print(result)




# 7. Add and remove elements from a set.

# set1={'apple','orange','kiwi','fruits'}
# set1.add('car')
# print(set1)


# set1={'apple','orange','kiwi','car','fruits'}
# set1.remove('car')
# print(set1)



# 8. Merge two dictionaries.

# dict={7,8,0,4}
# dict1={'o','u','p','p'}
# result=dict|dict1
# print(result)


# 9. Create a list of n elements from user input.


# list1=(input("enter the value:"))
# fruits=['apple','orange']
# fruits.append(list1)
# print(fruits)



# 10. Append, insert, and delete elements from a list.


# list1=['apple','orange']
# list1.append('kiwi')
# print(list1)

# list1=['mango','pineapple','orange']
# list1.insert(2,'kiwi')
# print(list1)

# list1=['car','bike','scooter']
# del list1[1]
# print(list1)


# 11. Create a tuple with different data types.Access tuple elements by index.Convert a list to a tuple
# and vice versa.Concatenate two tuples.Find the length of a tuple.Check if an element exists in a
# # tuple.

# x=('car','bus','bike','auto')
# h=('apple','orange')
# y=list(x)
# print(y)
# z=tuple(x)
# print(z)
# y=x.index('bike')
# print(y)
# result=x + h
# print(result)
# print(len(result))
# if 'orange' in result:
#     print('yes')
# else:
#     print('no') 




# 12.Create a dictionary with at least 5 key-value pairs.Access and print a value using its key.Update
# the value of an existing key.Add a new key-value pair to a dictionary.Delete a key from a dictionary
# using del or .pop().


# dict1={
#     'name':'godly',
#     'branch':'AI',
#     'place':'allapuzha',
#     'background':'Engineering',
#     'year':2025
# }
# x=dict1.items()
# print(x)
# dict1['place']='ernakulam'
# dict1['month']='6'
# dict1.pop('branch')
# print(dict1)



# 13. Create a set of integers from user input.Add a single element to a set.Add multiple elements to a
# set using .update().Remove an element using .remove() and .discard() — show the
# difference.Clear all elements from a set.


# a=int(input("enter the inetegers:"))
# b=int(input("enter the inetegers:"))
# set1={a}
# set2={b}
# set1.add(3)
# print('adding element is:',set1)
# set1.update([2])
# print('updated value:',set1)
# set2.remove(3)
# print('removed value is:',set2)
# set1.discard(5)
# print('discarded value is:',set1)
# set1.clear()
# print('after clear:',set1)




# # 14. Find the symmetric difference between two sets.


# set1={'apple','orange'}
# set2={'kiwi','papaya'}
# x=set1^set2
# print(x)



# 15.Remove common elements from a set.

# set={'apple','orange','banana'}
# set1={'orange','kiwi'}
# x=set-set1
# print(x)