money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
current_money = money_capital
current_spend = spend

while current_money + salary >= current_spend:

    current_money = current_money + salary - current_spend
    current_spend *= (1 + increase)
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
