import os

file_path = os.path.abspath("data_structure/nyc_weather.csv")
print("file path: ", file_path)

arr = []

with open(file_path, "r") as f:
    for line in f:
        tokens = line.split(",")
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")


print(arr)

# Calculate average temperate of first week of january
avg = sum(arr[0:7]) / len(arr[0:7])
print(avg)

# Maximum temparature in first 10 days

print(max(arr[0:10]))

# Excercise 2

weather_dict = {}

with open(file=file_path, mode="r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature. Ignore the row")

print(weather_dict)

# Temperature in january 4
print(weather_dict["Jan 9"])
print(weather_dict["Jan 4"])
