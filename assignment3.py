#!/usr/bin/env python
# coding: utf-8

# ## Assignment 3
# #### Feb. 21 2023
# ### Ke Jia (Gary)

# ***
# **1.  Write a lambda expression to get the product of two numbers.**
# 
#     Run test for expression(5,6)
#     Output:30

# In[1]:


multiply = lambda x,y: x*y
print(multiply(5, 6))


# ***
# **2. Write a function to get the area of a circle from the radius.**
# 
#     Hint: remember to import the right modul for being able to calculte the area of the circle.
#     Run test for function(10)
#     Output: 314.1592653589793
# 

# In[2]:


import math

def calculte_circle_area(radius):
    return math.pi * radius ** 2

print(calculte_circle_area(10))


# ***
# **3. Build a simple calculator which can: add, subtract, multiply, divide.**
# 
#     Hint: solve by writing a function that takes as argument two numbers and the operation and returns the desired output.
#     Run test for function(2,5,’d’)
#     Output: 0.4

# In[3]:


def calculator(num_1, num_2, operator):

    operations = {
        'a': lambda x,y: x+y,
        's': lambda x,y: x-y,
        'm': lambda x,y: x*y,
        'd': lambda x,y: x/y,
    }

    operate = operations.get(operator)
    return operate(num_1, num_2)


print(calculator(2, 5, 'd'))


# ***
# **4.Define a class named Rectangle which can be constructed by a length and width.**
# 
#     The Rectangle class has a method which can compute the area.
#     Run test for 
#         r = Rectangle(5,10)
#         r.area()
#     Output: 50

# In[4]:


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle(5, 10)
print(r.area())


# ***
# **5. Define a class named Shape and its subclass Square.**
# 
#     Shape objects can be consrtucted by name and length has an area function wich return 0
#     
#     Square subclass has an init function which take a length and name as argument and has an area method and a describe method what prints the name of the Shape.
#     
#     Print the area from Square class.
#     
#     Run test for:
#         s = Square('square',5)
#         print(s.area())
#         print(s.describe())
#     
#     Output: 
#         The area is:
#             25
#         This is a: square

# In[5]:


class Shape:
    
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def area(self):
        return 0


class Square(Shape):
    
    def area(self):
        return f'The area is:\n    {self.length ** 2}'
    
    def describe(self):
        return f'This is a: {self.name}'

    
s = Square('square', 5)
print(s.area())
print(s.describe())


# In[ ]:




