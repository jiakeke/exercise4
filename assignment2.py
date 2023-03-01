#!/usr/bin/env python
# coding: utf-8

# ## Assignment 2
# ### Feb. 16th 2023
# ### Ke Jia

# ***
# **Question 1.**

# In[1]:


var_1 = 100
var_2 = 29
var_3 = (3*(var_1+var_2))**2
print("The result of the calculation was:")
print(" "*7, var_3)


# ***
# **Question 2.**

# In[2]:


name = input("Name: ")
year = input("Year of birt: ")
age = input("Age: ")
password = '%s%s%s' % (year[-2:], name[:3], int(age)**2)
print("Password:", password)


# ***
# **Question 3.**

# In[3]:


num_1 = int(input("First number: "))%2
num_2 = int(input("Second number: "))%2
if num_1 and num_2:
    print("Both numbers are odd")
elif num_1 or num_2:
    print("One of the numbers is even")
else:
    print("Both numbers are even")


# ***
# **Question 4.**

# In[4]:


num = int(input("Give an integer: "))
amount = 0
for item in range(num):
    amount += item
print("The sum was:", amount)


# ***
# **Question 5.**

# In[5]:


import random
number = random.randint(0, 10)
times = 0

while 1:
    times += 1

    guess = int(input("Player: "))
    if number == guess:
        print("That’s right! Number of tries:", times)
        break
    elif number > guess:
        print("Try a greater number")
    else:
        print("Try a smaller number")


# ***
# **Extended solution for question 5**

# In[6]:


import random

def play(num=''):
    player = 'Player%s: ' % num

    number = random.randint(0, 10)
    times = 0
    while 1:
        times += 1
        guess = int(input(player))
        if number == guess:
            print("That’s right! Number of tries:", times, "\n\n")
            return times
        elif number > guess:
            print("Try a greater number")
        else:
            print("Try a smaller number")

times_1 = play(1)
times_2 = play(2)


if times_1 > times_2:
    print("Winner is Player2")
elif times_1 < times_2:
    print("Winner is Player1")
else:
    print("The match ended in a draw.")


# In[ ]:




