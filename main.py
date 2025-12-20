import argparse

from icrawler.builtin import BingImageCrawler

import annotation
import iterator


class SizeInterval:
    def __init__(self, min_width: int, min_height: int):
        self.min_width = min_width
        self.min_height = min_height


def argument_parsing() -> list[str]:
    """
    Разделение аргументов, введённых пользователем в консоли
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('sp', type=str, help='path to save photo')
    parser.add_argument('ap', type=str,
                        help='path to save annotation')
    parser.add_argument('nfe', type=int,
                        help='how many photo download to each period?')
    parser.add_argument('ints', nargs='+', type=str)
    args = parser.parse_args()
    return [args.sp, args.ap, args.nfe, args.ints]


# Диапазоны размеров!

def main() -> None:
    argparse = argument_parsing()
    res_path = argparse[0]
    ann_path = argparse[1]
    num_for_each = argparse[2]
    data = argparse[3]
    
    if (len(data) % 2 != 0):
        raise ValueError
    intervals = list()
    for i in range(0, len(data), 2):
        intervals += [SizeInterval(data[i], data[i+1])]

    for interv in intervals:
        bing_crawler = BingImageCrawler(storage={
                                        'root_dir': res_path+'/larger than ' + str(interv.min_width)+' '+str(interv.min_height)})
        filters = dict(size=str('>'+interv.min_width+'x'+interv.min_height))
        bing_crawler.crawl(keyword='bear', filters=filters,
                           offset=0, max_num=num_for_each)
    
    annotation.create_annotation_csv(res_path, ann_path)

    print('Iterator demonstration')
    for line in iterator.FileIterator(ann_path):
        print(line)


if __name__ == "__main__":
    main()
