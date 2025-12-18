import argparse

from icrawler.builtin import GoogleImageCrawler

import annotation
import user_ask as ua


def argument_parsing() -> list[str]:
    """
    Разделение аргументов, введённых пользователем в консоли
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('save_path', type=str, help='path to save photo')
    parser.add_argument('annotation_path', type=str,
                        help='path to save annotation')
    args = parser.parse_args()
    return [args.save_path, args.annotation_path]


def main() -> None:
    argparse = argument_parsing()
    res_path = argparse[0]
    ann_path = argparse[1]
    '''
    print('Сколько изображений нужно скачать в каждом периоде? ')
    n = ua.ask_natural()
    periods = ua.ask_info()
    for i in range(len(periods)):
        google_crawler = GoogleImageCrawler(
            feeder_threads=2,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': res_path+'/'+str(i)},
        )
        filters = dict(date=(periods[i].first_date, periods[i].second_date))
        google_crawler.crawl(keyword='bear', filters=filters,
                             max_num=(n/len(periods)))
    '''
    annotation.create_annotation_csv(
        'result', ann_path+'annotation.csv', base_dir='.')


if __name__ == "__main__":
    main()
