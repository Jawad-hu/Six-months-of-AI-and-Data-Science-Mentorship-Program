# A Function is block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# Functions can return data as a result.
# In Function is defined using the def keyword.

def greet_user ():
    print("Hello! , user")
# greet_user()

def aoa ():
    print ("Assalam o Alaikum!, All the way from london")
# aoa()

def aoa (name):
    print ("Assalam o Alaikum!, " + name)
# aoa("Jawad")

def aoa (name = "Khuda Ke Bnde "):
    print ("Assalam o Alaikum!, " + name, " Kese Ho Jan ")
# aoa("Jawad")

# Return Value from Function

def sqaure (number ):
    return number * number
# print (sqaure (5))

# Recursion Function
def factorial (n):
    if n ==1:
        return 1 
    else: 
        return n * factorial (n-1)
# print (factorial (6))


# Lamda Function

x = lambda a : a + 2
# print(x(5))

x = lambda a, b : a * b
print(x(5, 6))