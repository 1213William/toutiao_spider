import requests
import json
import sys


cookies = {
    's_v_web_id': 'a2a4126c8e6ff8d5bb62ebe15bf8bc7c'
}


def complete_url(offset, keyword):
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=%s&keyword=%s' % (offset, keyword)
    return url


def get_html_content(url):
    return requests.get(url, cookies=cookies)


def parse_html(html):
    for i in json.loads(html.content.decode('utf-8'))['data']:
        if 'title' and 'abstract' in i:
            print(i['title'])
            try:
                print('https://www.toutiao.com/a' + i['id'])
            except KeyError as e:
                pass
            print('+' * 100)


def main(keyword):
    for i in range(0, sys.maxsize, 20):
        url = complete_url(i, keyword)
        resp = get_html_content(url)
        parse_html(resp)


if __name__ == '__main__':
    try:
        choice = input('请输入你要搜索的内容:>>').strip()
        main(choice)
    except TypeError as e:
        pass
