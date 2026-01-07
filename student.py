# student_grade.py
# Program to calculate student grade

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def show_grade_criteria():
    print("=== Grade Criteria ===")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")

if __name__ == "__main__":
    import sys
    print("=== Student Grade Calculator ===")

    try:
        show_grade_criteria()

        if len(sys.argv) == 7:
            name = sys.argv[1]
            dept = sys.argv[2]
            sem = sys.argv[3]
            m1 = int(sys.argv[4])
            m2 = int(sys.argv[5])
            m3 = int(sys.argv[6])
        else:
            name = input("Enter Student Name: ")
            dept = input("Enter Department: ")
            sem = input("Enter Semester: ")
            m1 = int(input("Enter marks for Subject 1: "))
            m2 = int(input("Enter marks for Subject 2: "))
            m3 = int(input("Enter marks for Subject 3: "))

        print("\n=== Program Parameters ===")
        print(f"Name       : {name}")
        print(f"Department : {dept}")
        print(f"Semester   : {sem}")
        print(f"Subject 1  : {m1}")
        print(f"Subject 2  : {m2}")
        print(f"Subject 3  : {m3}")

        avg = calculate_average(m1, m2, m3)
        grade = calculate_grade(avg)

        print(f"\nAverage Marks = {avg:.2f}")
        print(f"Final Grade   = {grade}")

    except ValueError:
        print("Invalid input. Please enter correct numeric values for marks.")
