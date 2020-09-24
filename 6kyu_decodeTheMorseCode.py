def decodeMorse(morse_code):
    plain_text = [x.split(' ') for x in morse_code.split('  ')]
    msg = ''
    for word in plain_text:
        for char in word:
            if char in MORSE_CODE.keys():
                msg += MORSE_CODE[char]
            else:
                msg += ' '
    return msg.strip() 