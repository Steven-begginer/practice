a = [7,5,3,1]
for i in range(len(a)-1): 
    swap = False 
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i] # "=" can change the function label, "==" is the condition label.
            swap = True #no swap is false
        else:
            continue
    if swap == False: #no swap is True. we can use "if not swap:" instead of "if swap == False". The location is to jump out of internal loop.
        break

print(a)



        
