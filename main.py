from icrawler.builtin import GoogleImageCrawler

import user_ask


def main() -> None:
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': 'images'},
        api_key='ВАШ_API_КЛЮЧ',  # ← замените на ваш ключ
        search_engine_id='ВАШ_SEARCH_ENGINE_ID'  # ← замените на ID движка
    )
    filters = dict(date=((2017, 1, 1), (2017, 11, 30)))
    flickr_crawler = GoogleImageCrawler(storage={'root_dir': 'images'})
    flickr_crawler.crawl(keyword='bear', max_num=10)


if __name__ == "__main__":
    main()
