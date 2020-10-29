# task 4

def main():
    print('Letter neighbours')
    try:
        letter = input('input letter: ')
        letterNum = ord(letter[0])
        if letterNum not in range(ord('a'), ord('z')+1) and \
            letterNum not in range(ord('A'), ord('Z')+1):
            raise Exception('char is not a letter')
        if letterNum != ord('a') and letterNum != ord('A'): 
            print('prev: ', chr(letterNum-1))
        if letterNum != ord('z') and letterNum != ord('Z'):
            print('next: ', chr(letterNum+1))

    except Exception as e:
        print('Error: ', e)
    finally:
        print('bye!')

if __name__ == '__main__':
    main()
