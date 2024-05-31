# 公式サイトからpdfリンク一覧取得
def get_urls():
    import requests
    from bs4 import BeautifulSoup
    from lxml import html

    html = requests.get('http://sasp.mapion.co.jp/b/mandai/info/192/')
    soup = BeautifulSoup(html.text, 'html.parser')
    lxml_data = html.fromstring(str(soup))
    # ★以下は実際のHTML構成に合わせて実装する
    flyer_list = lxml_data.xpath('//*[@id="MapiContainer"]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td')
    print(flyer_list)
    # url_list = []
    # for flyer in flyer_list:
    #     # 日付
    #     date = flyer.find('div', {'class': 'sale'}).find('a').get_text(strip=True).replace(' ', '').replace('（', '(').replace('）', ')')

    #     # PDF
    #     url_info = {}
    #     url_info['date'] = date
    #     url_info['url'] = flyer.find('a', {'title': 'PDF'})['href']
    #     url_list.append(url_info)

    # return url_list

get_urls()