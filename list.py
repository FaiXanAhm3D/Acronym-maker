marks=[95,98,97]
for score in marks:
    print(score)
marks.append(99)
print("Inserting 99 at end",marks)
marks.insert(0,100)
print("Inseting 100 at first",marks)
print("Does 69 belongs to marks ?:",69 in marks)
print("Does 100 belongs to marks ?:",100 in marks)
print(len(marks))
print()
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print()
print(marks[2:])
print(marks[2:4])
print()
grace_marks=[22,25,27]
marks.extend(grace_marks)
print(marks)
marks.sort()
print(marks)
print()

a=0
while a<len(marks):
    print(marks[a])
    a=a+1

print()
more_numbers=[95,96,97,98,99]
print(more_numbers)
marks.extend(more_numbers)
print(marks)
print(marks.count(98))

print(marks.index(98))

marks.remove(98)
print(marks)

pop=marks.pop()
print(f"{pop} is popped from {marks}")

marks_copy=marks.copy()
marks.clear()
print(marks)
print(marks_copy)
