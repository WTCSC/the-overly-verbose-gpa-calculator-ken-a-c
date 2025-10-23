#The Overly Verbose Calculator

print("Welcome to the Overly Verbose GPA Calculator!")

def put_in_classes():
    classes = int(input("How many classes are you in? "))
    print(f"You are in {classes} classes.")
    return classes

def enter_grades(num_classes):
    grades = []
    for i in range(num_classes):
        grade = float(input(f"Enter grade {i+1} (0.0 - 4.0): "))
        grades.append(grade)
    return grades

# ---- Main Program ----
num_classes = put_in_classes()
grades = enter_grades(num_classes)

overall_gpa = sum(grades) / len(grades)
print(f"Calculating... beep boop... Your current GPA is: {overall_gpa:.2f}")

half = num_classes // 2

while True:
    analyze = input("Enter 1 or 2: ").strip()
    if analyze == "1":
        print("Analyzing first semester...")
        break
    elif analyze == "2":
        print("Analyzing second semester...")
        break
    else:
        print("Invalid input. Please enter 1 or 2.")
