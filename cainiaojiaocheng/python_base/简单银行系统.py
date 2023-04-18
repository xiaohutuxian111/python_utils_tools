"""
@FileName：简单银行系统.py
@Author：stone
@Time：2023/4/18 11:17
@Description:
"""

means = {"balance": 0, "financial_management": 0, "debt": 0}
loan = 0
rate = 0
pay = 0
investment = 0
annual_rate = 0


def balance():
    total = means["balance"] + means["financial_management"]
    print("你的资产的总额:%.2f" % total)
    print("你的资产明细:")
    print("           存款：%.2f" % means["balance"])
    print("           理财：%.2f" % means["financial_management"])
    print("           负债：%.2f" % means["debt"])


def init():
    print("亲输入你要选择的操作")
    print('''以下为可办理的业务：
                1. 查询资产
                2. 存款
                3. 取款
                4. 计算复利
                5. 计算贷款
                6. 计算未来资产
                q. 退出''')


def saving(amount):
    global means
    if amount < 0:
        print("存款金额不可小于0！")
    else:
        means["balance"] += amount
        print("已存款: %.2f" % amount)
        print("当前余额：%.2f 元" % means["balance"])


def draw_money(drawing):
    global means
    if drawing < 0:
        print("取款金额不可小于0")
    elif drawing > means["balance"]:
        print("取款金额不可超过余额！")
    else:
        means["balance"] -= drawing
        print("已取款: %.2f 元" % drawing)
        print("当前余额： %.2f 元" % means["balance"])


def fixed_investment(investment, annual_rate, years):
    global means
    inv = investment * 12
    a_rate = annual_rate / 100
    if a_rate == 0:
        expected = 0
    else:
        expected = inv * (1 + a_rate) * (pow((1 + a_rate), years) - 1) / a_rate
    print("定投的预期收入为 %.2f" % expected)
    means["financial_management"] = expected
    return expected


def loans(loan, rate, pay, years):
    global means
    if pay < (loan - pay) * rate:
        print("你是还不完的")
    else:
        if years == 0:
            count = 0
            while loan > 0:
                loan -= pay
                loan *= (1 + rate)
                count += 1
            print("将在%d年后还完贷款" % count)
        else:
            for _ in range(years):
                loan -= pay
                if loan == 0:
                    break
                else:
                    loan *= (1 + rate)
                    print("你现在的负债是:%.2f" % loan)
            return loan


def future(years):
    income = fixed_investment(investment, annual_rate, years)
    debt = loans(loan, rate, pay, years)
    captial = means["balance"] + income - debt
    print("你第%i年的总资产有:%.3f" % (years, captial))




def run():
    init()
    while True:
        chose = input("请输入序号：").strip()
        if chose == '1':
            balance()
        elif chose == '2':
            inc = float(input("请输入要存款的金额:").strip())
            saving(inc)
        elif chose == "3":
            dec = float(input("请输入要取款的金额:").strip())
            draw_money(dec)
        elif chose == "4":
            investment = float(input("请输入每月的定投金额: "))
            annual_rate = float(input("请输入年收益率: "))
            years = int(input("请输入定投期限(年): "))
            if investment <= 0 or annual_rate <= 0 or years <= 0:
                print("输入数据有误")
            else:
                meney = fixed_investment(investment, annual_rate, years)
            print("最终收获：%.2f 元" % meney)
        elif chose == "5":
            loan = float(input("请输入当前贷款："))
            rate = float(input("请输入年利率："))
            pay = float(input("请输入每年还款："))
            if loan <= 0 or rate <= 0 or pay <= 0:
                print("输入的数据有误")
            else:
                loans(loan, rate, pay, 0)
        elif chose == "6":
            years = int(input("希望查询多少年后的存款状况: "))
            future(years)
        elif chose == "q":
            print("欢迎下次光临")
            break
        else:
            print("你输入的命令有误,请重新输入")


if __name__ == '__main__':
    run()

run()
