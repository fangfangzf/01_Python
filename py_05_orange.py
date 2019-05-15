# 1. 定义橘子的单价
price = 8.5

# 2. 挑选橘子
weight = 7.5

# 3. 计算付款金额
money = weight * price

# 4. 只要买橘子，就返回 5 块钱，并没有创建新的money变量
money = money - 5

# 进行调试可以看到内存中存储的变量生命周期
print(money)
