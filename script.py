money = 100000
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
list_per_cent = []
for i_number in per_cent:
    list_per_cent.append(round((money * per_cent[i_number])*(365/365)/100))
print(list_per_cent)
print(f"Максимальная сумма, которую вы можете заработать - {max(list_per_cent)}")
