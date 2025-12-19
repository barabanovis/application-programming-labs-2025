import argparse
import pandas as pd


def argument_parsing() -> list[str]:
    """
    Разделение аргументов, введённых пользователем в консоли
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('save_path', type=str, help='path to save table')
    args = parser.parse_args()
    return [args.save_path]


def main():
    df = pd.read_csv('results.csv', names=['ABSOLUTE PATH', 'RELATIVE PATH'])
    print(df)


if __name__ == '__main__':
    main()
