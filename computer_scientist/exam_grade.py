def result(marks):
    if marks >= 75:
        return "Grade: First"
    elif marks >= 70 and marks < 75:
        return "Grade: Upper Second"
    elif marks >= 60 and marks < 70:
        return "Grade: Second"
    elif marks >= 50 and marks < 60:
        return "Grade: Third"
    elif marks >= 45 and marks < 50:
        return "Grade: F1 Supp"
    elif marks >= 40 and marks < 45:
        return "Grade: F2"
    elif marks < 40:
        return "Grade: F3"


count = 1
all_results = sorted([83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 49.9, 2, 0], reverse=True)
print(all_results)
print("# Result")
for i in all_results:
    grade = result(i)
    print(str(count) + ")",grade)
    count += 1
