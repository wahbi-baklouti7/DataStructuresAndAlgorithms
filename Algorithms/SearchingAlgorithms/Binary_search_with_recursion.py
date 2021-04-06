
def binary_recursion(array,value):
    l=0
    h=len(array)-1

    return _binary_recursion(array,l,h,value)

def _binary_recursion(arr,low,high,value):
    
    if low==high:
        if arr[low]==value:
            return True
        else:
            return False
    else:
        mid=(low+high)//2
        if arr[mid]==value:
            return True
        elif arr[mid]>value:
            return _binary_recursion(arr,low,mid-1,value)
        elif arr[mid]<value:
           return _binary_recursion(arr,mid+1,high,value)



# print(binary_recursion([1,2,5,6,7,10,19,26],25))