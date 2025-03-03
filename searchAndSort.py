def bubble_sort(li):
    n = len(li)
    for l in range(0,n-1):    
        for i in range(0,n-1):
            if li[ i ] > li[i+1]:
                li[i+1] , li[i]=li[i], li [ i+1 ]
            else:
                pass
    return li
def seletion_sort(l):
    n = len(l)
    for i in range(0,n-1):
        initial = i
        for j in range(i+1, n):
            if l[j]<l[initial]:
                initial = j
        if initial != i:
            l[i],l[initial] = l[initial] , l[i]
    return l 

def insertion_sort(l):
    n = len(l)
    for i in range(1,n):
        item =l[i]
        j = i-1
        while j>=0 and l[j] > item:
            l[j+1] = l[j]
            j-=1
            l[j+1] = item
    return l 
            
def linear_search(l,x):
    n= len(l)
    i= 0 
    while i<n:
        if l[i] == x:
            return i
        i+=1
    i = -1
    return i
def binary_search(l , x):
    left , right = 0 , len(l)-1
    while left<=right:
        mid = (left+right)//2
        if l[mid] == x :
            return mid
        if l[mid] <x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
           



numbers = [32, 79, 4, 65, 95, 68, 67, 49, 65, 32, 78, 55, 67, 71, 63, 20, 82, 81, 11, 20, 46, 45, 2, 21, 68, 43, 2, 54, 29, 90, 14, 91, 45, 22, 25, 44, 91, 86, 14, 24, 36, 81, 71, 72, 20, 85, 70, 99, 94, 94, 99, 93, 9, 0, 32, 74, 35, 78, 79, 63, 7, 88, 9, 67, 53, 95, 68, 16, 42, 81, 69, 47, 36, 80, 41, 42, 7, 56, 50, 94, 54, 86, 42, 95, 68, 13, 40, 55, 29, 85, 66, 9, 77, 12, 16, 2, 42, 38, 5, 85]
numbers=insertion_sort(numbers)
index = linear_search(numbers , 68)
print(index)