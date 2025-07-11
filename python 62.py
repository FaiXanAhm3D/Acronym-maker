def rotate(lst):
    end=lst[-1]
    length=len(lst)
    for i in range(length-1,0,-1):
        print(i)
        print(lst)
        lst[i]=lst[i-1]
    lst[0]=end
    print(lst)

lst=[1,2,3,4,5,6,7]
rotate(lst)
