'''
def bubble_sort (arr):
    length = len(arr)
    for i in range(length):
        for j in range (length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1], arr[j]

arr = [111, 2, 324, 546, 12, 3423,10,5]
bubble_sort(arr)
print(arr)
'''
'''
def merge_sort(arr):
    length = len(arr)
    if len==1:
        return arr

    middle = length//2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left_half, right_half)
'''
'''
arr = [13, 32, 535, 3242, 1231, 422,59]
def reverse(arr):
    dlina = len(arr)
    for i in range (dlina):
        for j in range (dlina):
            if reverse[0]<reverse[-1]:
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
            if reverse[0]>reverse[-1]:
                if arr[j]<arr[j+1]:
                    arr[j+1],arr[j]=arr[j],arr[j+1]
print(arr)
'''
'''
def linear_search (list, trigger):
    for i in range(len(list)):
        if list[i]==trigger:
            return i
'''
def binary_search(arr, trigger):
    low_border=0
    high_border = len(arr)-1

    while low_border<=high_border:
        middle = (low_border+high_border)//2
        if arr[middle]==trigger:
            return trigger
        elif arr[middle]>trigger:
            low_border=middle+1
        else:
            high_border = middle-1
    return -1

arr = [32,32,2,41,3,8,85,45]
print(binary_search(arr,85))