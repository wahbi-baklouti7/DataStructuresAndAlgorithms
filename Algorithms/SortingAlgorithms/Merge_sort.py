
def merge_sort(array):

    if len(array)<=1:
        return array
    
    mid=len(array)//2
    left=array[:mid]
    right=array[mid:]

    left_array=merge_sort(left)
    right_array=merge_sort(right)

    return merge_two_list(left_array,right_array)


def merge_two_list(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i=0
    j=0

    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i<len_a:
        sorted_list.append(a[i])
        i+=1

    while j<len_b:
        sorted_list.append(b[j])
        j+=1
    
    return sorted_list



arrays=[[5,6,7,4,8,2],
        [30,25,22,20,15],
        [1,2,3,4,5,6,7,8,9],
        [5,9,2,7,28,0,39,47],
        [1],
        []
        ]

if __name__=="__main__":

    for array in arrays:
        print(merge_sort(array))
        print("-"*30)

