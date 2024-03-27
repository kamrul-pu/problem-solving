"""
You have a browser of one tab where you start on the homepage and you can visit another url,
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history
and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history
and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
"""


class Node:
    def __init__(self, data: str, next=None, prev=None) -> None:
        """
        Initialize a Node object with data, next, and previous pointers.

        Args:
            data (str): The URL data stored in the node.
            next (Node, optional): Reference to the next node in the linked list. Defaults to None.
            prev (Node, optional): Reference to the previous node in the linked list. Defaults to None.
        """
        self.data = data
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        """
        Initialize the BrowserHistory object with the homepage.

        Args:
            homepage (str): The URL of the homepage.
        """
        # Initialize the current page with the homepage
        self.current: Node = Node(data=homepage)

    def visit(self, url: str) -> None:
        """
        Visit a new URL, appending it to the history and clearing forward history.

        Args:
            url (str): The URL to be visited.
        """
        # Create a new node for the visited URL
        node: Node = Node(data=url, prev=self.current)
        # Link the new node to the current page
        self.current.next = node
        # Update the current page to the newly visited URL
        self.current = node

    def back(self, steps: int) -> str:
        """
        Move back in the history by the specified number of steps.

        Args:
            steps (int): The number of steps to move back.

        Returns:
            str: The URL after moving back in history by the specified steps.
        """
        # Traverse backward in the history by the specified number of steps
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        # Return the URL of the current page after moving back in history
        return self.current.data if self.current else None

    def forward(self, steps: int) -> str:
        """
        Move forward in the history by the specified number of steps.

        Args:
            steps (int): The number of steps to move forward.

        Returns:
            str: The URL after moving forward in history by the specified steps.
        """
        # Traverse forward in the history by the specified number of steps
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        # Return the URL of the current page after moving forward in history
        return self.current.data if self.current else None


if __name__ == "__main__":
    # Example usage
    browser_history: BrowserHistory = BrowserHistory(homepage="leetcode.com")
    print(browser_history.visit(url="google.com"))
    print(browser_history.visit(url="facebook.com"))
    print(browser_history.visit(url="youtube.com"))
    print(browser_history.back(steps=1))
    print(browser_history.back(steps=1))
    print(browser_history.forward(steps=1))
    print(browser_history.visit(url="linkedin.com"))
    print(browser_history.forward(steps=2))
    print(browser_history.back(steps=2))
    print(browser_history.back(steps=7))
