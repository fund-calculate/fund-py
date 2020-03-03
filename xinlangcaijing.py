import requests
# 排序
import operator
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
        print("开始线程：" + self.name)
        self.text = get_fund_by_code(self.code)
        print("退出线程：" + self.name)


class Fund:
    # 基金代码
    code = ''
    # name
    name = ''
    # 估值涨幅
    valuation = 0
    # 日期
    date = ''
    # 时间
    time = ''

    # var hq_str_fu_519005="海富通股票混合,10:45:00,1.3258,1.2580,3.2070,0.3558,5.3895,2020-03-03";
    def __init__(self, text):
        print(text)
        data_text = text[22: len(text) - 3]
        data = data_text.split(',')

        self.code = text[14:20]
        self.name = data[0]
        self.time = data[1]
        self.valuation = float(data[6])
        self.date = data[7]


# 基金集合
def funds():
    map = {}
    # 5G芯片
    map['5G芯片'] = five_g_chip = ['519005', '320007', '005911']
    # 半导体芯片 南方现代教育股票003956 财富成长优选混合001480 银河创新混合519674
    map['半导体芯片'] = semiconductor_chip = ['003956', '001480', '519674']
    # 人工智能半导体 国联安中证全指半导体ETF联接C 007301 诺安和鑫混合002560 融通人工智能指数(LOF)161631
    map['人工智能半导体'] = ai_semiconductor = ['007301', '002560', '161631']
    # 新能源汽车
    map['新能源汽车'] = new_energy_vehicle = ['400015', '161028', '003853']
    # 科技
    map['科技'] = techfin = ['005777', '007874', '377240', '360006']
    # 沪深300
    map['沪深300'] = the_csi_300 = ['110020']
    # 中证500
    map['中证500'] = csi_500 = ['005919', '000008']
    # 中证银行
    map['中证银行'] = under_the_bank = ['001595']
    # 创业板
    map['创业板'] = entrepreneurship = ['001593']
    # 金融证券
    map['金融证券'] = financial_securities = ['501047', '161720']
    # 医疗
    map['医疗'] = medical = ['003096', '000878']
    # 军工
    map['军工'] = military = ['003017']
    # 白酒
    map['白酒'] = liquor = ['161725']
    # 基建
    map['基建'] = infrastructure = ['165525']
    # 保险
    map['保险'] = insurance = ['167301']
    # 债券
    map['债券'] = bond = ['002147']
    # 其他
    map['其他'] = other = ['005110']
    return map


# 打印
def print_fund(info):
    tplt = "{0:^10}\t{1:^35}\t{2:^10}\t{3:^15}\t{4:^10}"
    print(tplt.format("代码", "名称", "今日估值", "日期", "时间"))
    for fund in info:
        txt = tplt.format(fund.code, fund.name, fund.valuation, fund.date, fund.time)
        print(txt)
    print('\n')


# 分组
def fund_grouping(info):
    fund_map = {}
    for fund in info:
        for k, v in map.items():
            fund_grouped_collection = []
            for grouped_collection in v:
                if fund.code == grouped_collection:
                    fund_grouped_collection.append(fund)
            if fund_map.get(k):
                if fund_grouped_collection:
                    fund_map[k] = fund_map.get(k) + fund_grouped_collection
            else:
                fund_map[k] = fund_grouped_collection
    return fund_map


# var hq_str_fu_001593="天弘创业板ETF联接C,14:28:00,0.8203,0.8598,0.8598,-0.4128,-4.5941,2020-02-28";
if __name__ == '__main__':

    map = funds()

    # 基金数组
    funds_code = []
    for k, v in map.items():
        funds_code = funds_code + v

    info = []

    # 多线程
    threads = []
    for thread_code in funds_code:
        thread = myThread(1, thread_code)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
        fund = Fund(thread.text)
        info.append(fund)
        # 排序
        info.sort(key=operator.attrgetter('valuation'))

    # 单线程
    # for code in funds_code:
    #     text = get_fund_by_code(code)
    #     info.append(Fund(text))
    #     # 排序
    #     info.sort(key=operator.attrgetter('valuation'))

    # 打印
    print_fund(info)
    # 分组
    fund_map = fund_grouping(info)

    # 打印分组
    for key in fund_map:
        fund_list = fund_map.get(key)
        gains = 0
        for fund in fund_list:
            gains = gains + fund.valuation
        gains = round(gains / len(fund_list), 4)
        print('========================================================================')
        print('=======================================模块：' + key + '\t涨幅：' + str(gains) + '%')
        print('========================================================================')
        # 打印
        print_fund(fund_list)
