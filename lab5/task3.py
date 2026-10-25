def display_report(students):
    for student in students:
        average = calculate_average(student["marks"])
        performance = classify_performance(average)

        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Average:", round(average, 2))
        print("Performance:", performance)
        print("--------------------")


students = [
    {"id": 1, "name": "Rahim", "marks": [80, 85, 90]},
    {"id": 2, "name": "Karim", "marks": [65, 70, 75]},
    {"id": 3, "name": "Nadia", "marks": [45, 50, 55]}
]

display_report(students)