def maior(um,dois,tres,quatro,cinco):
    med=(um+dois+tres+quatro+cinco)/5
    print(f'{"%.2f"%med}')
    if um > med:
        print(f'{"%.2f"%um}')
        if dois>med:
            print(f'{"%.2f"%dois}')
            if tres>med:
                print(f'{"%.2f"%tres}')
                if quatro>med:
                    print(f'{"%.2f"%um}')
                    if cinco>med:
                        print(f'{"%.2f"%um}')
    elif dois>med:
        print(f'{"%.2f"%dois}')
        if tres>med:
            print(f'{"%.2f"%tres}')
            if quatro>med:
                print(f'{"%.2f"%um}')
                if cinco>med:
                    print(f'{"%.2f"%um}')
    elif tres>med:
        print(f'{"%.2f"%tres}')
        if quatro>med:
            print(f'{"%.2f"%um}')
            if cinco>med:
                print(f'{"%.2f"%um}')
    elif quatro>med:
        print(f'{"%.2f"%um}')
        if cinco>med:
            print(f'{"%.2f"%um}')
    elif cinco>med:
        print(f'{"%.2f"%um}')
def main():
    um=int(input(''))
    dois=int(input(''))
    tres=int(input(''))
    quatro=int(input(''))
    cinco=int(input(''))
    maior(um,dois,tres,quatro,cinco)
if __name__=='__main__':
    main()

