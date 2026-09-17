"""
Olympic Weight Sorting
Sport: Weightlifting
Connor J. T.
9/8/2026
"""
weightkg = float

print('Hello, and welcome to the Olympic weight lifting categorizer!')
print('These categories are for the Los Angeles 2028 Olympics.')
gender = input('Are you Male or Female?')


if gender == 'Male':
    weightkg = float(input('Great! Now, M, type in your weight in Kilograms.'))
    
    if weightkg > 110:
        print('You are in the +110kg category')
    elif weightkg < 65:
        print('You are in the -65kg category')
    elif weightkg < 75:
        print('You are in the 65-75kg category')
    elif weightkg < 85:
        print('You are in the 75-85kg category')
    elif weightkg < 95:
        print('You are in the 85-95kg category')
    elif weightkg < 110:
        print('You are in the 95-110kg category')
    
    
if gender == ('female' or 'Female' or 'f'):
    weightkg = float(input('Great! Now, F, type in your weight in Kilograms.'))
    
    if weightkg > 86:
        print('You are in the +86kg category')
    elif weightkg < 53:
        print('You are in the -53kg category')
    elif weightkg < 61:
        print('You are in the 53-61kg category')
    elif weightkg < 69:
        print('You are in the 61-69kg category')
    elif weightkg < 77:
        print('You are in the 69-77kg category')
    elif weightkg < 86:
        print('You are in the 77-86kg category')
        
