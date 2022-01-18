FILENAME = 'bakery.csv'

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        with open(FILENAME, 'r', encoding='utf-8') as bakery:
            print(bakery.read())
    elif len(sys.argv) == 2:
        with open(FILENAME, 'r', encoding='utf-8') as bakery:
            sales = bakery.read()
            sales_list = []
            for sale in sales.split('\n'):
                sales_list.append(sale)
            n = int(sys.argv[1]) - 1
            for ind in sales_list[n:]:
                print(ind)
    elif len(sys.argv) == 3:
        with open(FILENAME, 'r', encoding='utf-8') as bakery:
            sales = bakery.read()
            sales_list = []
            for sale in sales.split('\n'):
                sales_list.append(sale)
            n = int(sys.argv[1]) - 1
            z = int(sys.argv[2])
            for ind in sales_list[n:z]:
                print(ind)

