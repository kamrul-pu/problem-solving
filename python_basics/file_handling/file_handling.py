# """File Handling in Python."""
# import os

# if __name__ == "__main__":
#     # get the current script's directory
#     script_dir = os.path.dirname(os.path.realpath(__file__))
#     # combine with the file name to get the full path
#     file_path = os.path.join(script_dir, "sample.txt")
#     print("file path", file_path)
#     file = open(file_path, "r")
#     # This will print every line one by one in the file.
#     # for each in file:
#     #     print(each)

#     # read mode will read every thing
#     # print(file.read())
#     # Python code to illustrate with()

#     # with open(file_path, "r") as file:
#     #     data = file.read()
#     # print(data)

#     with open(file_path, "r") as file:
#         data = file.readlines()
#     # print(data)
#     for line in data:
#         word = line.split()
#         print(word)

#     # Create a file
#     file_path = os.path.join(script_dir, "test.txt")
#     file = open(file_path, "w")
#     file.write("THis is the write command")
#     file.write("It allows us to write in a particular file")
#     file.close()

#     # Python code to illustrate with() alongwith write()
#     file_path = os.path.join(script_dir, "file.txt")
#     with open(file_path, "w") as f:
#         f.write("Hello World!!!")

#     # Python code to illustrate append() mode
#     file = open(file_path, "a")
#     file.write("This will add this line")
#     file.close()


import os


def create_file(filename):
    try:
        with open(filename, "w") as f:
            f.write("Hello, world!\n")
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)


def read_file(filename):
    try:
        with open(filename, "r") as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)


def append_file(filename, text):
    try:
        with open(filename, "a") as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)


def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == "__main__":
    filename = "example.txt"
    new_filename = "new_example.txt"
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # combine with the file name to get the full path
    file_path = os.path.join(script_dir, filename)
    new_file_path = os.path.join(script_dir, new_filename)

    create_file(file_path)
    read_file(file_path)
    append_file(file_path, "This is some additional text.\n")
    read_file(file_path)
    rename_file(file_path, new_file_path)
    read_file(new_file_path)
    delete_file(new_file_path)
