import os
import matplotlib.pyplot as plt

# data files
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
            name = line[i:].strip()
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
                line = line.strip().replace("|", ",")  # allow pipe as separator
                parts = line.split(",")
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
# yasss grade
def student_grade():
    name_input = input("What is the student's name: ").strip().lower()
    students = load_students()
    assignments = load_assignments()
    submissions = load_submissions()



    matching_id = None
    for sid, sname in students.items():
        if sname.strip().lower() == name_input:
            matching_id = sid
            break

    if matching_id is None:
        print("Student not found.")
        return

    total_score = 0
    total_possible = 0

    for assignment_id, (_, points) in assignments.items():
        found = False
        for s in submissions:
            if s[0] == matching_id and s[1] == assignment_id:
                total_score += points * (s[2] / 100)
                found = True
                break
        if not found:
            total_score += 0
        total_possible += points

    percentage = round((total_score / total_possible) * 100)
    print(f"{percentage}%")





# stats
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
        print("Assignment not found.")
        return

    scores = [s[2] for s in submissions if s[1] == assignment_id]
    if scores:
        print(f"Min: {int(min(scores))}%")
        print(f"Avg: {int(sum(scores)/len(scores))}%")
        print(f"Max: {int(max(scores))}%")

# graph
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
        print("Assignment not found.")
        return






    scores = [s[2] for s in submissions if s[1] == assignment_id]
    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(name)
    plt.xlabel("Score (%)")
    plt.ylabel("Number of Students")
    plt.show()
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
