# task 2

ones = ('один','два','три','чотири','п\'ять','шість','сім','вісім','дев\'ять')
teens = ('десять','одинадцять','дванадцять','тринадцять','чотирнадцять','п\'ятнадцять',
    'шістнадцять','сімнадцять','вісімнадцять','дев\'ятнадцять')
tenth = ('десять','двадцять','тридцять','сорок','п\'ятдесят','шістдесят',
    'сімдесят','вісімдесят','дев\'яносто')
hundreds = ('сто','двісті','триста','чотириста','п\'ятсот','шістсот',
    'сімсот','вісімсот','дев\'ятсот')  
thousands = ('','тисяч(-а,-і)','мільйон(-и,-ів)','мільяр(-и,-ів)')

# get digits from integer > 0
def getDigits(intNum):
    result = list()
    while intNum > 0:
        result.append(intNum % 10)
        intNum //= 10
    while len(result) % 3 != 0:
        result.append(0)
    return result

# get text for 3-digit number, ex. 342
def process3digits(onesNum, tenthNum, hundrNum):
    resultList = list()
    if hundrNum != 0:
        resultList.append(hundreds[hundrNum-1])
    if tenthNum == 1:
        resultList.append(teens[onesNum])
    else:
        if tenthNum != 0:
            resultList.append(tenth[tenthNum-1])
        if onesNum != 0:
            resultList.append(ones[onesNum-1])
    return ' '.join(resultList)

# get string representation from integer
def getStringFromInt(intNum):
    if intNum == 0:
        return 'нуль'
    if abs(intNum) > 999999999:
        return 'та ну його...'
    resultList = list()
    digits = getDigits(abs(intNum))
    
    for k in range(2,len(digits),3):
        resultList.append(thousands[k//3])
        resultList.append(process3digits(digits[k-2],digits[k-1],digits[k]))
    if intNum < 0:
        resultList.append('мінус')
    resultList.reverse()
    return ' '.join(resultList)
        
def main():
    try:
        inputNum = int(input('integer: '))
        str = getStringFromInt(inputNum)
        print(str)
    except Exception as ex:
        print('Error: ', ex)
    finally:
        print('bye!')
    
if __name__ == '__main__':
    main()

