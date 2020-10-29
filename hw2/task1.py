from random import choice

# task 1
players = (
    'Liam','Noah','Oliver','William','Elijah',
    'James','Benjamin','Lucas','Mason','Ethan',
    'Olivia','Emma','Ava','Sophia','Isabella',
    'Charlotte','Amelia','Mia','Harper','Evelyn'
)

def main():
    print('The winner is: ', choice(players))

if __name__ == '__main__':
    main()