import argparse

def main():
    gold = 0
    bronze = 0
    silver = 0
    year = '1996'
    country = 'Algeria'
    res = ''
    with open('olympic_athlets.tsv') as file:
        i = 10
        for line in file:
            one_line = line.split('\t')
            line_year= one_line[-6]
            line_country = one_line[6]
            medal = one_line[-1]
            name = one_line[1]
            if i >= 0:
                if year == line_year and country == line_country:
                    print(f'{name} - {line_year} - {medal}')
                    if 'Gold' in medal:
                        gold += 1
                    elif 'Silver' in medal:
                        silver += 1
                    elif 'Bronze' in medal:
                        bronze += 1
                    i -= 1
                    res += f'{name} - {line_year} - {medal}' + '\n'

        if i == 10:
            print('There wasn\'t an olympiad this year')
            res += 'There wasn\'t an olympiad this year \n'

    print(f'Total gold: {gold}')
    print(f'Total silver: {silver}')
    print(f'total bronze: {bronze}')
    res += f'Total gold: {gold}\n' + f'Total silver: {silver}\n' + f'total bronze: {bronze}\n'


    with open("result.txt", "w") as file:
        file.write(res)

if __name__ == '__main__':
    main()

