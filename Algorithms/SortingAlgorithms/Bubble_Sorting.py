
def bubble_sort(arr):

    length=len(arr)
    # If the length less or equal than 1
    if length<=1:
        return arr
    else:
        step=0
        for l in range(length-1):
            is_swapped=False
            for c in range(length-1-l):
                if arr[c]>arr[c+1]:
                    arr[c],arr[c+1]=arr[c+1],arr[c]
                    is_swapped=True
                step+=1
            if not is_swapped:
                break
        print("Steps take:",step)
        return arr







arrays=[[30,25,22,20,22,15],
        [1,2,3,4,5,6,7,8,9],
        [5,9,2,7,28,0,39,47],
        [],
        [1]
        ]

if __name__=="__main__":

    for array in arrays:
        print(bubble_sort(array))
        print("-"*30)


