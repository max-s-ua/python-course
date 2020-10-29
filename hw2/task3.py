from datetime import datetime, date
from calendar import monthrange, weekday

months = ('січні','лютому','березні','квітні','травні','червні','липні', \
    'серпні','вересні','жовтні','листопаді','грудні')
_days = ('понеділок','вівторок','середа','четвер','п\'ятниця','субота','неділя')

# task 3
def main():
    try:
        #datestr = '02-02-2019'
        datestr = input('d-m-Y: ') 
        dat = datetime.strptime(datestr,'%d-%m-%Y').date()
        days = monthrange(dat.year, dat.month)[1]
        day = weekday(dat.year, dat.month, dat.day)
        
        dayoff = ''
        if day == 5 or day == 6:
            dayoff = 'вихідний'
        else: dayoff = 'не вихідний'

        print('У {:s} {:d} року - {:d} день(-ів)'.format(months[dat.month-1], dat.year, days))
        print('{:s} - {:s} ({:s})'.format(datestr, dayoff, _days[day]))
    except Exception as exp:
        print('Error: ',exp)
    

if __name__ == "__main__":
    main()

