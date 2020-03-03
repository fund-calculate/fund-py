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


# 基金数组
def fund_codes():
    funds_code = []
    for k, v in funds().items():
        funds_code = funds_code + v
    return funds_code
