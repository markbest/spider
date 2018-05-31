#! /usr/bin/env python
import re


class HtmlParse(object):
    def __init__(self):
        self.urls = []
        self.output = {}

    def parse(self, target_url, html_cont):
        pattern = re.compile(r'<h1 >([^<]*)</h1>')
        titles = pattern.findall(html_cont)
        self.output['url'] = target_url
        self.output['title'] = titles[0]

        pattern = re.compile(r'<a target=_blank href="(/item/[^"]+)">[^<]+</a>')
        urls = pattern.findall(html_cont)
        if len(urls) > 0:
            for url in urls:
                if url not in self.urls:
                    self.urls.append(url)
        return [self.urls, self.output]
