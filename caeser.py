# ceaser.py
# simple program to encode a line of text using cesar cipher
# with an arbitrary offset
#
# workhorse function
# caeser(sourcetext, offset=None, reverse=False)
#
# helper function
# modulate_index(sequence, index)

# 
from string import ascii_letters, ascii_lowercase, ascii_uppercase

def modulate_index(sequence, index):
    # modulate_index(sequence, int) -> int
    # Return an number in the range -len(sequence) < i < len(sequence)
    # which can be used as a valid index in the interpreter
    return index % len(sequence)
        

def caeser(sourcetext, offset=None, reverse=False):
    # caeser(string) -> string
    # offset - integer value for cipher offset
    # reverse - bool to reverse the offset (useful for decryption)
    # Apply an offset to ascii characters.
    
    # Trivial case, return sourcetext unchanged and avoid
    # translating character by character.
    if offset == None:
        return sourcetext
    # reverse flag undoes the cipher offset. This is the same
    # as making the offset negative. Conditional merely changes
    # the sign of offset. The same effect can be achieved by
    # manually adjusting the sign of offset in the caller.
    if reverse:
        offset = -offset
    
    # build enciphered string character by character
    # For each character, if it is an ascii letter apply
    # the offset and append the new character to the cipher. 
    # Otherwise, simply append nonletters to the cipher.
    cipher = []
    for char in sourcetext:
        if char in ascii_letters:
            if char in ascii_lowercase:
                i = ascii_lowercase.index(char) + offset
                i = modulate_index(ascii_lowercase, i)
                cipher.append(ascii_lowercase[i])
            else:
                i = ascii_uppercase.index(char) + offset
                i = modulate_index(ascii_uppercase, i)
                cipher.append(ascii_uppercase[i])
        else: cipher.append(char)
    ciphertext = ''.join(cipher)
    return ciphertext
    
if __name__ == "__main__":
    print("Type a message to encode and strike Enter.")
    cleartext = input("Message: ")
    raw_offset = input("Offset [default=None]: ")
    if raw_offset != '':
        try: offset = int(raw_offset)
        except ValueError:
            print(raw_offset, "is not a valid offset. Please use an integer numeral.")
            exit()
    else: offset = None
    ciphertext = caeser(cleartext, offset)
    print("Cipher:", ciphertext)
    
