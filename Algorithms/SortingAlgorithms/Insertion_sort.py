def insertion_sort(list):
    length=len(list)
    step=0
    for l in range(1,length):
        value=list[l]
        j=l-1
        while j>=0 and value<list[j]:
            if list[j]>value:
                list[j+1]=list[j]
            j-=1
        step+=1
        list[j+1]=value
        
        

    print("Steps:",step)
    return list




arrays=[[30,25,22,20,22,15],
        [1,2,3,4,5,6,7,8,9],
        [5,9,2,7,28,0,39,47],
        [],
        [1]
        ]

if __name__=="__main__":

    for array in arrays:
        print(insertion_sort(array))
        print("-"*30)






