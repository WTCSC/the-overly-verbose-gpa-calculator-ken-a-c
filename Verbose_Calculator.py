#The Overly 

print ("Welcome to the Overly Verbose GPA Calculator!")

def put_in_classes(classes):
    print(f"How many classes are you in? {classes}")

def Enter_Grade(Grade):
    v = []

    v.append(int(input("Enter grade 1 (0.0-4.0):")))
    v.append(int(input("Enter grade 2 (0.0-4.0):")))
    v.append(int(input("Enter grade 3 (0.0-4.0):")))
    v.append(int(input("Enter grade 4 (0.0-4.0):")))
    v.append(int(input("Enter grade 5 (0.0-4.0):")))
    v.append(int(input("Enter grade 6 (0.0-4.0):")))
    

    return v


print ("Calculating... beep boop... Your current GPA is: 3.30")

Which semester do you want to analyze?
1. First semester (first half of classes)
2. Second semester (second half of classes)
Enter 1 or 2: 2

Second semester GPA: 3.43
Overall GPA: 3.30
Nice! Your second semester GPA is higher than your overall. You're trending upward!

What's your goal GPA? 3.5

Good news! You can reach your goal of 3.5 by improving just ONE grade:
- If you raise your grade in class 3 from 2.8 to 4.0, your GPA would be 3.50
- If you raise your grade in class 5 from 3.0 to 4.0, your GPA would be 3.40

Time to hit the books!