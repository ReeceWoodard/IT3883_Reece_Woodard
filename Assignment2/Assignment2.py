# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Reece Woodard
# Assignment Number: Lab2
# Due Date: 6/19/2026
# Purpose: Calculates the averages for a list of students grades and prints the results in descending order.

file_name = "input.txt"

students = []

# Reads each student's name and scores from the file
with open(file_name, "r") as file:
    for line in file:
        parts = line.strip().split()
        
        name = parts[0]
        
        scores = parts[1:]
        
        total = 0
        for score in scores:
            total += float(score)
        
        average = total / len(scores)
        
        students.append((name, average))

# Sorts students by average score from highest to lowest
students.sort(key=lambda student: student[1], reverse=True)

# Prints each student's name and score
for student in students:
    print(student[0], format(student[1], ".2f"))
