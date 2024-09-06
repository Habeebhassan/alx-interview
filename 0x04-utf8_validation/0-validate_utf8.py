#!/usr/bin/python3
"""Module for validating UTF-8 encoded data.
"""

def validUTF8(data):
    """Determines if a given list of integers represents a valid UTF-8 encoding.

    In UTF-8 encoding, a character can be between 1 and 4 bytes long.
    The input list can contain multiple characters.
    Each integer in the list represents a byte in the data.

    Args:
        data (list): A list of integers where each integer corresponds to a byte
                     in the UTF-8 encoded data.

    Returns:
        bool: True if the data represents a valid UTF-8 encoding, False otherwise.
    """
    pending_bytes = 0
    total_bytes = len(data)
    
    for index in range(total_bytes):
        if pending_bytes > 0:
            pending_bytes -= 1
            continue
        
        if not isinstance(data[index], int) or data[index] < 0 or data[index] > 0x10FFFF:
            return False
        
        if data[index] <= 0x7F:
            pending_bytes = 0
        elif data[index] & 0b11111000 == 0b11110000:
            # 4-byte UTF-8 character
            expected_bytes = 4
            if total_bytes - index >= expected_bytes:
                subsequent_bytes_valid = all(
                    (byte & 0b11000000 == 0b10000000)
                    for byte in data[index + 1: index + expected_bytes]
                )
                if not subsequent_bytes_valid:
                    return False
                pending_bytes = expected_bytes - 1
            else:
                return False
        elif data[index] & 0b11110000 == 0b11100000:
            # 3-byte UTF-8 character
            expected_bytes = 3
            if total_bytes - index >= expected_bytes:
                subsequent_bytes_valid = all(
                    (byte & 0b11000000 == 0b10000000)
                    for byte in data[index + 1: index + expected_bytes]
                )
                if not subsequent_bytes_valid:
                    return False
                pending_bytes = expected_bytes - 1
            else:
                return False
        elif data[index] & 0b11100000 == 0b11000000:
            # 2-byte UTF-8 character
            expected_bytes = 2
            if total_bytes - index >= expected_bytes:
                subsequent_bytes_valid = all(
                    (byte & 0b11000000 == 0b10000000)
                    for byte in data[index + 1: index + expected_bytes]
                )
                if not subsequent_bytes_valid:
                    return False
                pending_bytes = expected_bytes - 1
            else:
                return False
        else:
            return False
    
    return True
