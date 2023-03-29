"""
@FileName：generateTools.py
@Author：stone
@Time：2023/3/21 13:26
@Description：生成测试工具类
"""

from faker import Faker


class GenerateTools():
    """生成测试工具类"""
    faker = Faker("zh_CN")

    @staticmethod
    def generate_IdCard(self, max_age=150):
        """生成用户身份证号"""
        pass

    def generate_user_name(self):
        """生成用户名"""
        return self.faker.name()

    def generate_address(self):
        """生成用户地址"""
        return self.faker.address()

    @staticmethod
    def generate_telephone_number(number_length=11):
        """生成手机号"""
        pass


if __name__ == '__main__':
    p = GenerateTools()
    p.generate_user_name()
    print(p.generate_address())
