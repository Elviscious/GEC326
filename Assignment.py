def calculate_gpa():
    total_points = 0
    total_credit_units = 0

    for i in range(6):
        print(f"\nCourse {i+1}")
        grade = input("Enter grade (A, B, C, D, F): ").upper()
        credit_units = float(input("Enter credit units: "))

        # Convert grade to grade point
        grade_point = {
            'A': 5.0,
            'B': 4.0,
            'C': 3.0,
            'D': 2.0,
            'F': 0.0
        }.get(grade, None)

        if grade_point is None:
            print("Invalid grade entered. Please enter a valid grade (A, B, C, D, F).")
            return

        total_points += grade_point * credit_units
        total_credit_units += credit_units

    gpa = total_points / total_credit_units
    print(f"\nYour GPA is: {gpa:.2f}")

calculate_gpa()
