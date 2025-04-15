#Grade Calculation 
# Get input from the user for marks in each subject
subject1 = float(input("Enter marks obtained in Subject 1: "))
subject2 = float(input("Enter marks obtained in Subject 2: "))
subject3 = float(input("Enter marks obtained in Subject 3: "))

# Calculate total marks and percentage
total_marks = subject1 + subject2 + subject3
percentage = (total_marks / (3 * 100)) * 100

# Assign grade based on percentage
if percentage >= 80:
    grade = 'A'
elif 70 <= percentage < 80:
    grade = 'B'
elif 60 <= percentage < 70:
    grade = 'C'
elif 40 <= percentage < 60:
    grade = 'D'
else:
    grade = 'E'

# Display the results
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
