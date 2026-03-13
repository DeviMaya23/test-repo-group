GRADE_MAPPING = [
    ("HD", 85),
    ("D", 75),
    ("C", 65),
    ("P", 50),
    ("F", 0)
]


def main():
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

    student_list = []
    for i in range(total_student):
        name = input(f"Student {i + 1} name: ")

        while True:
            while True:
                try:
                    score = int(input(f"{name}'s score: "))
                    break
                except ValueError:
                    print("Score must be integer.")

            if 0 <= score <= 100:
                for category, minimum in GRADE_MAPPING:
                    if score >= minimum:
                        score_category = category
                        break
                break
            print("Score must be between 0-100")

        student_list.append({
            "name": name,
            "score": score,
            "score_category": score_category
        })

    print("\nResults:")
    for student in student_list:
        name = student["name"]
        first_letter = name[0].upper()
        new_name = first_letter + name[1:]
        print(f"{new_name}: {student["score"]} ({student["score_category"]})")


main()
