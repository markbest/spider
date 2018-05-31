#! /usr/bin/env python

import html_download
import html_output
import html_parse
import url_manage


class SpiderMain(object):
    def __init__(self):
        self.url_manage = url_manage.UrlManage()
        self.html_download = html_download.HtmlDownload()
        self.html_parse = html_parse.HtmlParse()
        self.html_output = html_output.HtmlOutPut()

    def run(self, url):
        self.url_manage.add_new_url(url)

        count = 1
        while self.url_manage.has_new_url():
            new_url = self.url_manage.get_new_url()
            html_cont = self.html_download.download(new_url)
            if html_cont is None:
                print('parse url %s occur error' % new_url)
                continue

            # 返回两个参数，第一个参数是urls，第二个是解析的结果
            parse_rs = self.html_parse.parse(new_url, html_cont)
            if len(parse_rs) == 2:
                self.url_manage.add_new_urls(parse_rs[0])
                self.html_output.output(parse_rs[1])
            else:
                continue
            print('parse %d url success' % count)
            if count > 100:
                break
            count = count + 1


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider = SpiderMain()
    spider.run(root_url)
