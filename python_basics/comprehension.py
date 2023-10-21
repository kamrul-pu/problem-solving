numbers = [1, 2, 3, 4, 5, 6, 7]
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)

print(even)
# List comprehenssion
evens = [num for num in numbers if num % 2 == 0]
print(evens)

sq_numbers = [n * n for n in numbers]
print(sq_numbers)

# Set Comprehenssion
s = set([1, 2, 3, 4, 5, 2, 3])
print(s)

# Create even sets from set using set comprehenssion
even_set = {num for num in s if num % 2 == 0}
print(even_set)

# Dictionay Comprehension
cities = [
    "Chandpur",
    "Mumbai",
    "New York",
]
countries = [
    "Bangladesh",
    "India",
    "USA",
]

# Zip Function makes one list of tuples from the two list
# [(Chandpur, Bangladesh), (Mumbai, India),(New york,USA)]
z = list(zip(cities, countries))

# for a in z:
#     print(a)
print(z)
# Create a dictionary from the two list

d = {city: country for city, country in zip(cities, countries)}

# {'Chandpur': 'Bangladesh', 'Mumbai': 'India', 'New York': 'USA'}
print(d)

students = (
    1,
    2,
    3,
    4,
    5,
)
marks = (90, 89, 95, 99, 85)

# create a mark dictionary from the students and marks tuple
d = {student: mark for student, mark in zip(students, marks)}
print(d)
