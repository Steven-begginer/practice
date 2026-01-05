arr = [7,5,3,1]
for i in range(len(arr)-1):
    analyzed_index = i
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j  # Changed == to =
    arr[analyzed_index], arr[min_index] = arr[min_index], arr[analyzed_index]
print(arr)

#min_index is variable, we set up variable which is aim to find out the correct value as result in the final. In this context, we set up the min_index with the purpose of finding out the minmial index.