def selection_sort(list):
    length=len(list)
    step=0
    for l in range(length-1):
        min_val_index=l
        for c in range(l,length):
            if list[min_val_index]>list[c]:
                min_val_index=c
        step+=1
        # if l <=min_val_index:
        list[l],list[min_val_index]=list[min_val_index],list[l]
        
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
        print(selection_sort(array))
        print("-"*30)




