classes_held = int(input("Enter the number of classes held = "))
classes_attended = int(input("Enter the number of classes attended = "))
attendance_percentage = (classes_attended / classes_held) * 100
print(f"Attendance percentage = {attendance_percentage}%")
if attendance_percentage >= 75:
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")
