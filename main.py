import argparse


parser = argparse.ArgumentParser(
        prog="Awesome Lesya Ukrainka",
        description="Analyzing olympic athlets dataset"
    )

parser.add_argument('filename', help='name of input file')
parser.add_argument('-medals', '--medals', nargs=2, help='Used for getting count of medals for each type of countries')
parser.add_argument('-total', '--total', help='Used for getting total result for each country')
parser.add_argument('-overall', '--overall', help="Used for getting highest medals and year for following countries")
parser.add_argument('-interactive', '--interactive', help="Used for getting statistic for current country")
parser.add_argument('-output', '--output', nargs=1, help='name of output file')


def get_medals_count(filename: str, team: str, year: str) -> str:
    gold = 0
    bronze = 0
    silver = 0

    res = ''

    with open(filename) as file:
        i = 10
        for line in file:
            one_line = line.split('\t')
            line_year= one_line[-6]
            line_country = one_line[6]
            medal = one_line[-1]
            name = one_line[1]
            if i >= 0:
                if year == line_year and team == line_country:
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

    return res


def main():
    args = parser.parse_args()

    if args.medals:
        res = get_medals_count('olympic_athlets.tsv', args.medals[0], args.medals[1])

    if args.output:
        with open(args.output[0], "w") as file:
            file.write(res)


if __name__ == '__main__':
    main()
