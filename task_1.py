money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
MONTH = 0
MY_MONEY = money_capital + salary
while MY_MONEY > spend:
    MY_MONEY = MY_MONEY - spend
    spend = spend + spend*increase
    MY_MONEY += salary
    MONTH += 1
print("Количество месяцев, которое можно протянуть без долгов:", MONTH)
