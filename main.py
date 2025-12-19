import argparse
import pandas as pd
import cv2
import matplotlib.pyplot as plt


def argument_parsing() -> list[str]:
    """
    Разделение аргументов, введённых пользователем в консоли
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('table_path', type=str, help='path to save table')
    parser.add_argument('gist_path', type=str, help='path to save diagram')
    args = parser.parse_args()
    return [args.table_path, args.gist_path]


def which_orientation(path_to_image: str) -> str:
    '''
    Определяет ориентацию картинки: вертикальная, горизонтальная или квадратная
    '''
    print(path_to_image)
    image = cv2.imread(path_to_image)
    if image is None:
        raise ValueError

    if image.shape[0] == image.shape[1]:
        return 'square'
    elif image.shape[0] < image.shape[1]:
        return 'vertical'
    else:
        return 'horizontal'


def sort_by_orientation(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Сортирует датафрейм по столцу "ориентация"
    '''
    return df.sort_values(by='orientation')


def draw_gistagram(df: pd.DataFrame, save_path: str):
    '''
    Рисует диаграмму распределения "ориентации" среди всех изображений и рисует диаграмму
    '''
    data = df['orientation']
    plt.hist(data, bins=30, edgecolor='black')
    plt.xlabel('Orientation')
    plt.ylabel('Count')
    plt.title('Distribution of orientations')
    plt.savefig(save_path)
    plt.show()


def main():
    args = argument_parsing()
    table_path = args[0]
    gist_path = args[1]

    print('PURE DATAFRAME')
    df = pd.read_csv('results.csv', names=['ABSOLUTE PATH', 'RELATIVE PATH'])
    print(df)

    df['orientation'] = df['ABSOLUTE PATH'].apply(which_orientation)
    print('DATAFRAME with \'orientation\' column')
    print(df)

    df = sort_by_orientation(df)
    print('DATAFRAME SORTED BY \'orientation\'')
    print(df)

    print('DATAFRAME FILTERED BY \'orientation\' == \'horizontal\'')
    df2 = df[df['orientation'] == 'horizontal']
    print(df2)

    draw_gistagram(df, gist_path)

    df.to_csv(table_path, index=False)


if __name__ == '__main__':
    main()
