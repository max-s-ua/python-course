# task 5

def main():
    print('Digits sum and count')
    try:
        number = int(input('number: '))
        number = abs(number)
        count = 0
        sum = 0
        while number > 0:
            sum += number % 10
            count += 1
            number //= 10
        print('count: ', count)
        print('sum: ', sum)

    except Exception as e:
        print('Error: ', e)
    finally:
        print('bye!')

if __name__ == '__main__':
    main()