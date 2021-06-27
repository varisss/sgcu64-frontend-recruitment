# I try to make the app more practical by storing the data on a server
# so the checkins will not be lost when the app close or rerun

import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://Varis:1234@cluster0.qofjm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['chula_chana']

collections = [db['sala'], db['sportscomplex'], db['mitrtown'], db['engineering'], db['arts']]

places = [
    {'name': 'Sala Phra Keaw'},
    {'name': 'CU Sports Complex'},
    {'name': 'Samyan Mitrtown'},
    {'name': 'Faculty of Engineering'},
    {'name': 'Faculty of Arts'}
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
        collections[i].delete_many({'number': number})
    # check the number into the selected place
    collections[int(place) - 1].insert_one({'number': number})
    print('Checking in ' + number + ' into ' + places[int(place) - 1]['name'])
    print(divider)

def checkout():
    # in case there is no number provided (checkout without checking in first)
    if number == '':
        number2 = input('Enter phone number: ')
        for i in range(len(places)):
            collections[i].delete_many({'number': number2})
        print('Checked ' + number2 + ' out successfully')
        print(divider)
    for i in range(len(places)):
        collections[i].delete_many({'number': number})
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
            print('\t' + str(i + 1) + '. ' + places[i]['name'] + ': ' + str(collections[i].count_documents({})))
        print(divider)