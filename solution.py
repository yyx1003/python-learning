total_cost = float(input())                   # total_cost为当前房价
annual_salary = float(input())                # 年薪
portion_saved = float(input()) / 100          # 月存款比例，输入30就为30%
semi_annual_raise = float(input()) / 100      # 输入每半年加薪比例，输入7转化为7%

portion_down_payment = 0.3                    # 首付比例，浮点数
down_payment = portion_down_payment * total_cost   # 首付款
print(f'首付 {down_payment:.2f} 元')

current_savings = 0.0                         # 存款金额，从0开始
number_of_months = 0

# 补充你的代码，计算月工资，计算月存款
monthly_salary = annual_salary / 12
monthly_deposit = monthly_salary * portion_saved

# 补充你的代码，计算多少个月才能存够首付，结果为整数，不足1月按1个月计算，即向上取整
while current_savings < down_payment:
    number_of_months += 1

    # 月初：先结算上一个月存款的利息（年利率2.25%，按月计息）
    current_savings += current_savings * 0.0225 / 12
    # 月初：发工资，存入当月应存的部分
    current_savings += monthly_deposit
    # 每满6个月（第7、13、19…个月初）涨一次薪
    if number_of_months % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
        monthly_deposit = monthly_salary * portion_saved

    # 每满12个月，输出一次月末存款（千分位、不保留小数）
    if number_of_months % 12 == 0:
        print(f'第{number_of_months}个月月末有{current_savings:,.0f}元存款')

print(f'{int(number_of_months)}个月可以存够首付')
