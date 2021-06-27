places = [
    {'name': 'Sala Phra Keaw', 'checkins': []},
    {'name': 'CU Sports Complex', 'checkins': []},
    {'name': 'Samyan Mitrtown', 'checkins': []},
    {'name': 'Faculty of Engineering', 'checkins': []},
    {'name': 'Faculty of Arts', 'checkins': []}
]

number = ''
select = ''
divider = '--------------------\n'

def checkin():
    for i in range(len(places)):
        print('\t' + str(i + 1) + '. ' + places[i]['name'])
    place = input('Please select a place: ')
    # check the number out of other places
    for i in range(len(places)):
        if number in places[i]['checkins']:
            places[i]['checkins'].remove(number)
    # check the number into the selected place
    places[int(place) - 1]['checkins'].append(number)
    print('Checking in ' + number + ' into ' + places[int(place) - 1]['name'])
    print(divider)

def checkout():
    # in case there is no number provided (checkout without checking in first)
    if number == '':
        print('No number provided')
        print(divider)
        return
        # check the number out of any place it might be in
    for i in range(len(places)):
        if number in places[i]['checkins']:
            places[i]['checkins'].remove(number)
    print('Checked ' + number + ' out successfully')
    print(divider)

# I made another choice, number 4 will exit from the app
while select != '4':
    print('Welcome to Chula Chana\nAvilable Commands:\n\t1. Check in user\n\t2. Check out user\n\t3. Print people count\n\t4. Exit')
    select = input('Please enter a number: ')
    print(divider)

    if select == '1':
        print('Check In')
        number = input('Enter phone number: ')
        checkin()

    if select == '2': checkout()

    if select == '3':
        print('Current Population')
        for i in range(len(places)):
            print('\t' + str(i + 1) + '. ' + places[i]['name'] + ': ' + str(len(places[i]['checkins'])))
        print(divider)