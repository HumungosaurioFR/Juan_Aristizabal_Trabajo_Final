list_appointment = []

sw = True
import os

def fnt_clean():
    os.system('cls')
    print('For: Juan Esteban Aristizábal Suárez\nDate: 21th may of 2024\n')

def fnt_add():
    fnt_clean()
    name = input('\nOwners name: ')
    contact = input('telephone: ')
    animal = input('Pets race: ')
    day = input('Date of appointment(DD/MM/YY): ')
    appointment = (f'Owners Name: {name}, Telephone: {contact}, Animal: {animal}, Date: {day}')
    list_appointment.append(appointment)
        
def fnt_check():
    fnt_clean()
    for i in list_appointment:
        print(i)
        
        enter = input('\n<ENTER>')
    
while sw == True:
    fnt_clean()
    op = input('<<< Welcome to PetAristiShop (The place for your animals) >>>\n\n1. Regiter appointment\n2. Check Appointments\n3. Exit\n\n-> ')
    if op == '1':
        fnt_add()
    if op == '2':
        fnt_check()
    if op == '3':
        sw = False
        fnt_clean()
        print('Goodbye')
        enter = input('<ENTER>')