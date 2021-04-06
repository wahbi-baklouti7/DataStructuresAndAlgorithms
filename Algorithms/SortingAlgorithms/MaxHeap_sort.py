

def maxheap(arr,n,parent_index):
    large_ind=parent_index
    left_index=2*parent_index+1
    right_index=2*parent_index+2

    if left_index<n and arr[left_index]>arr[large_ind]:
        large_ind=left_index
    if right_index<n and arr[right_index]>arr[large_ind]:
        large_ind=right_index
    
    if large_ind!=parent_index:
        arr[large_ind],arr[parent_index]=arr[parent_index],arr[large_ind]
        maxheap(arr,n,large_ind)
    







def maxheap_sort(arr):
    length=len(arr)

    for i in range(length//2-1,-1,-1):
        maxheap(arr,length,i)
    for j in range(length-1,0,-1):
        arr[j],arr[0]=arr[0],arr[j]
        maxheap(arr,j,0)
    return arr




arrays=[[5,6,7,4,8,2],
        [30,25,22,20,15],
        [1,2,3,4,5,6,7,8,9],
        [5,9,2,7,28,0,39,47],
        [1],
        []
        ]

if __name__=="__main__":

    for array in arrays:
        print(maxheap_sort(array))
        print("-"*30)