# task 2

def main():
    print('Hi. Lets calcutale price of cheese...')
    try:
        price = float(input('price of 1 kg: '))
        if price < 0:
            raise ValueError('\'value\' must be positive')

        print('weight(g)\tPrice(usd)')    
        for weight in range(50, 1050, 50):
            print('{:5.2f}\t\t{:5.2f}'.format(weight,weight * price / 1000))
            
    except Exception as e:
        print('Error: ', e)
    finally:
        print('bye!')

if __name__ == '__main__':
    main()