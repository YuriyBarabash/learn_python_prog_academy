# Task 1
import string
def most_common_words(filepath, number_of_words=3):
    word_with_count = {}
    lst_max = []
    dict_max = {}
    with open(filepath) as file:
        for line in file:
            for i in string.punctuation:
                line = line.replace(i, ' ')
            line = line.split()
            for i in line:
                count = line.count(i)
                if i in word_with_count:
                    word_with_count[i] += count
                else:
                    word_with_count[i] = count
        lst = list(word_with_count.values())
        for _ in range(number_of_words):
            lst_max.append(max(lst))
            lst.remove(max(lst))
        for x, y in word_with_count.items():
            if y in lst_max:
                dict_max[x] = y
    return dict_max

print(most_common_words('lorem_ipsum.txt', ))

# Task 2
import csv
def get_top_performers(file_path, number_of_top_students=5):
    students_dict = {}
    lst_max_points = []
    dict_best_students = {}
    with open(file_path, newline='') as csvfile:
        students = csv.reader(csvfile) #, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for line in students:
            line = str(line[0]).split(';')
            name, _, points = line
            points = float(points)
            students_dict[name] = points
        lst = list(students_dict.values())
        for _ in range(number_of_top_students):
            lst_max_points.append(max(lst))
            lst.remove(max(lst))
        for x, y in students_dict.items():
            if y in lst_max_points:
                dict_best_students[x] = y
    return list(dict_best_students.keys())

print(get_top_performers("students.csv", 2))





