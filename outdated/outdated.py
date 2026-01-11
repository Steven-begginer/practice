list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def convert(month, day, year):
        return (f"{year}-{int(month):02}-{int(day):02}")
def main():
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                month,day,year = date.split("/")
                if 1 <= int(day) <= 31 and 1<= int(month) <= 12:
                    print(convert(month,day,year))
                    break
                else:
                     print("reprompt the user again")
                     continue
            else:
            # Remove comma and split
                month,day,year = date.replace(","," ").split()
                if month in list:
                    month = list.index(month) + 1
                    if 1 <= int(day) <= 31 and 1<= int(month) <=12:
                            print(convert(month, day, year))
                            break
                    else:
                        print("repromt the user again")
                        continue
                else:
                     continue
        except ValueError:
            print("Invaid value")
            continue
main()