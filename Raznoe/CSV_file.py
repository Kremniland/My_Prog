import csv

# Чтение .csv файла как списка из строк:
# with open('My_CSV.csv', 'r') as f:
#     reader = csv.reader(f)
#     print(reader.line_num)
#     print(reader.dialect)
#     for i in reader:
#         print(i)

# Чтение .csv файла как словаря:
# with open('My_CSV.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for i in reader:
#         print(i)

# Создание .csv файла по строкам:
# with open('output.csv', 'w') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_ALL)   # quoting=csv.QUOTE_ALL - обрамление элемента
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['1', '2', '3'])

# Записываем словарь:
# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# Чтение как словаря:
# with open('names.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'])
