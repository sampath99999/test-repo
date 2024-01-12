# num1 = int(input("enter first number n :"))
# num2 = int(input("enter second number n :"))
# num3 = int(input("enter third number n :"))
# max_input = max(num1, num2, num3)
# print(max_input)
# ===========================================
# Write a Python program to check if a character is a vowel or consonant.
# alphabet=input("enter any alphabet :")
# if alphabet.lower() in ['a','e','i','o','u']:
#     print(f"{alphabet} is an vowel")
# else:
#     print(f"{alphabet} is a constant")

# num1 = int(input("enter first number n :"))
# num2 = int(input("enter second number n :"))
# num3 = int(input("enter third number n :"))
# avg_input = (num1+num2+num3)/3
# print(f"the average of 3 numbers is {avg_input}")


# num=int(input("enter any number n:"))
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     multiply= num *i
#     print(f"{num}*{i}={multiply}")

# a={1,2,3,4,2,3,4,0,1,8,9,4,20,"python"}
# print(type(a))
# a.update({12,13})
# a.pop()
# a.remove(2)
# print(a)

# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# a=2
# b=5
# def add(a,b):
#     return a+b
# print(add(1,5))

# def outer():
#     print("outer")
#     def inner():
#        print("inner")
#     inner()
# outer()

# def func(**a):
#     print("this is function",a)
# func(a=1)
# count = 0

# while count < 5:
#     print(count)
#     count += 1


# string1="Hello "
# string2=" Bindu"
# result=string1 + string2
# print(result)

# string1='Hello '
# string2=' Bindu'
# string1 +=string2
# print(string1)

# my_string = "Hello, World!"
# length = len(my_string)
# print(length)

# 1.Write a Python function that takes two parameters and returns their sum.

# def add(a,b):
#     return a + b
# print(add(1,5))


# 2.Create a function that takes a limit as a parameter and prints all even numbers from 1 to that limit.

# def even():
#     for i in range(0,int(input("Limit: ")),2):
#         print(i)
# even()

# 3.Write a function to calculate the factorial of a given number.


# def factorial(n):
#     ans = 1
#     for i in range(1,n+1):
#         ans = ans*i
#     return ans

# fiveFactorial = factorial(7)
# print(fiveFactorial)

# 4.Implement a function that takes a string as input and returns its reverse.

# word='string'
# reverse=word[::-1]
# print(reverse)

# word = "sampath"
# reversed = ''
# for char in word:
#     reversed = char + reversed
# print(reversed)

#  5.Write a program that prints the multiplication table (up to 10) for a given number using a function.


# def n_table(n):
#     for i in range(1,11):
#         print(n*i)

# num=int(input("enter any number n:"))

# n_table(num)

num = int(input("Enter a Number: "))
for i in range(2, int(num / 2) + 1):
    if num % i == 0:
        print(f"{num} is not a prime")
        break
else:
    print(f"{num} is a prime")
