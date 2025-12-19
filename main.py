import argparse

from icrawler.builtin import BingImageCrawler

import annotation


class SizeInterval:
    def __init__(self, min_width: int, min_height: int):
        self.min_width = min_width
        self.min_height = min_height


def argument_parsing() -> list[str]:
    """
    Разделение аргументов, введённых пользователем в консоли
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('save_path', type=str, help='path to save photo')
    parser.add_argument('annotation_path', type=str,
                        help='path to save annotation')
    parser.add_argument('number_of_photo_for_each', type=int,
                        help='how many photo download to each period?')
    parser.add_argument('intervals', nargs='+', type=str)
    args = parser.parse_args()
    return [args.save_path, args.annotation_path, args.number_of_photo_for_each, args.intervals]


# Диапазоны размеров!

def main() -> None:
    '''
    argparse = argument_parsing()
    res_path = argparse[0]
    ann_path = argparse[1]
    num_for_each = argparse[2]
    data = argparse[3]
    print(data)

    if (len(data) % 2 != 0):
        raise ValueError
    intervals = list()
    for i in range(0, len(data), 2):
        intervals += [SizeInterval(data[i], data[i+1])]

    for interv in intervals:
        bing_crawler = BingImageCrawler(storage={
                                        'root_dir': 'results/larger than ' + str(interv.min_width)+' '+str(interv.min_height)})
        filters = dict(size=str('>'+interv.min_width+'x'+interv.min_height))
        bing_crawler.crawl(keyword='bear', filters=filters,
                           offset=0, max_num=num_for_each)
    '''
    annotation.create_annotation_csv('results', 'results.csv')


if __name__ == "__main__":
    main()
