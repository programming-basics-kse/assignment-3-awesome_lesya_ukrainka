import argparse


parser = argparse.ArgumentParser(
        prog="Awesome Lesya Ukrainka",
        description="Analyzing dataset"
    )

parser.add_argument('filename', help='name of input file')
parser.add_argument('command', help=' \
                    -medals - used for getting count of medals each type for country, \
                    -total - used for getting total result for each country, \
                    -overall - used for getting highest medals and year for following countries, \
                    -interactive - used for getting statistic for current country',
                    choices=('-medals', '-total', '-overall', '-interactive'))
parser.add_argument('team', help='name of country or code of team')
parser.add_argument('year', help='year of games')
parser.add_argument('--output', help='name of output file')


def main():
    args = parser.parse_args()

    print('Hello World!')


if __name__ == '__main__':
    main()