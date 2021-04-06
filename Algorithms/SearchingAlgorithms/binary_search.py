def binary_search(array,value):
    l=0
    h=len(array)-1
    if len(array)<=1:
        if array[0]==value:
            return True
        else:
            return False
    
    while l<=h:
        mid=(l+h)-l//2
        mid_value=array[mid]

        if mid_value==value:
            return True
        
        elif mid_value>value:
            h=mid-1

        elif mid_value<value:
            l=mid+1
    if l>h:
        return False




# print(binary_search([1,2,55,63,3,66,3,8,6,56,9],9))