# -*- coding: utf-8 -*-
# --------------------------------------
# Author:waitig.com
# Date:2016-04-01
# Desc:自动下载Tumblr用户所有视频的脚本
# --------------------------------------
# import getopt
import wget
import re, os, requests, thread, json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


# ----------- 爬取tumblr图片和视频 -----------
class TumblrClass:
    def __init__(self, TumloadClass):
        self.clear_video = 0
        self.clear_img = 0
        self.img_path = ''
        self.video_path = ''
        self.index_url = ''
        self.curPage = 1
        self.isVIP = 0
        self.videoNum = 0
        self.isSave = 0
        self.exitIt = 0
        self.video_url_file = ''
        self.img_url_file = ''
        self.chkUrl = 'http://check.waitig.com/software/tumload.php'
        self.uid = ''
        self.UI = None
        self.TumloadClass = TumloadClass
        self.headers = {
            'Host': self.index_url.replace('http://', ''),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': self.index_url,
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }
        self.se = requests.Session()

    def set_headers(self, reUrl):
        self.headers = {
            'Host': self.index_url.replace('http://', '').strip('/'),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': reUrl,
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }

    def set_uid(self, uid):
        self.uid = uid

    def setUIClass(self, UI):
        self.UI = UI

    def log(self, logs):
        self.UI.log(logs)

    def setVideoNum(self, num):
        self.UI.setVideoNum(num)

    def insertDownloadUrl(self, url):
        self.UI.insertDownloadUrl(url)

    def setVIP(self, isVIP):
        self.isVIP = isVIP
        self.TumloadClass.setVIP(isVIP)

    def exit(self):
        self.exitIt = 1

    def reset(self):
        self.clear_video = 0
        self.clear_img = 0
        self.img_path = ''
        self.video_path = ''
        self.index_url = ''
        self.curPage = 1
        self.videoNum = 0
        self.isSave = 0
        self.exitIt = 0
        self.video_url_file = ''
        self.img_url_file = ''

    def get_blogs_in_file(self, fileName):
        blogList = []
        inFile = open(fileName, 'r')
        for line in inFile:
            blogList.append(line)
        return blogList

    def get_img_urls(self, text):
        img_urls = []
        return img_urls

    def get_video_urls(self, text):
        video_urls = re.findall('(?P<video_urls>https://www.tumblr.com/video/[^/]*?/\d+/\d+/)', text)
        return video_urls

    def get_video_files(self, url):
        url = url.strip('/')
        self.log('Start to deal video url : ' + url)
        # -----------------------------------------------------------
        self.set_headers(url)
        self.headers = {
            'Host': 'www.tumblr.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        Reslut = self.se.get(url, headers=self.headers)
        sourceUrl = ''
        sourceUrls = re.findall('src=\"(?P<video_urls>https://www.tumblr.com/video_file/\d+/[^\"]*?)\"', Reslut.text)
        if (sourceUrls != []):
            sourceUrl = sourceUrls[0]
        SourceType = ''
        SourceTypes = re.findall('type=\"video/(?P<vide_type>[^\"]*?)\"', Reslut.text)
        if (SourceTypes != []):
            SourceType = SourceTypes[0]
        sourceUrl = re.sub('https://www.tumblr.com/video_file/\d+/', '', sourceUrl)
        sourceUrl = sourceUrl.replace('/', '_')
        sourceUrl = 'https://vt.tumblr.com/' + sourceUrl
        trueUrl = sourceUrl + '.' + SourceType
        self.log('True url : ' + trueUrl)
        return trueUrl

    def save_video_file(self, url, path):
        url = self.get_video_files(url)
        aHref = '<a href="' + url + '">' + url + '</a><br/>\n'
        self.video_url_file.write(aHref)
        self.video_url_file.flush()
        self.insertDownloadUrl(url)

        if (self.isSave == 1):
            self.log('Start to download video file : ' + url)
            fileName = url.replace('https://vt.tumblr.com/', '')
            tmp_fileName = '_' + fileName
            if (os.path.exists(path) == False):
                os.makedirs(path)
            if (os.path.exists(path + fileName) and self.clear_video == 0):
                self.log('The video file : [' + fileName + '] exists! skipped!')
                return
            self.headers = {
                'Host': 'vt.tumblr.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }
            # ---------wget-----------------------
            self.log('Downloading... method=wget')
            result = wget.download(url, out=path + tmp_fileName)
            os.rename(path + tmp_fileName, path + fileName)
            print 'Video file downloaded in ' + path + fileName

    def save_img_file(self, url, path):
        self.log('Start to download image file : ' + url)
        fileName = ''
        tmp_fileName = '_' + fileName
        if (os.path.exists(path) == False):
            os.makedirs(path)
        if (os.path.exists(path + fileName) and self.clear_img == 0):
            print 'The Image file : [' + fileName + '] exists! skipped!'
            return
        os.rename(path + tmp_fileName, path + fileName)
        self.log('Image file downloaded in ' + path + fileName)

    def deal_blogs_page(self, url):
        if (self.exitIt):
            print 'exitIt deal_blogs_page'
            return
        self.log('Start to deal url : ' + url)
        self.headers = {
            'Host': (self.index_url.replace('http://', '')).split('/')[0],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': self.index_url,
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }
        try:
            Result = self.se.get(url, headers=self.headers)
        except Exception, ex:
            self.log(str(Exception) + ":" + str(ex))
            return
        text = Result.text
        img_urls = self.get_img_urls(text)
        video_urls = self.get_video_urls(text)
        for img in img_urls:
            self.save_img_file(img, self.img_path)

        for videoUrl in video_urls:
            self.videoNum += 1
            self.setVideoNum(self.videoNum)
            self.save_video_file(videoUrl, self.video_path)
            if (self.videoNum > 10 and self.isVIP == 0):
                self.log('You are not vip ,only can get 10 urls each time!')
                self.insertDownloadUrl('You are not vip ,only can get 10 urls each time!')
                return
        nextUrls = re.findall('href=\"/page/(?P<next>\d+)\"', text)
        if (nextUrls != []):
            nextPage = str(self.curPage + 1)
            if (nextPage in nextUrls):
                nextUrl = self.index_url + 'page/' + nextPage
                self.curPage += 1
                self.deal_blogs_page(nextUrl)
        else:
            self.log('Loading completed ,exited!')
            return

    def deal_save_path(self):
        userNames = re.findall('http://(?P<PATH>[^\.]*?)\.tumblr\.com/', self.index_url)
        userName = ''
        if (userNames != []):
            userName = userNames[0]
        self.img_path = userName + '/img/'
        self.video_path = userName + '/videos/'
        if (os.path.exists(self.video_path) == False):
            os.makedirs(self.video_path)
        self.video_url_file = open(self.video_path + 'video_url.html', 'w')

    def main(self, type, value, isSave):
        self.exitIt = 0
        self.isSave = isSave
        if (type == 1):
            if (re.match('^[http://]', value) == False):
                self.index_url = 'http://' + value.strip('/') + '/'
            else:
                self.index_url = value.strip('/') + '/'
            self.set_headers(self.index_url)
            self.deal_save_path()
            try:
                thread.start_new_thread(self.check_ads, (self.index_url, 0))
            except:
                self.log("Error: unable to start thread[chkUrl]")
            self.deal_blogs_page(self.index_url)
        elif (type == 0):
            urlList = self.get_blogs_in_file(value)
            for url in urlList:
                if (re.match('^[http://]', url) == False):
                    self.index_url = 'http://' + url.strip('/') + '/'
                else:
                    self.index_url = url.strip('/') + '/'
                self.deal_save_path()
                try:
                    self.check_ads(self.index_url, 0)
                except BaseException, e:
                    self.log(str(e))
                    pass
                self.deal_blogs_page(self.index_url)
        return

    def check_ads(self, sourceUrl, init=1):
        headers = {
            'Host': 'check.waitig.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'check.waitig.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }
        postData = {
            'uid': self.uid,
            'tumUrl': sourceUrl,
            'init': str(init)
        }
        try:
            Reslut = self.se.post(self.chkUrl, headers=headers, data=postData)
            text = Reslut.text
            print text
            if (1 == init):
                decodeJson = json.loads(text)
                self.TumloadClass.setAD1(decodeJson['ad1'])
                self.TumloadClass.setAD2(decodeJson['ad2'])
                self.TumloadClass.setAD3(decodeJson['ad3'])
                self.TumloadClass.setTopUrl(str(decodeJson['topUrl']))
                self.setVIP(decodeJson['isVIP'])
        except BaseException, e:
            print(str(e))
            pass

    def __del__(self):
        self.video_url_file.close()

#
# if __name__ == '__main__':
#     tc = TumblrClass()
#     type = ''
#     values = ''
#     isSave = 0
#     if (len(sys.argv) != 3):
#         print 'Input number Error!'
#         print 'python ' + sys.argv[0] + ' -u[url] or -f[fileName] [0/1]'
#         exit()
#     opts, args = getopt.getopt(sys.argv[1:], "hu:f:h:s:")
#     for op, value in opts:
#         if (op == '-u'):
#             type = 1
#             values = value
#         elif (op == '-f'):
#             type = 0
#             values = value
#         else:
#             print 'python ' + sys.argv[0] + ' -u[url] or -f[fileName]  [0/1]'
#             exit()
#     isSave = sys.argv[2]
#     # print isSave
#     tc.main(type, values, isSave)
