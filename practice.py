# algorithm : linear search 
arr = [1,3,4,6,10,11,31]
guessed_value = int(input()) # loop 7 times, from 0,1,2,3,4,5,6
for i in range(len(arr)):
    if arr[i] == guessed_value:
        print("you find out the value")
        break
    elif arr[i] != guessed_value:
        if i < len(arr):
            print("you do not find out the value and continue to open the next box")
            if i == len(arr) -1:
                print("value not exist")
    
    
