def is_palindrome(string):
    """
    Check if a string is a palindrome.

    Args:
        string (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove any whitespace and convert the string to lowercase
    string = string.replace(" ", "").lower()

    # Check if the reversed string is equal to the original string
    return string == string[::-1]