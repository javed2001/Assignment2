temp = [30, 30, 29, 30, 28, 33, 34]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

largest = temp[0]
day = ""
average = 30

for i in range(1, len(temp)):
    if temp[i] > largest:
        largest = temp[i]
        day = days[i]
    average += temp[i]

average /= len(days)

print("The highest temperature is:", largest)
print("The day is:", day)
print("The average is:", average)
