def search(arr, x): #O(n)
    for i in arr:
        if i ==x:
            return True
    return False


def binarySearch(arr, x): #O(log(n))
    #arr.sort()
    left = 0
    right = len(arr)-1
    while(left <= right):
        mid = (left+right)//2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            right = mid-1
        elif arr[mid] < x:
            left = mid+1
    return False


def binarySearchRecursive(arr, x, left ,right):

    while(left <= right):
        mid = (left+right)//2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binarySearchRecursive(arr,x,left,mid-1)
        elif arr[mid] < x:
            return binarySearchRecursive(arr,x, mid+1,right)

    return False



if __name__ == "__main__":
    arr = [10,20,30,40,50]
    #print(search(arr,20))
    print(binarySearch(arr,50))
    print(binarySearchRecursive(arr,50,0,len(arr)-1))





