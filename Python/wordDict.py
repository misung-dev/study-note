dictionary = {}

while True:
    print('*' * 49)
    print('*' + '\t\t' + 'Sookmyung Dictionary' + '\t\t' + '*')
    print('*' * 49)
    print('\t' + '1. Add words and meanings')
    print('\t' + '2. Delete words')
    print('\t' + '3. Print dictionary')
    print('\t' + '4. Look up words')
    print('\t' + '5. vocabulary test')
    print('\t' + '6. Exit')
    print('=' * 49)
    menu = int(input('Select a menu: '))

    
    if menu == 1:
        print('Enter words to add (Press ENTER to finish)')
        while True:
            key = input('word: ')
            if len(key) == 0:
                break
            value = input('meaning: ')
            dictionary[key] = value
        print()

    elif menu == 2:
        print('Enter words to delete (Press ENTER to finish)')
        while True:
            key = input('word: ')
            if len(key) == 0:
                break
            elif key in dictionary:
                del dictionary[key]
                print('  ', f"'{key}' successfully deleted")
            else:
                print('  ', f"'{key}' not found")
        print()

    elif menu == 3:
        print('Sookmyung dictionary:', dictionary)
        for words in dictionary:
                print('   ' + words)
        print()

    elif menu == 6:
        break

    else:
        print('You entered a wrong menu!!'+ '\n')
