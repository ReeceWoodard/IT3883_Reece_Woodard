# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Reece Woodard
# Assignment Number: Lab1
# Due Date: 6/12/2026
# Purpose: Script that displays string data that can be appended and cleared.


input_buffer = "" 
user_choice = ""

while user_choice != "4":
    print("Menu:")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "1":
        user_input = input("Enter a string to append: ")
        input_buffer = input_buffer + user_input

    elif user_choice == "2":
        input_buffer = ""
        print("Input buffer cleared.")

    elif user_choice == "3":
        print("Current input buffer:")
        print(input_buffer)

    elif user_choice == "4":
        print("Exiting program.")

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
