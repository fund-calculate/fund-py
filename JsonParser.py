import json


def loadJsonFile():
    # 打开‘json’的json文件
    f = open('data/json.json', encoding='utf-8')
    # 读文件
    res = f.read()
    # 把json串变成python的数据类型：字典
    data = json.loads(res)
    stocks = data["data"]["stocks"]
    codes = []
    for stock in stocks:
        code = stock["symbol"]
        code = code[1:8]
        codes.append(code)
    print(codes)
    return codes


if __name__ == "__main__":
    codes = loadJsonFile()
    print(codes)
