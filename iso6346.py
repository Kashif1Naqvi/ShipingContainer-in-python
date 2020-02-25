
def create(owner_code,serial,category='U'):
    if not (len(owner_code) == 3 and owner_code.isalpha()):
        raise ValueError("Invaild ISO 6346 owner code '{}' ".format(owner_code))
    if category not in ('U','J','Z','R'):
        raise ValueError("Invaild ISO 6346 category identifier '{}' ".format(category))
    if not (len(serial)  == 6 and serial.isdigit() ):
        raise ValueError("Invaild ISO 6446 serial number")

    raw_code = owner_code + category + serial
    full_Code = raw_code + str(check_digit(raw_code))
    return full_Code

def check_digit(raw_code):
    s = sum(code(char) * 2 **index for index, char in enumerate(raw_code) )
    return s % 11 % 10

def code(char):
    return int(char) if char.isdigit() else letter_code(char)

def letter_code(letter):
    value = ord(letter.lower()) - ord('a')  + 10
    return value + 1
