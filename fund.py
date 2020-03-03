from pingan import Fund
from JsonParser import loadJsonFile


if __name__ == '__main__':
    # 从文件里获取
    funds_code = ['001593', '007874', '161725', '519005', '003096', '007301', '000878', '501047', '005919', '005777',
                  '000008', '377240', '005110', '320007', '005911', '003853', '161028', '165525', '003017', '400015',
                  '001595', '002147', '167301']
    # funds_code = ['001593', '007874']

    funds = []
    for code in funds_code:
        fund = Fund(code)
        fund.print_base()
        if fund.stocks:
            funds.append(fund)
