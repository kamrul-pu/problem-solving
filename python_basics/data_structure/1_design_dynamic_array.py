# Dynamic Array implementation
# Note: Python lists are dynamic arrays by default,
# but this is an example of what's going on under the hood.


class DynamicArray:
    def __init__(self, capacity: int):
        """
        Initializes a dynamic array with a given capacity.

        Args:
            capacity (int): The initial capacity of the array.
        """
        self.capacity = capacity  # Capacity of the array
        self.length = 0  # Current number of elements in the array
        self.arr = [0] * self.capacity  # Internal array to store elements

    def get(self, i: int) -> int:
        """
        Get the element at index i.

        Args:
            i (int): Index of the element to retrieve.

        Returns:
            int: The element at the specified index.
        """
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        """
        Set the element at index i to the given value n.

        Args:
            i (int): Index of the element to set.
            n (int): Value to set at the specified index.
        """
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        """
        Append a new element to the end of the array.

        Args:
            n (int): The element to append to the array.
        """
        if self.length == self.capacity:
            self.resize()  # Resize the array if it's full

        # add the element in the last index and increase length
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        """
        Remove and return the last element of the array.

        Returns:
            int: The removed element from the end of the array.
        """
        if self.length > 0:
            self.length -= 1  # Decrement the length to remove the last element
        return self.arr[self.length]

    def resize(self) -> None:
        """
        Resize the array by doubling its capacity.
        """
        self.capacity = 2 * self.capacity  # Double the capacity
        new_arr = [0] * self.capacity  # Create a new array with the doubled capacity

        # Copy existing elements to the new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr  # Update the internal array reference to the new array

    def getSize(self) -> int:
        """
        Get the current number of elements in the array.

        Returns:
            int: The current number of elements in the array.
        """
        return self.length

    def getCapacity(self) -> int:
        """
        Get the current capacity of the array.

        Returns:
            int: The current capacity of the array.
        """
        return self.capacity


if __name__ == "__main__":
    # Initialize a DynamicArray with initial capacity of 1
    dynamic_array = None
    result = []

    # List of commands to execute
    commands = [
        "Array",
        1,
        "getSize",
        "getCapacity",
        "pushback",
        1,
        "getSize",
        "getCapacity",
        "pushback",
        2,
        "getSize",
        "getCapacity",
        "get",
        1,
        "set",
        1,
        3,
        "get",
        1,
        "popback",
        "getSize",
        "getCapacity",
    ]

    # Index to iterate through the commands
    index = 0

    # Iterate through each command
    while index < len(commands):
        command = commands[index]

        # If the command is a string, execute corresponding method of DynamicArray class
        if isinstance(command, str):
            if command == "Array":
                # Create a new DynamicArray instance with initial capacity specified in the next command
                capacity = commands[index + 1]
                dynamic_array = DynamicArray(capacity)
                index += 1  # Increment index to skip the capacity value
                result.append(None)
            elif command == "getSize":
                result.append(dynamic_array.getSize())
            elif command == "getCapacity":
                result.append(dynamic_array.getCapacity())
            elif command == "pushback":
                index += 1
                element = commands[index]
                dynamic_array.pushback(element)
                result.append(None)
            elif command == "popback":
                result.append(dynamic_array.popback())
            elif command == "get":
                index += 1
                i = commands[index]
                result.append(dynamic_array.get(i))
            elif command == "set":
                index += 1
                i = commands[index]
                index += 1
                value = commands[index]
                dynamic_array.set(i, value)
                result.append(None)
            else:
                print("Unknown command:", command)
        # If the command is an integer, ignore it
        else:
            continue

        index += 1

    print(result)
