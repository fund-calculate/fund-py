# 排序
import operator
from data.funds import funds, fund_codes
from Sina.valuation import myThread
from entity.Fund import Fund, print_fund, fund_grouping, print_fund_group

# var hq_str_fu_001593="天弘创业板ETF联接C,14:28:00,0.8203,0.8598,0.8598,-0.4128,-4.5941,2020-02-28";
if __name__ == '__main__':

    # 基金集合
    map = funds()
    # 基金数组
    fund_codes = fund_codes()

    # 多线程
    threads = []
    for thread_code in fund_codes:
        thread = myThread(1, thread_code)
        thread.start()
        threads.append(thread)
    info = []
    for thread in threads:
        thread.join()
        fund = Fund(thread.text)
        info.append(fund)
        # 排序
        info.sort(key=operator.attrgetter('valuation'))

    # 单线程
    # for code in fund_codes:
    #     text = get_fund_by_code(code)
    #     info.append(Fund(text))
    #     # 排序
    #     info.sort(key=operator.attrgetter('valuation'))

    # 打印
    print_fund(info)
    # 分组
    fund_map = fund_grouping(info, map)
    # 分组打印
    print_fund_group(fund_map)