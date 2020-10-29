# task 3

def main():
    print('Check odd and even numbers in range')
    try:
        begin = int(input('begin: '))
        end = int(input('end: '))
        if begin > end:
            raise Exception('begin > end')
        print('Range {:d} - {:d}'.format(begin, end))
        odd = []
        even = []
        for number in range(begin, end+1):
            if number % 2 > 0:
                odd.append(number)
            else:
                even.append(number)
        print('odd: ', odd)
        print('even: ', even)
    except Exception as e:
        print('Error: ', e)
    finally:
        print('bye!')

if __name__ == '__main__':
    main()