# ponosik.

## пример юзания
```py
mongo = KasMongo("username", "password", "cluster", "database", "collection")

# Вставка данных
mongo.insert("name", "Alice")

# Поиск одного документа
print(mongo.find("name", "Alice"))

# Поиск всех документов
print(mongo.find_all())

# Обновление документа
mongo.update("name", "Alice", "Bob")

# Удаление документа
mongo.delete("name", "Bob")

# Подсчет документов
print(mongo.count_documents())

# Получение уникальных значений
print(mongo.distinct("name"))

# Закрытие подключения
mongo.close()
```
