from icrawler.builtin import GoogleImageCrawler

import user_ask as ua


def main() -> None:
    print('Сколько изображений нужно скачать в каждом периоде? ')
    n = ua.ask_natural()
    periods = ua.ask_info()
    for i in range(len(periods)):
        google_crawler = GoogleImageCrawler(
            storage={'root_dir': 'results/'+str(i)},
            api_key='ВАШ_API_КЛЮЧ',
            cse_id='32d119033722e4c0d'
        )
        filters = dict(date=(periods[i].first_date, periods[i].second_date))
        google_crawler.crawl(keyword='bear', filters=filters,
                             max_num=(n/len(periods)))


if __name__ == "__main__":
    main()
