class stu_manager:
    def __init__(self):
        self.student = {}

    def addStudent(self, rollno, studentname, marks):
        if rollno in self.student:
            print(f"{rollno} already exists")
        else:
            self.student[rollno] = {"name": studentname, "marks": marks}
            print(f"{rollno} for {studentname} has been added")

    def getstudent(self, rollno):
        if rollno in self.student:
            return self.student[rollno]
        else:
            return f"No student with rollno {rollno}"

    def gettopstudent(self, criteria):
        topstudent = [
            {"rollno": rollno, "name": data["name"], "marks": data["marks"]}
            for rollno, data in self.student.items()
            if data["marks"] > criteria
        ]
        return topstudent


# Object creation
result = stu_manager()

# List of student dictionaries
students_data = [
    {"rollno": 117, "studentname": "dhivya", "marks": 98},
    {"rollno": 119, "studentname": "kavin", "marks": 76},
    {"rollno": 153, "studentname": "anna", "marks": 87},
    {"rollno": 154, "studentname": "john", "marks": 69}
]

# Add students to the manager
for student in students_data:
    result.addStudent(student["rollno"], student["studentname"], student["marks"])

# Get student by roll number
print(result.getstudent(119))

# Optional: get top students with marks > 80
print("Top Students:\n", result.gettopstudent(80))
