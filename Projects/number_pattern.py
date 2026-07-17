def number_pattern(n):
    if type(n) is not int:
        return "Argument must be an integer value."
    if n < 1: 
        return 'Argument must be an integer greater than 0.'
    else : 
        number = ''
        for i in range(1,n+1):
            number += str(i) + ' '
        return number.strip()
print(number_pattern(4)) 