#function to read lines from a text file and display the lines starting with the alphabet T
def Disp_Lines():
    with open("notes.txt",'r') as file:
        data=file.readlines()
        for i in data:
            if i[0]=='T':
                print(i)
            else:
                continue
Disp_Lines()
            
