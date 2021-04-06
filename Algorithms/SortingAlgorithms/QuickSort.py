
def partition(arr,l,h):
    i=l
    j=h
    pivot=arr[i]

    while i<j:

        while i<len(arr)-1 and  arr[i]<=pivot:
            i+=1
        
        while arr[j]>pivot:
            j-=1

        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[l],arr[j]=arr[j],arr[l]
    return j

def quick_sort(array):
    l=0
    h=len(array)-1
    
    return _quick_sort(array,l,h)

def _quick_sort(arr,low,high):

    
    if low<high:
        p=partition(arr,low,high)

        _quick_sort(arr,low,p)      # Left partition
        _quick_sort(arr,p+1,high)   # Right partition
    
    return arr
"""

def partition(arr,l,h):
    
    j=l
    i=j
    pivot=arr[h]

    while j<h:
        while j<h and arr[j]>pivot:
            j+=1
        arr[i+1],arr[j]=arr[j],arr[i+1]
        i+=1
        
    return i


def quick_sort(array):
    l=0
    h=len(array)-1

    return _quick_sort(array,l,h)


def _quick_sort(arr,l,h):

    if l<h:
        p=partition(arr,l,h)

        _quick_sort(arr,l,p-1)
        _quick_sort(arr,p+1,h)
    return arr

"""



arrays=[[30,25,22,20,15],
        [1,2,3,4,5,6,7,8,9],
        [5,9,2,7,28,0,39,47,1],
        [],
        [1]
        ]

if __name__=="__main__":

    for array in arrays:
        print(quick_sort(array))
        print("-"*30)