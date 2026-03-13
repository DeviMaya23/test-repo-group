GRADE_MAPPING = [
    ("HD", 85),
    ("D", 75),
    ("C", 65),
    ("P", 50),
    ("F", 0)
]


def main():
    # Get total number of students
    total_student = 0
    while True:
        while True:
            try:
                total_student = int(input("How many students?\n"))
                break
            except ValueError:
                print("Input must be numerical.")
        if 3 <= total_student <= 10:
            break
        else:
            print("Invalid input (number must be between 3 and 10)")

    # Get all students information
    student_list = {}
    for i in range(total_student):
        while True:
            name = input(f"Student {i + 1} name: ").lower().strip()
            if not name.replace(" ", "").isalpha():
                print("Student name must be alpha characters "
                      "(space between names allowed).")
                continue

            name = name[0].upper() + name[1:]

            if name in student_list:
                print(f"Student {name} already exists.")
            else:
                break

        # Score input & validation
        while True:
            while True:
                try:
                    score = int(input(f"{name}'s score: "))
                    break
                except ValueError:
                    print("Score must be integer.")
            if 0 <= score <= 100:
                break
            print("Score must be between 0-100")

        student_list[name] = score

    # Print Result
    print("\nResults:")
    for name, score in student_list.items():
        for category, minimum in GRADE_MAPPING:
            if score >= minimum:
                score_category = category
                break
        print(f"{name}: {score} ({score_category})")

    # Get average
    score_list = list(student_list.values())
    print(f"\nAverage score: {sum(score_list)/total_student}")

    # Get minimum & maximum
    names_list = list(student_list.keys())
    min_score = min(score_list)
    max_score = max(score_list)

    min_names = []
    max_names = []
    for i, score in enumerate(score_list):
        if score == min_score:
            min_names.append(names_list[i])
        if score == max_score:
            max_names.append(names_list[i])

    print("Highest: ", end="")
    print(*max_names, sep=", ", end=" ")
    print(f"({max_score})")

    print("Lowest: ", end="")
    print(*min_names, sep=", ", end=" ")
    print(f"({min_score})")


main()
