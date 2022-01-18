FILENAME = 'bakery.csv'
def input_sales_in_file(sale):


    with open(FILENAME, 'a', encoding='utf-8') as bakery:
        return bakery.write(str(sale) +'\n')


if __name__ == '__main__':
    import sys
    exit(input_sales_in_file(sys.argv[1]))