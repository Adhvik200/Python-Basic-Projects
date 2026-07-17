def verify_card_number(card_number):
    # Remove dashes and spaces
    digits = card_number.replace('-', '').replace(' ', '')
    
    # Reverse the digits for the algorithm
    digits = digits[::-1]
    total = 0
    
    for i, char in enumerate(digits):
        n = int(char)
        # Double every second digit
        if i % 2 == 1:
            n *= 2
            # Subtract 9 if the product is greater than 9
            if n > 9:
                n -= 9
        total += n
    
    # If the total modulo 10 is 0, the card is valid
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

# Testing the function with the provided examples
print(verify_card_number('453914889'))             # VALID!
print(verify_card_number('4111-1111-1111-1111'))   # VALID!
print(verify_card_number('1234 5678 9012 3456'))   # INVALID!
