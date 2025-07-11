#nested loops

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

#exercise

number = [10,10,4,10,10,4,4,4]
for x_count in number:
    print('@'*x_count)
print("----")


number = [3,3,3,3,3,7,7]
for x_count in number:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
    
    


