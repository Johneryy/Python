def bool_to_word(boolean):

    if boolean == "Yes".lower().upper():
        return True
    elif boolean == "No".lower().upper():
        return False
    else:
        return "Invalid String,Enter YES or NO"

bool = input("Enter Yes or No-> ")
print(bool_to_word(bool))