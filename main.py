import argparse
import pandas as pd
import cv2


def argument_parsing() -> list[str]:
    """
    Разделение аргументов, введённых пользователем в консоли
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('save_path', type=str, help='path to save table')
    args = parser.parse_args()
    return [args.save_path]


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
    return df.sort_values(by='orientation')


def main():
    print('PURE DATAFRAME')
    df = pd.read_csv('results.csv', names=['ABSOLUTE PATH', 'RELATIVE PATH'])
    print(df)

    df['orientation'] = df['ABSOLUTE PATH'].apply(which_orientation)
    print('DATAFRAME with \'orientation\' column')
    print(df)

    new_df = sort_by_orientation(df)
    print('DATAFRAME SORTED BY \'orientation\'')
    print(new_df)
    
    print('DATAFRAME FILTERED BY \'orientation\' == \'horizontal\'')
    df2 = df[df['orientation'] == 'horizontal']
    print(df2)


if __name__ == '__main__':
    main()
