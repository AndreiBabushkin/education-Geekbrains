"""Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах."""


def new_contact():

    contacts = ['Number', 'Name', 'Surname', 'Text']
    dict_contact = {contact: input(f'Укажите {contact}') for contact in contacts}
    return dict_contact



