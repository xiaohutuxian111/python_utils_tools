"""
@FileName：generateTools.py
@Author：stone
@Time：2023/3/21 13:26
@Description：生成测试工具类
"""
import json
import random
import datetime
from functools import reduce

from faker import Faker


class GenerateTools():
    """生成测试工具类"""
    faker = Faker("zh_CN")

    def __init__(self, json_path='./AdministrativeAreaCode.json'):
        self.json_path = json_path
        self.address_info = random.choice(self.read_json())

    def read_json(self):
        """将区域码和地址在json中读取并以列表的形式返回"""
        with open(self.json_path, encoding='utf-8') as f:
            area_code_dict = json.load(f)
        # 将地址中的县级和区级解析
        code_lis = area_code_dict['province']
        result = []
        for ele_dic in code_lis:
            address = ""
            address = address.join(ele_dic["name"])
            # 当前市级单位下没有区
            if "city" in ele_dic:
                for city_item in ele_dic['city']:
                    city_address = address + city_item["name"]
                    # 针对直辖市下仅有一个县,数据类型不一致
                    if "county" in city_item:
                        if isinstance(city_item['county'], dict):
                            lis = []
                            lis.append(city_item['county'])
                            city_item['county'] = lis
                        for county_item in city_item['county']:
                            temp = city_address + county_item['name']
                            zip = county_item['zip']
                            result.append((temp, zip))
                    else:
                        temp = city_address + city_item['name']
                        zip = county_item['zip']

                        result.append((temp, zip))
            else:
                temp = address + ele_dic['name']
                zip = ele_dic['zip']
                result.append((temp, zip))

        return result

    def generate_IdCard(self):
        """生成用户身份证号"""
        address_code = self.address_info[1]
        date_str = self.get_whole_year()
        sex_str = str(random.randint(0, 1000)).zfill(3)
        id_str = address_code + date_str + sex_str
        sum_code = 0
        for ele in id_str:
            sum_code += int(ele)
        id_code = sum_code % 11
        if id_code == 10:
            id_code = "X"
        return id_str + str(id_code)

    def get_whole_year(self):
        year = random.randint(1900, 2050)
        """获取一年中任意一天"""
        begin = datetime.date(year, 1, 1)
        now = begin
        end = datetime.date(year, 12, 31)
        delta = datetime.timedelta(days=1)
        days = []
        while now <= end:
            days.append(now.strftime("%Y%m%d"))
            now += delta
        return random.choice(days)

    def generate_user_name(self):
        """生成用户名"""
        return self.faker.name()

    def generate_address(self):
        """生成用户地址"""
        return self.address_info[0]

    def generate_telephone_number(self):
        """生成手机号"""
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数字
        third = {3: random.randint(0, 9),
                 4: [5, 7, 9][random.randint(0, 2)],
                 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                 7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                 8: random.randint(0, 9),
                 }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)

        return "1{}{}{}".format(second, third, suffix)

    def get_user_info(self):
        user_name = self.generate_user_name()
        address = self.generate_address()
        phone = self.generate_telephone_number()
        id_card = self.generate_IdCard()
        info_dict = {'name': user_name, 'address': address, 'phone': phone, 'id_card': id_card}
        return info_dict


if __name__ == '__main__':
    p = GenerateTools()
    print(p.get_user_info())
