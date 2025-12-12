salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
def calculate_money_capital(salary, spend, months, increase):
    total_deficit = 0

    for i in range(months):
        if i > 0:
            spend *= (1 + increase)

        deficit = max(spend - salary, 0)
        total_deficit += deficit

    return round(total_deficit)


result = calculate_money_capital(salary, spend, months, increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {result}")



