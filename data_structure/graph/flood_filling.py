"""Flood filling."""


def dfs(
    sr,
    sc,
    ans: list[list[int]],
    image: list[list[int]],
    new_color: int,
    del_row: list[int],
    del_col: list[int],
    init_color: int,
) -> None:
    # Mark the current cell with the new color
    ans[sr][sc] = new_color

    # Get the number of rows and columns in the image
    n: int = len(image)
    m: int = len(image[0])

    # Explore neighbors in four directions (up, right, down, left)
    for i in range(4):
        nrow: int = sr + del_row[i]
        ncol: int = sc + del_col[i]

        # Check if the neighbor is within the bounds of the image
        # and has the same initial color, and hasn't been visited yet
        if (
            nrow >= 0
            and nrow < n
            and ncol >= 0
            and ncol < m
            and image[nrow][ncol] == init_color
            and ans[nrow][ncol] != new_color
        ):
            # Recursive call to explore the neighbor
            dfs(
                sr=nrow,
                sc=ncol,
                ans=ans,
                image=image,
                new_color=new_color,
                del_row=del_row,
                del_col=del_col,
                init_color=init_color,
            )


def flood_fill(
    image: list[list[int]], sr: int, sc: int, new_color: int
) -> list[list[int]]:
    # Get the initial color of the starting point
    init_color: int = image[sr][sc]

    # Create a copy of the image to store the result
    ans: list[list[int]] = image.copy()

    # Define the directions to explore (up, right, down, left)
    del_row: list[int] = [-1, 0, 1, 0]
    del_col: list[int] = [0, 1, 0, -1]

    # Call the DFS function to perform flood fill
    dfs(
        sr=sr,
        sc=sc,
        ans=ans,
        image=image,
        new_color=new_color,
        del_row=del_row,
        del_col=del_col,
        init_color=init_color,
    )

    # Return the updated image after flood fill
    return ans


if __name__ == "__main__":
    # Example usage of the flood_fill function
    image: list[list[int]] = [
        [1, 1, 1],
        [2, 2, 0],
        [2, 2, 2],
    ]
    print("Original Image:")
    print(image)

    # Perform flood fill starting from position (1, 1) with new color 3
    result = flood_fill(image=image, sr=1, sc=1, new_color=3)

    print("\nImage after Flood Fill:")
    print(result)
