import argparse


parser = argparse.ArgumentParser(
        prog="Awesome Lesya Ukrainka",
        description="Analyzing olympic athlets dataset"
    )

parser.add_argument('filename', help='name of input file')
parser.add_argument('-medals', '--medals', nargs=2, help='Used for getting count of medals for each type of countries')
parser.add_argument('-total', '--total', help='Used for getting total result for each country')
parser.add_argument('-overall', '--overall', nargs="*", help="Used for getting highest medals and year for following countries")
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
            team_code = one_line[7]
            if i >= 0:
                if year == line_year and (team == line_country or team == team_code):
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
            res += 'There wasn\'t an olympiad this year \n'

    res += f'Total gold: {gold}\n' + f'Total silver: {silver}\n' + f'total bronze: {bronze}\n'

    print(res)
    return res


def get_medals_total(filename: str, year: str) -> str:
    count_medals = {}
    res = ''

    with open(filename) as file:
        for line in file:
            one_line = line.split('\t')
            line_year = one_line[-6]
            line_country = one_line[6]
            medal = one_line[-1]

            if year == line_year:
                if line_country not in count_medals:
                    gold = 0
                    silver = 0
                    bronze = 0
                    count_medals[line_country] = {'Gold': gold, 'Silver': silver, 'Bronze': bronze}

                    if 'Gold' in medal:
                        count_medals[line_country]['Gold'] += 1
                    elif 'Silver' in medal:
                        count_medals[line_country]['Silver'] += 1
                    elif 'Bronze' in medal:
                        count_medals[line_country]['Bronze'] += 1
                else:
                    if 'Gold' in medal:
                        count_medals[line_country]['Gold'] += 1
                    elif 'Silver' in medal:
                        count_medals[line_country]['Silver'] += 1
                    elif 'Bronze' in medal:
                        count_medals[line_country]['Bronze'] += 1

    for country in count_medals:
        res += f"{country}: {count_medals[country]['Gold']} - {count_medals[country]['Silver']} - {count_medals[country]['Bronze']} \n"

    print(res)
    return res


def get_medals_overall(filename: str, countries: list[str]) -> str:
    data = {}
    res = ''

    with open(filename) as file:
        for line in file:
            one_line = line.split('\t')
            country = one_line[6]

            if country not in countries:
                continue

            year = one_line[9]
            medal = one_line[-1]

            if country not in data:
                data[country] = {}

            if year not in data[country]:
                data[country][year] = 0

            if 'NA' not in medal:
                data[country][year] += 1

    for item in data.keys():
        stats = data[item]
        year = ''
        medals = 0

        for key, val in stats.items():
            if val > medals:
                year = key
                medals = val

        res += f"{item} - {year} - {medals} \n"

    print(res)
    return res

def  get_statistics(filename: str, country: str) -> str:
    with open(filename) as file:
        for line in file:
            one_line = line.split('\t')
            team_code = one_line[7]
            line_country = one_line[6]
            if country != (team_code or line_country):
                continue





def main():
    args = parser.parse_args()

    if args.medals:
        res = get_medals_count(args.filename, args.medals[0], args.medals[1])

    if args.total:
       res = get_medals_total(args.filename, args.total)

    if args.overall:
        res = get_medals_overall(args.filename, args.overall)

    if args.interactive:
        res = ''
        while True:
            country = input('Input country or exit:')
            if country == 'exit':
                break
            else:
                one_country = get_statistics(args.filename, country)
                res += one_country

    if args.output:
        with open(args.output[0], "w") as file:
            file.write(res)

if __name__ == '__main__':
    main()
