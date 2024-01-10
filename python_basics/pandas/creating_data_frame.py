"""Creating Dataframe using pandas."""
import os
import pandas as pd

if __name__ == "__main__":
    # list of strings
    lst = ["Geeks", "For", "Geeks", "is", "portal", "for", "Geeks"]

    df = pd.DataFrame(lst)
    # print(df)
    # print(df.describe())
    # intialise data of lists.
    data = {"Name": ["Tom", "nick", "krish", "jack"], "Age": [20, 21, 19, 18]}
    df = pd.DataFrame(data)
    print(df)
    print(df.describe())
    # Define a dictionary containing employee data
    data = {
        "Name": ["Jai", "Princi", "Gaurav", "Anuj"],
        "Age": [27, 24, 22, 32],
        "Address": ["Delhi", "Kanpur", "Allahabad", "Kannauj"],
        "Qualification": ["Msc", "MA", "MCA", "Phd"],
    }
    # Convert the dictionary in data frame
    df = pd.DataFrame(data)

    # Select two columns
    print(df[["Name", "Qualification"]])
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # combine with the file name to get the full path
    file_path = os.path.join(script_dir, "nba.csv")
    # Making data frame from csv file
    data = pd.read_csv(file_path, index_col="Name")
    # Selecting a row
    first = data.loc["Avery Bradley"]
    second = data.loc["R.J. Hunter"]
    print(first, "\n\n\n", second)
    print(data.describe())
    # retrieving columns by indexing operator
    first = data["Age"]
    print(first)
    second = data[["Age", "College"]]
    print(second)

    # retrieving rows by iloc method
    row2 = data.iloc[3]
    print(row2)
