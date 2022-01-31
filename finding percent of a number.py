connect = True


while connect == True:
    number = input('nomer: ')
    procent = input('porsenr: ')
    while type(number) != int:
        try:
            number = int(number)
            procent = int(procent)
        except ValueError:
            print('vodi ifrõ: ')
            number = input('vodi tislo: ')
            print()
            procent = input('vidi prosent: ')  
            print()  

    while type(number) != float:
        try:
            number = float(number)
            procent = float(procent)

        except ValueError:
            print('vodi ifrõ!')
            number = input('tislo: ')
            print()
            procent = input('prosent: ')  
            print()  


            
    finish = number / 100 * procent

    print('teie vastus:', float(finish))