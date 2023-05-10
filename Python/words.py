dictionary=[]

while True:
    print('*' * 49)
    print('*' + '\t\t' + 'Sookmyung Dictionary' + '\t\t' + '*')
    print('*' * 49)
    print('\t' + '1. Add words')
    print('\t' + '2. Delete words')
    print('\t' + '3. Print dictionary')
    print('\t' + '4. Exit')
    print('=' * 49)
    menu = int(input('Select a menu: '))

    if menu == 1:
        print('Enter words to add (Press ENTER to finish)')
        while True:
            words = input('word: ')
            if len(words) == 0:
                break
            elif words in dictionary:
                print('Already exists!!')
            else:
                dictionary.append(words)
        print()

    elif menu == 2:
        print('Enter words to delete (Press ENTER to finish)')
        while True:
            words = input('word: ')
            if len(words) == 0:
                break
            elif words not in dictionary:
                print("Doesn't exist!")
            else:
                dictionary.remove(words)
        print()

    elif menu == 3:
        print('Sookmyung dictionary:')
        for words in dictionary:
                print('   ' + words)
        print()

    elif menu == 4:
        break

    else:
        print('You entered a wrong menu!!'+ '\n')
