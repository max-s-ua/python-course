# task 1

def main():
    print('Hi. Lets calcutale you deposit...')
    try:
        amount = float(input('amount: '))
        if amount < 0:
            raise ValueError('\'amount\' must be positive')
        rate = float(input('rate: '))
        if rate < 0:
            raise ValueError('\'rate\' must be positive')
        years = int(input('years: '))
        if rate < 0:
            raise ValueError('\'years\' must be positive')

        print('Year\tAmound\tProfit')    
        for year in range(1, years+1):
            profit = amount * rate / 100
            print('{:d}\t{:5.2f}\t{:5.2f}'.format(year,amount,profit))
            amount += profit
            
    except Exception as e:
        print('Error: ', e)
    finally:
        print('bye!')

if __name__ == '__main__':
    main()
