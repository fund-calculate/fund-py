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
        # print(text)
        data_text = text[22: len(text) - 3]
        data = data_text.split(',')

        self.code = text[14:20]
        self.name = data[0]
        self.time = data[1]
        self.valuation = float(data[6])
        self.date = data[7]


# 打印
def print_fund(info):
    tplt = "{0:^10}\t{1:^35}\t{2:^10}\t{3:^15}\t{4:^10}"
    print(tplt.format("代码", "名称", "今日估值", "日期", "时间"))
    for fund in info:
        txt = tplt.format(fund.code, fund.name, fund.valuation, fund.date, fund.time)
        print(txt)
    print('\n')

# 打印分组
def print_fund_group(fund_map):
    for key in fund_map:
        fund_list = fund_map.get(key)
        gains = 0
        for fund in fund_list:
            gains = gains + fund.valuation
        gains = round(gains / len(fund_list), 4)
        print('----------------------------------------------------------------------------------------------------')
        print('|', ('模块：' + key + '\t涨幅：' + str(gains) + '%').center(89), "|")
        print('----------------------------------------------------------------------------------------------------')
        # 打印
        print_fund(fund_list)

# 分组
def fund_grouping(info, map):
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
