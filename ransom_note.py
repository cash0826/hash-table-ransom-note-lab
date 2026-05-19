def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    
    note = ""
    letters = {}
    
    for char in magazine:
        letters[char] = letters.get(char, 0) + 1
    
    for char in ransomNote:
        if letters.get(char, 0) > 0:
            note += char
            letters[char] -= 1
        else:
            return False
    
    return note == ransomNote
            
# Poor-man debugging
print(can_construct("listen", "silent night"))
print(can_construct("cat", "act one"))
print(can_construct("robar", "act one"))