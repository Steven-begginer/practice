a = [7,5,3,1]
for i in range(len(a)-1): 
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i] # "=" can change the function label, "==" is the condition label.
        else:
            continue
print(a)



        
