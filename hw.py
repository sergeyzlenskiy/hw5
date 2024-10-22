import csv
import json

# Открываем файл с покупками (формат .txt) и создаем словарь покупок
purchase_log = {}
with open('purchase_log.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        # Парсим строку как JSON
        purchase_data = json.loads(line.strip())
        user_id = purchase_data['user_id']
        category = purchase_data['category']
        purchase_log[user_id] = category

# Открываем файл визитов и создаем файл с результатами
with open('visit_log.csv', mode='r', encoding='utf-8') as visit_file, open('funnel.csv', mode='w', encoding='utf-8', newline='') as funnel_file:
    reader = csv.DictReader(visit_file)
    fieldnames = ['user_id', 'source', 'category']  # Поля для записи в новый файл
    writer = csv.DictWriter(funnel_file, fieldnames=fieldnames)
    
    # Записываем заголовок в файл funnel.csv
    writer.writeheader()

    # Обрабатываем построчно файл визитов
    count = 0
    for row in reader:
        user_id = row['user_id']
        # Если для пользователя есть покупка, записываем его в funnel.csv
        if user_id in purchase_log:
            row['category'] = purchase_log[user_id]
            writer.writerow(row)
            count += 1

print(f"Файл funnel.csv успешно создан. Количество записанных строк: {count}")