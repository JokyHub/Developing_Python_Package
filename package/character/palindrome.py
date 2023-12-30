# We define here a function that checks if the entry is a palindrome or not.
# Ex : ELLE is a palindrome ; MEME is also a palindrome.
# Check for the definition online and also other implementation methods.

def palindrome(word: str):
    """ This function reverse the word entered and check if it's the same as the original word and return TRUE"""

    return word[::-1]==word
