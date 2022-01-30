"""
Given two array of integers of equal length, merge the arrays in the following manner. The new array will contain the 1st element of array1, then 1st element of array2, then 2nd element of array1, then 2nd element of array2 and so on.
Input-> [1,2,3],[10,20,30]
Output-> [1,10,2,20,3,30]
"""

list_1 = [1,2,3]
list_2 = [10,20,30]
len_1 = len(list_1)
len_2 = len(list_2)
new_arr = []
for i in range(0,len_1):
  e1 = list_1[i]
  new_arr += [e1]
  for j in range(0,len_2):
    e2 = list_2[j]
    if(i==j):
      new_arr += [e2]
print(new_arr)
