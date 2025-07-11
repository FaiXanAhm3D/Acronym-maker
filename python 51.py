def Count3and7(N):
    lst=[]
    count=0
    for i in range(1,N+1):
        if i%3==0 or i%7==0:
            lst.append(i)
            count+=1
    print(f"between 1 and {N}, {lst} are the numbers which are divisible by 3 or 7")
    print(f"total count = {count}")

end=int(input("Enter the end limit: "))
Count3and7(end)
