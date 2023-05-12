dictionary = {}

while True:
    print('*' * 49)
    print('*' + '\t\t' + 'Sookmyung Dictionary' + '\t\t' + '*')
    print('*' * 49)
    print('\t' + '1. Add words and meanings')
    print('\t' + '2. Delete words')
    print('\t' + '3. Print dictionary')
    print('\t' + '4. Look up words')
    print('\t' + '5. Vocabulary test')
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
        print('Sookmyung dictionary:')
        for key, value in sorted(dictionary.items()):
            print('%20s  %20s' % (key, value))
        print()
            
    elif menu == 4:
        print('Enter words to look up (Press ENTER to finish)')
        while True:
            key = input('word: ')
            if len(key) == 0:
                break
            elif key in dictionary:
                print(f'{dictionary[key]}')
            else:
                print('  ', f"'{key}' not found")
        print()

    elif menu == 5:
        score = 0
        for key in dictionary:
            answer = input(f"meaning of '{key}': ")
            if answer == value:
                score += 1
        print(f"*** {score} correct answers out of {len(dictionary)} ***\n")
            
    elif menu == 6:
        break

    else:
        print('You entered a wrong menu!!')