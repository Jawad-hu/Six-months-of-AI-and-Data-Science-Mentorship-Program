# Nested for Loop

colors = ['red', 'green', 'blue']
items = ["book", "pen", "copy"]

for color in colors:
    for item in items:
        print(item,color)

# Nested while Loop 
i = 0
while i < 3:
    j = 0 
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    
# for loop inside while loop

i = 1 
while i < 4: 
    for j in range (3):
        print(i,j)
        i +=1