import csv


def reader_excel():

    with open('Contacts.csv', 'r', encoding='utf-8', newline='') as con:
        reader_contacts = csv.DictReader(con)
        for cont in reader_contacts:
            print()
            for c in cont:
                print(c, cont[c])
