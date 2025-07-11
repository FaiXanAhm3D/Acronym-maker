def duplicate(lst):
    main=[]
    
    for element in lst:
        for i in element:
            count=0
            for j in element:
                if i==j:
                    if i not in main:
                        main.append(i)
                    else:
                        continue
    print(main)

lst=[[1,2,3,3,34,4,5,5],[11,22,33,11,33],[1,1,2,2,3,3]]
duplicate(lst)
