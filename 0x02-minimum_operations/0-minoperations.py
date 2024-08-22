#!/usr/bin/python3
'''Minimum Operations Python3'''


def minOperations(n):
    '''
    Calculates the minimum number of operations required
    to achieve exactly `n` "H" characters in a file.

    Prototype:
        def minOperations(n)

    Returns:
        int: The minimum number of operations needed.
             If it is impossible to achieve `n`, returns 0.
    '''
    current_chars = 1  # Number of "H" characters currently in the file
    clipboard_chars = 0  # Number of "H" characters copied to the clipboard
    operations = 0  # Total number of operations performed

    while current_chars < n:
        # If no characters have been copied yet
        if clipboard_chars == 0:
            # Copy all current characters
            clipboard_chars = current_chars
            # Increment the operation counter
            operations += 1

        # If no paste operation has been performed yet
        if current_chars == 1:
            # Paste the copied characters
            current_chars += clipboard_chars
            # Increment the operation counter
            operations += 1
            # Continue to the next iteration
            continue

        remaining_chars = n - current_chars  # Remaining characters needed

        # Check if it's impossible to reach `n`
        # If the clipboard contains more characters than needed
        # or if the current number of characters is equal to or
        # greater than the clipboard content.
        if remaining_chars < clipboard_chars:
            return 0

        # If the remaining characters cannot be evenly divided by the current count
        if remaining_chars % current_chars != 0:
            # Paste the characters from the clipboard
            current_chars += clipboard_chars
            # Increment the operation counter
            operations += 1
        else:
            # Copy all current characters
            clipboard_chars = current_chars
            # Paste the copied characters
            current_chars += clipboard_chars
            # Increment the operation counter by 2 (copy + paste)
            operations += 2

    # Return the total operation count if `n` is achieved
    if current_chars == n:
        return operations
    else:
        return 0
