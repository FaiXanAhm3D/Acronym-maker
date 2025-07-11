# Ask the user to enter a list of numbers separated by space
input_string = input("Enter a list of numbers separated by space: ")

# Split the input string into a list of strings
list_of_string = input_string.split()

# Convert the list of strings into a list of integers
listn = [int(num) for num in list_of_string]

# Print the list of numbers
print("List of numbers:", listn)

s=len(listn)
if s%2 != 0:
    s=s-1
for i in range(0,s,2):
    print(i,i+1)
    listn[i],listn[i+1]=listn[i+1],listn[i]
print(listn)

