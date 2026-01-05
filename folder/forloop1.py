arr = [1,2,3,4]
for i in range(len(arr)):
    for j in range(i+5, len(arr)):
        print(arr[j])
# looking for the result, we can see when the for loop has the maximal range or called stop, it can not exceed to the stop even if the start value is more than the stop value.