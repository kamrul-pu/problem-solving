"""Else in for loop."""

if __name__ == "__main__":
    for i in range(1, 4):
        print(i)
    else:  # Executed because no break in for
        print("No Break")

    for i in range(1, 4):
        print(i)
        break
    else:  # Not executed as there is a break
        print("No Break")
