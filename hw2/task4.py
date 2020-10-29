from random import randint

# task 4

def main():
    N = 20

    array = []
    for k in range(0, N):
        if k % 2 == 0:
            array.append(randint(1, N//2))
        else:
            array.append(-randint(1, N//2)) 
    print(array) 

    try:
        inputNum = int(input('number: '))
        count = 0
        for number in array:
            if number == inputNum:
                count += 1
        print('number {:d} is repeated in the array {:d} times'.format(inputNum,count))
        
    except Exception as exp:
        print('Error: ', exp)
    finally:
        print('bye!')
    
if __name__ == '__main__':
    main()

