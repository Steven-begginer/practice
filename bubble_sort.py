arr = [7,5,3,1]
for i in range(len(arr)-1): 
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i] # "=" can change the function label, "==" is the condition label.
        else:
            continue
print(arr)



        
