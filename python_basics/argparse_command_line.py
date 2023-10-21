"""How to process command line"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Positional Argument and optional arguments
    # Positional Argument are mandatory
    # In terminal: python filename.py 4 5 add
    # parser.add_argument("number1", help="First Number")
    # parser.add_argument("number2", help="Second Number")
    # parser.add_argument("operation", help="Operation")

    # Option argument [it may be optional]
    # Execution System python filename.py --number1 4 --number2 5 --operation add
    parser.add_argument("--number1", help="First Number")
    parser.add_argument("--number2", help="Second Number")
    parser.add_argument(
        "--operation",
        help="Operation",
        choices=[
            "add",
            "subtract",
            "multiply",
            "division",
        ],
    )

    args = parser.parse_args()
    # print(args.number1)
    # print(args.number2)
    # print(args.operation)
    num1 = int(args.number1)
    num2 = int(args.number2)
    operation = args.operation
    # if operation == "add":
    #     print(num1 + num2)
    # elif operation == "subtract":
    #     print(num1 - num2)
    # elif operation == "multiply":
    #     print(num1 * num2)
    # elif operation == "division":
    #     print(num1 / num2)
    # else:
    #     raise Exception("Invalid Operation")

    # Using match
    result = None
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "division":
            result = num1 / num2
        # case _:
        #     raise Exception("Invalid Operation")
        case _:
            result = None

    print(result)
