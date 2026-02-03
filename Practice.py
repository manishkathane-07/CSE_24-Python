#-----------------------------------------------------Q1--------------------------------------
# Construct a program to create the following array using Numpy arr ([[1, 2, 3], [4, 5, 6]])

import numpy as np
A = np.zeros((2,3), dtype=int)
for i in range(2):
    for j in range(3):
        A[i][j] = int(input("Enter element of [%d][%d] "%(i,j)))
print(A)

# Perform the following operations on the array using Numpy features.
# a) Print the number of dimensions of the array
print(A.ndim)
# b) Print the shape of the array
print(A.shape)
# c) Print the size of the array
print(A.size)
# d) Print the type of elements in the array
print(A.dtype)

# ----------------------------------------------------Q2-----------------------------------------
# An election is contested by five candidates. The candidates are numbered 1 to 5 and the voting is done by marking the candidate number on the ballot paper. Construct a system to read the ballots and count the 2 votes cast for each candidate using an array variable count. In case the number read is outside the range 1 to 5, the ballot should be considered as "Soilt Ballot" and the program should also count the number of Spoilt Ballots.

import numpy as np

votes = np.array(list(map(int, input("Enter votes: ").split())))

count = np.zeros(5, dtype=int)
spoilt = 0

for vote in votes:
    if 1 <= vote <= 5:
        count[vote-1] += 1
    else:
        spoilt += 1

print("Votes:", count)
print("Spoilt Ballots:", spoilt)


# ----------------------------------------------------Q3-----------------------------------------
#Develop an application with the following details:
# a) Consider an integer array, the number of elements and their values are determined by the user.
import numpy as np
r=int(input("Number of rows: "))
c=int(input("Number of coloums: "))
M= np.zeros((r,c), dtype=int)
for i in range(r):
    for j in range(c):
        M[i][j] = int(input("Enter element of [%d][%d] "%(i,j)))
print(M)
# b) Application should be able to find those pair of elements that has the maximum and minimum difference among all element pairs


n = int(input("Enter number of elements: "))


arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))


min_diff = abs(arr[0] - arr[1])
max_diff = abs(arr[0] - arr[1])

min_pair = (arr[0], arr[1])
max_pair = (arr[0], arr[1])


for i in range(n):
    for j in range(i + 1, n):
        diff = abs(arr[i] - arr[j])

        if diff < min_diff:
            min_diff = diff
            min_pair = (arr[i], arr[j])

        if diff > max_diff:
            max_diff = diff
            max_pair = (arr[i], arr[j])

print("Pair with minimum difference:", min_pair, "Difference =", min_diff)
print("Pair with maximum difference:", max_pair, "Difference =", max_diff)

# ----------------------------------------------------Q4-----------------------------------------
# Write a NumPy program to find the set difference between two arrays. The set difference will return sorted, distinct values in arrayl that are not in array2.
# Expected Output:
# Arrayl: [0 10 20 40 60 80]
# Array2: [10, 30, 40, 50, 70, 90]
# Set difference between two arrays:
# [0 20 60 80]

import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])
set_diff = []
for element in array1:
    if element not in array2:
        set_diff.append(element)
set_diff = np.array(set_diff)
print('set difference between two arrays:', set_diff)

# ----------------------------------------------------Q5-----------------------------------------
# Develop a program which takes 10 integer inputs from user and store them in an array. Now, copy all the elements in another array but in reverse order..
arr = []
print("Enter 10 numbers: ")
for i in range(10):
    arr.append(int(input()))
rev = arr[::-1]
print("original array:", arr)
print("Reverse :", rev)