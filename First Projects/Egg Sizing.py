"""
Doc String
Connor T.
9/3/2026
"""

eggsizeoz = [15, 18, 21, 24, 27, 30]
eggsize = ['Peewee', 'Small', 'Medium', 'Large', 'Extra Large', 'Jumbo']



eggoz = float(input('Please type in Dozen egg weight in ounces'))
print('Your Dozen Egg Weight is',eggoz,'oz')

print('Method 1, Slower')

if eggoz < 15:
    print('Your egg is tooooo small')
if 15 <= eggoz < 18:
    eggsize = 'Peewee'
    print('Your Egg size per dozen is',eggsize)
    pass
if 18 <= eggoz < 21:
    eggsize = 'Small'
    print('Your Egg size per dozen is',eggsize)
    pass
if 21 <= eggoz < 24:
    eggsize = 'Medium'
    print('Your Egg size per dozen is',eggsize)
    pass
if 24 <= eggoz < 27:
    eggsize = 'Large'
    print('Your Egg size per dozen is',eggsize)
    pass
if 27 <= eggoz < 30:
    eggsize = 'Extra Large'
    print('Your Egg size per dozen is',eggsize)
    pass
if eggoz >= 30:
    eggsize = 'Jumbo'
    print('Your Egg size per dozen is',eggsize)
    pass


print('Method 2, Faster')

if eggoz < 15:
    print('TOO SMALL')
elif eggoz < 18:
    eggsize = 'Peewee'
    print('Your Egg size per dozen is',eggsize)
    pass
elif eggoz < 21:
    eggsize = 'Small'
    print('Your Egg size per dozen is',eggsize)
    pass
elif eggoz < 24:
    eggsize = 'Medium'
    print('Your Egg size per dozen is',eggsize)
    pass
elif eggoz < 27:
    eggsize = 'Large'
    print('Your Egg size per dozen is',eggsize)
    pass
elif eggoz < 30:
    eggsize = 'Extra Large'
    print('Your Egg size per dozen is',eggsize)
    pass
elif eggoz >= 30:
    eggsize = 'Extra Large'
    print('Your Egg size per dozen is',eggsize)
    pass
