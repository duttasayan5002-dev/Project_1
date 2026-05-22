# Name: Sayan Dutta
# Project: Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures

# Function to calculate grade and comment
def calculate_grade(average):
    if average >= 90:
        return 'A', "Excellent! Keep up the great work!"
    elif average >= 80:
        return 'B', "Very Good! You're doing well."
    elif average >= 70:
        return 'C', "Good. Room for improvement."
    elif average >= 60:
        return 'D', "Needs Improvement. Study more."
    else:
        return 'F', "Failed. Please work harder."


# Function for colored grade display
def color_grade(grade):
    colors = {
        'A': '\033[92m',  # Green
        'B': '\033[94m',  # Blue
        'C': '\033[93m',  # Yellow
        'D': '\033[95m',  # Purple
        'F': '\033[91m'   # Red
    }
    reset = '\033[0m'
    return colors.get(grade, '') + grade + reset


# Function to validate marks
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100!")
        except ValueError:
            print("Invalid input! Enter numbers only.")


# Function to validate number of students
def get_valid_students():
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                return n
            else:
                print("Enter a positive number!")
        except ValueError:
            print("Invalid input! Enter a whole number.")


# Save results to file
def save_results(results):
    with open("results_sample.txt", "w") as file:
        file.write("STUDENT GRADE REPORT\n")
        file.write("=" * 60 + "\n")
        for student in results:
            file.write(
                f"{student['name']} | "
                f"Avg: {student['average']:.2f} | "
                f"Grade: {student['grade']} | "
                f"{student['comment']}\n"
            )
    print("Results saved to results_sample.txt")


# Search student by name
def search_student(results):
    name = input("Enter student name to search: ").lower()
    found = False

    for student in results:
        if student['name'].lower() == name:
            print("\nStudent Found!")
            print("-" * 40)
            print(f"Name   : {student['name']}")
            print(f"Average: {student['average']:.2f}")
            print(f"Grade  : {student['grade']}")
            print(f"Comment: {student['comment']}")
            found = True
            break

    if not found:
        print("Student not found!")


# Display statistics
def show_statistics(results):
    averages = [student['average'] for student in results]

    class_avg = sum(averages) / len(averages)
    highest = max(averages)
    lowest = min(averages)

    high_student = results[averages.index(highest)]['name']
    low_student = results[averages.index(lowest)]['name']

    print("\n" + "=" * 50)
    print("CLASS STATISTICS")
    print("=" * 50)
    print(f"Total Students : {len(results)}")
    print(f"Class Average  : {class_avg:.2f}")
    print(f"Highest Marks  : {highest:.2f} ({high_student})")
    print(f"Lowest Marks   : {lowest:.2f} ({low_student})")


# Main program
def main():
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)

    results = []
    num_students = get_valid_students()

    # Collect student data
    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")

        while True:
            name = input("Enter student name: ").strip()
            if name:
                break
            print("Name cannot be empty!")

        math = get_valid_marks("Math")
        science = get_valid_marks("Science")
        english = get_valid_marks("English")

        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)

        results.append({
            'name': name,
            'average': average,
            'grade': grade,
            'comment': comment
        })

    # Menu system
    while True:
        print("\n" + "=" * 50)
        print("MENU")
        print("=" * 50)
        print("1. Display All Results")
        print("2. Search Student")
        print("3. Show Statistics")
        print("4. Save Results")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            print("\n" + "=" * 70)
            print(f"{'Name':<20} {'Average':<10} {'Grade':<10} Comment")
            print("=" * 70)

            for student in results:
                print(
                    f"{student['name']:<20} "
                    f"{student['average']:<10.2f} "
                    f"{color_grade(student['grade']):<10} "
                    f"{student['comment']}"
                )

        elif choice == '2':
            search_student(results)

        elif choice == '3':
            show_statistics(results)

        elif choice == '4':
            save_results(results)

        elif choice == '5':
            print("\nThank you for using Grade Calculator!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()