import argparse


parser = argparse.ArgumentParser(
        prog="Awesome Lesya Ukrainka",
        description="Analyzing olympic athlets dataset"
    )

parser.add_argument('filename', help='name of input file')
parser.add_argument('-medals', '--medals', nargs=2, help='Used for getting count of medals for each type of countries')
parser.add_argument('-total', '--total', nargs=1, help='Used for getting total result for each country')
parser.add_argument('-overall', '--overall', nargs="*", help="Used for getting highest medals and year for following countries")
parser.add_argument('-interactive', '--interactive', action="store_true", help="Used for getting statistic for current country")
parser.add_argument('-output', '--output', nargs=1, help='name of output file')


def get_medals_count(filename: str, team: str, year: str) -> str:
    gold = 0
    bronze = 0
    silver = 0

    res = ''

    try:
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
    except Exception:
        print('please enter a valid dataset filename')

    print(res)
    return res


def get_medals_total(filename: str, year: str) -> str:
    count_medals = {}
    res = ''

    try:
        with open(filename) as file:
            for line in file:
                one_line = line.split('\t')
                line_year = one_line[-6]
                line_country = one_line[6]
                medal = one_line[-1].strip()

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
    except Exception:
        print('Please enter a valid dataset filename')

    print(res)
    return res


def get_medals_overall(filename: str, countries: list[str]) -> str:
    data = {}
    res = ''

    try:
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
    except Exception:
        print('Please enter a valid dataset filename')

    print(res)
    return res


def  get_interactive_statistics(filename: str, country: str) -> str:
    try:
        res = ''
        first_participation = {}
        total_medals_by_year = {}

        with open(filename) as file:
            for line in file:
                one_line = line.split('\t')
                team_code = one_line[7]
                line_country = one_line[6]
                if country.lower() != team_code.lower() and country.lower() not in line_country.lower():
                    continue

                medal = str(one_line[-1]).strip()
                year = int(one_line[9])
                city = one_line[11]

                if 'year' not in first_participation:
                    first_participation['year'] = year
                    first_participation['city'] = city
                elif year < first_participation['year']:
                    first_participation['year'] = year
                    first_participation['city'] = city

                if 'NA' not in medal and medal:
                    if year not in total_medals_by_year:
                        total_medals_by_year[year] = {
                            'count': 1,
                            'gold': 1 if medal == 'Gold' else 0,
                            'silver': 1 if medal == 'Silver' else 0,
                            'bronze': 1 if medal == 'Bronze' else 0,
                        }
                    else:
                        total_medals_by_year[year]['count'] += 1

                        if medal == 'Gold':
                            total_medals_by_year[year]['gold'] += 1
                        elif medal == 'Silver':
                            total_medals_by_year[year]['silver'] += 1
                        elif medal == 'Bronze':
                            total_medals_by_year[year]['bronze'] += 1

        if 'year' in first_participation:
            res += f'First participation: {first_participation['year']} in {first_participation['city']} \n'

        if total_medals_by_year:
            max_year, max_medals = max(total_medals_by_year.items(), key=lambda x: x[1]['count'])

            if max_medals:
                res += f'The most successful olympiad: in {max_year} ({max_medals['count']} medals) \n'

            min_year, min_medals = min(total_medals_by_year.items(), key=lambda x: x[1]['count'])

            if min_medals:
                res += f'The most unsuccessful olympiad: in {min_year} ({min_medals['count']} medals) \n\n'

            gold_medals = [item['gold'] for item in total_medals_by_year.values()]
            silver_medals = [item['silver'] for item in total_medals_by_year.values()]
            bronze_medals = [item['bronze'] for item in total_medals_by_year.values()]

            avg_gold_medals = round(sum(gold_medals) / len(gold_medals), 1)
            avg_silver_medals = round(sum(silver_medals) / len(silver_medals), 1)
            avg_bronze_medals = round(sum(bronze_medals) / len(bronze_medals), 1)

            res += f'Average of gold medals: {avg_gold_medals} \n'
            res += f'Average of silver medals: {avg_silver_medals} \n'
            res += f'Average of bronze medals: {avg_bronze_medals} \n'

        print(res)
        return res

    except Exception:
        print('Please, enter a valid dataset filename')
        return ''


def main():
    args = parser.parse_args()

    if args.medals:
        res = get_medals_count(args.filename, args.medals[0], args.medals[1])
    elif args.total:
       res = get_medals_total(args.filename, args.total)
    elif args.overall:
        res = get_medals_overall(args.filename, args.overall)
    elif args.interactive:
        res = ''
        while True:
            country = input('Input country or exit: ')
            if country == 'exit':
                break
            else:
                one_country = get_interactive_statistics(args.filename, country)
                res += one_country
                while one_country == '' and country != 'exit':
                    country = input('No country that matches this, try again: ')

                    if country == 'exit':
                        return

                    one_country = get_interactive_statistics(args.filename, country)
                    res += one_country

    if args.output:
        with open(args.output[0], "w") as file:
            file.write(res)


if __name__ == '__main__':
    main()
