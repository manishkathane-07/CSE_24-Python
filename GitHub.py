def second_largest(arr):
    #your code goes here
    if len(arr)<2:
      return -1
    arr.sort(reverse=True)
    for x in range(1,len(arr)):
      if arr[x]!=arr[0]:
        return arr[x]
    return -1
    
n = int(input())
arr = list(map(int, input().split()))
print(second_largest(arr))



def reverse_array(arr):
  list.reverse(arr)
n = int(input())
arr = list(map(int, input().split()))

reverse_array(arr)

for x in arr:
    print(x, end=" ")



def find_missing(arr, n):
    #your coe goes here
    for x in range(1,n+1):
      if x not in arr:
        return x


n = int(input())
arr = list(map(int, input().split()))
print(find_missing(arr, n))
