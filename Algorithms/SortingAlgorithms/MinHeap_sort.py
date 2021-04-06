
def minheap(arr,n,parent_index):
    smallest_index=parent_index
    left_index=2*parent_index+1
    right_index=2*parent_index+2

    if left_index<n and arr[left_index]<arr[smallest_index]:
        smallest_index=left_index
    if right_index<n and arr[right_index]<arr[smallest_index]:
        smallest_index=right_index
    if smallest_index!=parent_index:
        arr[smallest_index],arr[parent_index]=arr[parent_index],arr[smallest_index]
        minheap(arr,n,parent_index)


def minheap_sort(array):
    length=len(array)

    for n in range(length//2-1,-1,-1):
        minheap(array,length,n)
    
    for j in range(length-1,0,-1):
        array[0],array[j]=array[j],array[0]
        minheap(array,j,0)
    return array


arrays=[[5,6,7,4,8,2],
        [30,25,22,20,15],
        [1,2,3,4,5,6,7,8,9],
        [5,9,2,7,28,0,39,47],
        [1],
        []
        ]

if __name__=="__main__":

    for array in arrays:
        print(minheap_sort(array))
        print("-"*30)