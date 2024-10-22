import csv
import json

purchase_log = {}
with open('purchase_log.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        purchase_data = json.loads(line.strip())
        user_id = purchase_data['user_id']
        category = purchase_data['category']
        purchase_log[user_id] = category

with open('visit_log.csv', mode='r', encoding='utf-8') as visit_file, open('funnel.csv', mode='w', encoding='utf-8', newline='') as funnel_file:
    reader = csv.DictReader(visit_file)
    fieldnames = ['user_id', 'source', 'category']  
    writer = csv.DictWriter(funnel_file, fieldnames=fieldnames)
    
    writer.writeheader()

    count = 0
    for row in reader:
        user_id = row['user_id']
        if user_id in purchase_log:
            row['category'] = purchase_log[user_id]
            writer.writerow(row)
            count += 1

print(f"Файл funnel.csv успешно создан. Количество записанных строк: {count}")