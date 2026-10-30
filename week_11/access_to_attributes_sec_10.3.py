class Student:
    # CLASS ATTRIBUTES: Shared by EVERY student object created from this class
    university_name = "State University"
    total_students = 0

    def __init__(self, name, major):
        # INSTANCE ATTRIBUTES: Unique to each individual student object
        self.name = name
        self.major = major
        
        # Increment the shared class attribute whenever a new student is born
        Student.total_students += 1

    def __repr__(self):
        return f"Student(Name: '{self.name}', Major: '{self.major}', University: {Student.university_name})"


# --- Video Demo Walkthrough ---

print(f"Total students before enrollment: {Student.total_students}")

# 1. Enrolling individual students (creating instances)
student1 = Student("Alice", "Computer Science")
student2 = Student("Marcus", "Data Science")

# 2. Inspecting unique instance attributes
print(f"\nStudent 1 Name & Major: {student1.name}, {student1.major}")
print(f"Student 2 Name & Major: {student2.name}, {student2.major}")

# 3. Accessing the shared class attribute via the class name and via instances
print(f"\nUniversity (via class): {Student.university_name}")
print(f"University (via student1 instance): {student1.university_name}")

# 4. Checking the global class attribute tracker
print(f"Total students enrolled: {Student.total_students}")