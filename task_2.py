salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
i = 0
PODUSHKA = 0
while i < months:
    if i == 0:
        PODUSHKA = spend-salary
    else:
        PODUSHKA = PODUSHKA + spend - salary
    spend = spend + spend*increase
    i += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(PODUSHKA))
