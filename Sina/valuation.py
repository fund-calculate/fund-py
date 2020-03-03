import requests
import threading


# http://hq.sinajs.cn/?list=fu_003853 新浪财经基金净值
def get_fund_by_code(code):
    api = 'http://hq.sinajs.cn/?list=fu_' + code
    text = requests.get(api).text
    return text


class myThread(threading.Thread):
    def __init__(self, threadID, code):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = code
        self.code = code

    def run(self):
        self.text = get_fund_by_code(self.code)
