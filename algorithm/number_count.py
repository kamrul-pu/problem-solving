count = {}

n = int(input())
nums = list(map(int, input().split(" ")))

for num in nums:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1

t = int(input())
while t:
    x = int(input())
    print(f"Count of {x} is: {count.get(x,0)}")
    t -= 1
