# Overly Verbose GPA Calculator

Welcome to the Overly Verbose GPA Calculator! This program is a fun, interactive tool that helps you calculate your GPA in a very detailed (and slightly dramatic) way. It not only computes your overall GPA but also gives semester-level insights and suggests how to reach your goal GPA.

## Features

Calculate Overall GPA: Input your grades for all classes and get your current GPA.

Semester Analysis: Split your grades into first and second semester and see which semester is doing better.

Goal GPA Check: Enter your target GPA and see if you’ve already achieved it.

Improvement Suggestions: If your goal GPA isn’t met, the program will suggest which single grade improvements could help you reach your goal.

## How to Use

Run the program.

Enter the number of classes you are taking.

Enter each grade (on a 0.0 - 4.0 scale).

Choose which semester to analyze (1 for first semester, 2 for second semester).

Review your semester GPA compared to your overall GPA.

Enter your goal GPA. The program will tell you if you’ve reached it or which grades need improvement.

## Example Interaction

Welcome to the Overly Verbose GPA Calculator!
How many classes are you in? 4
Enter grade 1 (0.0 - 4.0): 3.5
Enter grade 2 (0.0 - 4.0): 4.0
Enter grade 3 (0.0 - 4.0): 3.0
Enter grade 4 (0.0 - 4.0): 3.8
Calculating... beep boop... Your current GPA is: 3.57

Enter 1 or 2: 1
Analyzing first semester...

First semester GPA: 3.75
Overall GPA: 3.57
Nice! Your first semester GPA is higher than your overall. You're trending upward!

What's your goal GPA? 3.8

Good news! You can reach your goal of 3.80 by improving just ONE grade:
- If you raise your grade in class 3 from 3.00 to 4.0, your GPA would be 3.82

## Requirements

###1. Create a grades list:

Make a list called grades with at least 5 grades on a 4.0 scale (e.g., 4.0, 3.3, 2.7).

You can either pre-fill it or ask the user to input the grades.

###2. Validate user input:

Grades must be numbers between 0.0 and 4.0.

If invalid input is entered (letters, negatives, or numbers above 4.0), show an error and ask again.

###3. Calculate overall GPA:

Sum all grades, count them, and divide the sum by the count.

Display the GPA with a fun or clear message.

###4. Analyze semester GPA (using list slicing):

Ask the user which semester to check (first half or second half of classes).

Slice the grades list to get that semester’s grades.

Calculate and display the semester GPA.

Compare it to the overall GPA and tell the user if it improved, declined, or stayed the same.

###5. Goal GPA analysis:

Ask for a goal GPA (must be between 0.0 and 4.0).

Check if the goal can be reached by improving only one grade to 4.0.

Tell the user which grade(s) could be improved to meet the goal, or if multiple improvements are needed.

Congratulate the user if the goal is already met.

## How It Works

The program first asks for the number of classes and the grades for each.

It calculates the overall GPA by averaging all grades.

Users choose which semester to analyze, and the program calculates semester GPA.

Users can set a goal GPA. The program checks if it’s achievable and suggests improvements if necessary.
