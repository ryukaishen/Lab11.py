import os
import matplotlib.pyplot as plt

# Helper functions to load data from files
def load_students():
    students = {}
    with open("data/students.txt") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue
            name = parts[0].strip()
            student_id = parts[1].strip()
            if name and student_id:
                students[student_id] = name
    return students

def load_assignments():
    assignments = {}
    with open("data/assignments.txt") as file:
        lines = [line.strip() for line in file if line.strip()]
        for i in range(0, len(lines), 3):
            try:
                name = lines[i].strip()
                assignment_id = lines[i + 1].strip()
                points = int(lines[i + 2].strip())
                assignments[assignment_id] = (name, points)
            except (IndexError, ValueError):
                continue
    return assignments

def load_submissions():
    submissions = []
    submissions_folder = "data/submissions"
    if not os.path.isdir(submissions_folder):
        return submissions

    for filename in os.listdir(submissions_folder):
        file_path = os.path.join(submissions_folder, filename)
        if not os.path.isfile(file_path):
            continue
        with open(file_path) as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                try:
                    student_id = parts[0].strip()
                    assignment_id = parts[1].strip()
                    percent = float(parts[2].strip())
                    submissions.append((student_id, assignment_id, percent))
                except ValueError:
                    continue
    return submissions

# Menu option 1: Student grade
def student_grade():
    name = input("What is the student's name: ").strip()
    students = load_students()
    assignments = load_assignments()
    submissions = load_submissions()

    student_id = None
    for sid, sname in students.items():
        if sname.strip().lower() == name.strip().lower():
            student_id = sid
            break
    if student_id is None:
        print("Student not found. Valid names are:")
        for s in students.values():
            print(f"- {s}")
        return

    total_score = 0
    for s in submissions:
        if s[0] == student_id:
            if s[1] in assignments:
                points_possible = assignments[s[1]][1]
                total_score += points_possible * (s[2] / 100)

    percentage = round((total_score / 1000) * 100)
    print(f"{percentage}%")

# Menu option 2: Assignment statistics
def assignment_stats():
    name = input("What is the assignment name: ").strip()
    assignments = load_assignments()
    submissions = load_submissions()

    normalized_input = name.strip().lower()
    assignment_id = None
    for aid, (aname, _) in assignments.items():
        if aname.strip().lower() == normalized_input:
            assignment_id = aid
            break
    if assignment_id is None:
        print("Assignment not found. Valid assignments are:")
        for aname, _ in assignments.values():
            print(f"- {aname}")
        return

    scores = [s[2] for s in submissions if s[1] == assignment_id]
    if scores:
        print(f"Min: {int(min(scores))}%")
        print(f"Avg: {int(sum(scores)/len(scores))}%")
        print(f"Max: {int(max(scores))}%")

# Menu option 3: Assignment graph
def assignment_graph():
    name = input("What is the assignment name: ").strip()
    assignments = load_assignments()
    submissions = load_submissions()

    normalized_input = name.strip().lower()
    assignment_id = None
    for aid, (aname, _) in assignments.items():
        if aname.strip().lower() == normalized_input:
            assignment_id = aid
            break
    if assignment_id is None:
        print("Assignment not found. Valid assignments are:")
        for aname, _ in assignments.values():
            print(f"- {aname}")
        return

    scores = [s[2] for s in submissions if s[1] == assignment_id]
    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(name)
    plt.xlabel("Score (%)")
    plt.ylabel("Number of Students")
    plt.show()

def main():
    while True:
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
