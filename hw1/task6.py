# task 6

myFriends = {
    'vasya': 'Vasiliy The Great', 
    'petia': 'Petro Petrovych',
    'kolia': 'Kolia, Just Kolia',
    'bill': 'Bill Gates',
    'chuck': 'Chuck Norris'
}

def main():
    name = input('enter you name: ').lower()
    if name in myFriends:
        print('Hello, ', myFriends[name])
    else:
        print('I don\'t know you')

if __name__ == '__main__':
    main()    