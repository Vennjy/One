
import os
from Recources.Classes import *

'''Hello! This is a simple script i wrote that makes and deletes organisms. I worked on this for one and a half day,
   and I finished at November 15 2019. How are you future Vennjy :).'''

def main():
    loop = True
    user = Organism('User', None)

    # Greeting Message:
    text = 'Greetings! This is a simple script to create or remove organisms. Below are the list of actions you could '\
           'do. '

    print('\n', text)
    user.help()

    # End of Greeting Message.
    # [______________________]
    # Start of the script

    while loop:
        a = input('>>> ')
        if a.lower() == 'x':
            break

        if a.lower() == 'remove':
            user.remove()
        if a.lower() == 'show':
            user.all()
        if a.lower() == 'create':
            user.create()
        if a.lower() == 'list':
            print(user.population)
            print('')
        if a.lower() == 'help':
            user.help()
        if a.lower() == 'clear':  # Does not work properly on IDEs
            os.system('cls')
            print('\n', text)
            user.help()


if __name__ == '__main__':
    main()
