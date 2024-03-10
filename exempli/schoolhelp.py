print('Welcome to Sydney Boys High School')
name = input('What is your name? ')
print(f'Hello {name}.')
swimming = input('Can you swim 50 metres? ')
if swimming.lower() == 'yes':
    print('You might like to try water polo.')
else:
    ball = input('Do you enjoy ball sports? ')
    if ball.lower() == 'yes':
        contact_sports = input('Do you enjoy contact sports? ')
        if contact_sports.lower() == 'yes':
            print('Perhaps try basketball.')
        else:
            print('Cricket could be a good option.')
    else:
        print('Rifle shooting')
room = input('

