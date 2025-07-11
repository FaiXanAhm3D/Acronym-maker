s=[]
def isempty():
    if s==[]:
        print("stack is empty")
    else:
        display()

def display():
    if s==[]:
        print("Stack is empty")
    else:
        for i in s:
            print(i)
def push(element):
    s.append(element)

push(5)
push(6)
push(7)
display()
isempty()
s.pop()
display()

