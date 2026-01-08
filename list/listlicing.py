"""
#please input the last 4 digits to verify the final results,

def verify(digits):
    if digits == "7745":
        return ("successfully login!")
    else:
        return ("fail! please try again!")
    
def main():
    phone_number = input("")
    digits = phone_number[len(phone_number) - 4:len(phone_number)] # here i use the list licing to leave last four digits of string.
    #the lowerbound is for index, the upperbound is for the limits of string which is like for loop.
    print(verify(digits))

if __name__ == "__main__":
    main()
"""
#here is another situation for list slicing.
x = "123456789"
print(x[-4:]) # it is from the last one to the last four location.