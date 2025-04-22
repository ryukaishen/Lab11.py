import os
import matplotlib.pyplot as plt

# helper functions
def load_students():
    students = {}
    with open("data/students.txt") as file:
        for line in file:
            parts = line.strip().split(",")
            name = parts[0]
            student_id = parts[1]
            students[student_id] = name
    return students

def load_assignments():
    assignments = {}
    with open("data/assignments.txt") as file:
        for line in file:
            parts = line.strip().split(",")
            name = parts[0]
            points = int(parts[1])
            assignment_id = parts[2]
            assignments[assignment_id] = (name, points)
    return assignments

def load_submissions():
    submissions = []
    with open("data/submissions.txt") as file:
        for line in file:
            parts = line.strip().split(",")
            student_id = parts[0]
            assignment_id = parts[1]
            percent = float(parts[2])
            submissions.append((student_id, assignment_id, percent))
    return submissions
# stuent grade
def student_grade():
    name = input("What is the student's name: ")
    students = load_students()
    assignments = load_assignments()
    submissions = load_submissions()

    student_id = None
    for sid, sname in students.items():
        if sname == name:
            student_id = sid
            break
    if student_id is None:
        print("Student not found")
        return

    total_score = 0
    for s in submissions:
        if s[0] == student_id:
            points_possible = assignments[s[1]][1]
            total_score += points_possible * (s[2] / 100)

    percentage = round((total_score / 1000) * 100)
    print(f"{percentage}%")
# stats
def assignment_stats():
    name = input("What is the assignment name: ")
    assignments = load_assignments()
    submissions = load_submissions()

    assignment_id = None
    for aid, (aname, _) in assignments.items():
        if aname == name:
            assignment_id = aid
            break
    if assignment_id is None:
        print("Assignment not found")
        return

    scores = [s[2] for s in submissions if s[1] == assignment_id]
    if scores:
        print(f"Min: {int(min(scores))}%")
        print(f"Avg: {int(sum(scores)/len(scores))}%")
        print(f"Max: {int(max(scores))}%")

# graphj
def assignment_graph():
    name = input("What is the assignment name: ")
    assignments = load_assignments()
    submissions = load_submissions()

    assignment_id = None
    for aid, (aname, _) in assignments.items():
        if aname == name:
            assignment_id = aid
            break
    if assignment_id is None:
        print("Assignment not found")
        return

    scores = [s[2] for s in submissions if s[1] == assignment_id]
    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(name)
    plt.xlabel("Score (%)")
    plt.ylabel("Number of Students")
    plt.show()
def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    choice = input("\nEnter your selection: ")

    if choice == "1":
        student_grade()
    elif choice == "2":
        assignment_stats()
    elif choice == "3":
        assignment_graph()

if __name__ == "__main__":
    main()
