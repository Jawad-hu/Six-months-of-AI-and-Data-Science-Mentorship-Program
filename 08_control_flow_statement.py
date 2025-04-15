# # Conditional statements
#  # ==
#  # !=
# # >
# # <
x = -10 
if x > 0:
    print("x is positive")
    
elif x < 0: 
    print ("x is greater than 0 ")
    
else:
    print ("both are equal")
    
    
# # For Loop 

menu =["Dahi Bhally","Biryani","Chaat","Samosa", "Shami", "palak paneer"]

for food in menu:
    print(food)
    
# # While Loop

i = 1
while i < 100:
    print(i)
    i = i+1

for letters in "Python":
    if letters == "h":
        break
    print(letters)


for letters in "Python":
    if letters == "h":
        continue
    print(letters)
    
    
for letters in "Python":
    if letters == "h":
       pass
    print(letters)