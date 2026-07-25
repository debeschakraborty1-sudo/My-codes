# Python Program to Process Student Records using File Handling


with open("students.txt", "w") as file:
    file.writelines([
        "101,Arjun,85\n",
        "102,Ravi,72\n",
        "103,Priya,91\n",
        "104,Meena,65\n"
    ])
print("Reading first record using readline():")
with open("students.txt", "r") as file:
    first_line = file.readline()
    print(first_line)
    file.seek(0)
    records = file.readlines()
total_marks = 0
count = 0
result_data = []
for record in records:
    rollno, name, marks = record.strip().split(",")

    marks = int(marks)
    total_marks += marks
    count += 1
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"
    result_data.append(f"{rollno} - Grade: {grade}\n")
average = total_marks / count
print("Average Marks =", average)
with open("results.txt", "w") as result_file:
    result_file.write("Student Grades\n")
    result_file.write("-----------------\n")
    result_file.writelines(result_data)
print("\nContents of results.txt:")
with open("results.txt", "r") as file:
    print(file.read())
