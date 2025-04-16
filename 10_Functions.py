# A fuction is a block of code that only runs when it is called
# You pass data, known as parameters, into a function
# Function can return data as a result
# In Python a fuction is a defined using the def keyword 

# Lets define a function
def greet_user ():
    print ("Hello! , User")
    
greet_user()

def aoa():
    print ("Assalam o Alaikum, All the way from London")
aoa()

def aoa (name):
    print ("Assalam o Alaikum, ", name)
# aoa("Jawad")

def aoa (name = " Khuda ke Bande "):
    print ("Assalam o Alaikum, ", name , " Kese Ho Aap?")
aoa()

# Return Values 
def square (number): 
    return number * number
result = square(0)
print (square(9))

def square (number): 
    return number * number
print (square(9))

# Recursion

    