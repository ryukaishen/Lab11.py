import os
import matplotlib.pyplot as plt

# file studentssss
def load_students():
    students = {}
    with open("data/students.txt") as file:
        for line in file:
            line = line.strip()
            if not line or not line[0].isdigit():
                continue
            i = 0
            while i < len(line) and line[i].isdigit():
                i += 1
            student_id = line[:i]
            student_name = line[i:].strip()
            if student_name and student_id:
                students[student_id] = student_name
    return students

# file assignmment
def load_assignments():
    assignments = {}
    with open("data/assignments.txt") as file:
        lines = [line.strip() for line in file if line.strip()]
        for i in range(0, len(lines), 3):
            try:
                name = lines[i]
                assignment_id = lines[i + 1]
                points = int(lines[i + 2])
                assignments[assignment_id] = (name, points)
            except (IndexError, ValueError):
                continue
    return assignments

# submissions
def load_submissions():
    submissions = []
    folder = "data/submissions"
    if not os.path.isdir(folder):
        return submissions

    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if not os.path.isfile(file_path):
            continue
        with open(file_path) as file:
            for line in file:
                line = line.strip().replace("|", ",")
                parts = line.split(",")
                if len(parts) != 3:
                    continue
                try:
                    student_id = parts[0].strip()
                    assignment_id = parts[1].strip()
                    percent_score = float(parts[2].strip())
                    submissions.append((student_id, assignment_id, percent_score))
                except ValueError:
                    continue
    return submissions

# grade grade grade
def student_grade():
    student_name = input("What is the student's name: ").strip().lower()
    students = load_students()
    assignments = load_assignments()
    submissions = load_submissions()

    found_ids = [student_id for student_id, name in students.items() if name.strip().lower() == student_name]

    if not found_ids:
        print("Student not found.")
        return

    found_id = found_ids[0]
    earned_points = 0
    possible_points = 0

    for assignment_id, (_, max_score) in assignments.items():
        matching_submissions = [entry for entry in submissions if entry[0] == found_id and entry[1] == assignment_id]
        if matching_submissions:
            earned_points += max_score * (matching_submissions[0][2] / 100)
        possible_points += max_score

    final_percentage = round((earned_points / possible_points) * 100)
    print(f"{final_percentage}%")

# sttatssss yasss
def assignment_stats():
    assignment_name = input("What is the assignment name: ").strip().lower()
    assignments = load_assignments()
    submissions = load_submissions()

    matching_ids = [aid for aid, (name, _) in assignments.items() if name.strip().lower() == assignment_name]

    if not matching_ids:
        print("Assignment not found.")
        return

    target_id = matching_ids[0]
    scores = [score for (sid, aid, score) in submissions if aid == target_id]
    if scores:
        print(f"Min: {int(min(scores))}%")
        print(f"Avg: {int(sum(scores)/len(scores))}%")
        print(f"Max: {int(max(scores))}%")

# graphpphphpia
def assignment_graph():
    assignment_name = input("What is the assignment name: ").strip().lower()
    assignments = load_assignments()
    submissions = load_submissions()

    matching_ids = [aid for aid, (name, _) in assignments.items() if name.strip().lower() == assignment_name]

    if not matching_ids:
        print("Assignment not found.")
        return

    target_id = matching_ids[0]
    scores = [score for (sid, aid, score) in submissions if aid == target_id]
    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(assignment_name.title())
    plt.xlabel("Score (%)")
    plt.ylabel("Number of Students")
    plt.show()

# menu
def main():
    print("\n1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    choice = input("\nEnter your selection: ").strip()

    if choice == "1":
        student_grade()
    elif choice == "2":
        assignment_stats()
    elif choice == "3":
        assignment_graph()
    else:
        print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
