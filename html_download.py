#! /usr/bin/env python
import urllib3


class HtmlDownload(object):
    def download(self, url):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        http = urllib3.PoolManager()
        resp = http.request('GET', url)
        if resp.status != 200:
            return None
        return resp.data.decode('utf-8')
