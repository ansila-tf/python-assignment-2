age_list = [24, 25, 26, 27, 28]
print(age_list)
name_list = ["anu", "ammu", "rahul", "arun", "meera"]
print(name_list)
name_list.append("Yazhini")
print(name_list)
age_list.insert(2, 30)
print(age_list)
name_list.remove("Yazhini")
print(name_list)
age_list.pop()
print(age_list)
age_list.extend([29, 30, 26])
print(age_list)
age_list.sort(reverse=True)
print(age_list)
print("maximum age:", max(age_list))
print("minimum age:", min(age_list))
print("sum of ages:", sum(age_list))
print(name_list[0])
print(name_list[-1])
print(name_list[::-1])
student_marks = {
    "anu": 85,
    "ammu": 90,
    "rahul": 75,
    "arun": 88,
    "meera": 95
}
print(student_marks)
print(student_marks["anu"])
student_marks["Janani"] = 80
print(student_marks)
student_marks["rahul"] = 82
print(student_marks)
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print(my_set)

#A set doesnot allow duplicate elements so repeated elements like'a' and 'i' are stored only once.
#also sets are unordered,so the output order may vary

#my_set[4] = 's'

#this code throws a typerror because sets do not support indexing or item
#assignment.we cannot modify set elements using an index

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}
print(set1)
print(set2)
print("union:", set1.union(set2))
print("intersection:", set1.intersection(set2))

score = int(input("enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("please enter a valid score between 0 and 10")

elif score > 7:
    print("above average: excellent performance! keep it up.")

elif score >= 4:
    print("average: good effort! keep practicing, there's room for improvement.")

else:
    print("below average: need to improve your performance, consistent practice will lead to better results.")



