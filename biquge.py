# -*-coding:utf-8-*-
from DrissionPage import SessionPage
from urllib.parse import urljoin
from tqdm import tqdm


def get_conetent(url):
    chapter_page = SessionPage()
    chapter_page.get(url, verify=False)
    return chapter_page('#content').text


def main():
    url = 'https://www.xbiqugew.com/book/36327/'
    page = SessionPage()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    page.get(url, verify=False)
    chapters = page.s_ele('#list').eles('t:dd')
    chapter_arr = list()
    for chapter in chapters:
        try:
            href = chapter('t:a').inner_ele.attrib['href']
        except:
            continue
        if '第一章' not in chapter.text and not chapter_arr:
            continue
        chapter_arr.append((chapter.text, urljoin(url, href)))
    for title, path in tqdm(chapter_arr):
        try:
            content = get_conetent(path)
        except:
            continue
        with open('诡秘之主.txt', 'a', encoding='utf-8') as f:
            f.write(title)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
        pass


if __name__ == '__main__':
    main()
