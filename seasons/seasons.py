from datetime import date # date is class. datetime is a library
import sys
import inflect
p = inflect.engine()


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    current_date = date.today()
    print(current_date)
    date_of_birth = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(date_of_birth)
    except ValueError:
        sys.exit("Invalid date")
    Duration = (current_date - birth_date).days
        # Check if birth date is a leap day (Feb 29)
    minutes = round(Duration * 24 * 60)
    print(minutes)
    print(p.number_to_words(minutes))
if __name__ == "__main__":
    main()