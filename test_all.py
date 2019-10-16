import datetime
import unittest
import json
import validators
from lab_1.main.parser import get_html_page, find_articles, publish_report


class TestCrawler(unittest.TestCase):
    def setUp(self):
        page = open("lab_1/main/test/vc.html", "r", encoding="UTF-8")
        page_content = page.read()
        page.close()
        self.url = 'https://vc.ru/'
        self.html = page_content
        self.array = ['Как Slack-боты убили дашборды',
                      'Как за десять дней заработать $60 тысяч и получить бесценные инсайты о продукте',
                      'Офис JetBrains в Санкт-Петербурге',

                      'Факторы ранжирования медицинских сайтов по коммерческим запросам',
                      'Структура SDR-отдела в сервисной ИТ-компании',

                      'Откуда не ждали: три финтех-стартапа из Африки, Южной Америки и Юго-Восточной Азии',

                      'Языковой сервис Duolingo запустит приложение для обучения детей родному языку \n\n\nМатериал редакции',
                      'Как айтишники 20 километров проплыли',

                      'Лекторий vc.ru в Москве: как сообщество и продукт развивают друг друга \n\n\nМатериал редакции',
                      'Собери сам: как магазин мебели выстроил экосистему аналитики в одном окне',
                      'Правила создания лучших форм',

                      'Власти России разрешат продавцам на экспорт получать возврат НДС без сбора бумажных документов с апреля 2020 года \n\n\nМатериал редакции',

                      'Суд оставил основателя Baring Vostok Майкла Калви под домашним арестом до 13 января 2020 года \n\n\nМатериал редакции',
                      'Три эпичных моментов стартапа: как пройти и выжить',

                      'Сеть книжных магазинов «Республика» сменила гендиректора второй раз за месяц \n\n\nМатериал редакции',

                      '«Яндекс» предложил Avito, ivi, «2ГИС» и другим уладить конфликт из-за мест в поисковой выдаче \n\n\nМатериал редакции',
                      'Бот на проводе: как выбрать кейс и платформу для обзвона (и не разозлить клиента)',
                      'Как мы продаём сайты и SEO в США, часть вторая',
                      'UX-исследования не решат всех ваших проблем',

                      'Продуктовая сеть «Вкусвилл» откроет аптеки в своих магазинах вместе с партнёром \n\n\nМатериал редакции',

                      'Что нового в macOS Catalina: закрытие iTunes, iPad как второй монитор, обновление приложений и «Локатор» \n\n\nМатериал редакции',
                      'Алгоритмы подбора лучших предложений', 'Нормальный текст вакансии',

                      'Чем занимается «белый хакер», как им стать и сколько можно заработать \n\n\nМатериал редакции']

    def test_get_html_page(self):
        self.assertEqual(get_html_page(self.url).status_code, 200)

    def test_find_articles(self):
        self.assertListEqual(find_articles(self.html), self.array)

    def test_file_structure(self):
        creation_date = datetime.datetime.now().strftime("%b %m, %Y, %H:%M")
        result = {"url": self.url,
                  "creationDate": creation_date,
                  "articles": self.array}
        path = "lab_1/articles.json"
        publish_report(path, result)
        with open(path, 'r', encoding="UTF-8") as headers_content:
            content = json.load(headers_content)
        self.assertTrue(validators.url(content["url"]))
        try:
            datetime.datetime.strptime(content["creationDate"], '%b %m, %Y, %H:%M').date()
        except ValueError:
            print('Invalid date!')
        self.assertNotEqual(len(content["articles"]), 0)

    if __name__ == '__main__':
        unittest.main()
