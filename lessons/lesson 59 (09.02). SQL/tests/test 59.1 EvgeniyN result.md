Вопросы с выбором варианта: 42/100%  
Вопросы с текстовыми ответами: 0/0%  
# Вопрос 1. Тема: Основы SQL
  
**1. Какая команда используется для извлечения всех записей из таблицы в SQL?**
  
Варианты ответов:
1) SELECT all FROM table_name;
2) SELECT 1 FROM table_name;
3) SELECT FROM table_name;
4) ✅ SELECT * FROM table_name;
  
### ИИ анализ
Команда `SELECT * FROM table_name;` является стандартным синтаксисом SQL для выбора всех столбцов из указанной таблицы.  Символ `*` — это специальный оператор, обозначающий "все столбцы".  Другие варианты либо используют несуществующий синтаксис, либо выбирают конкретные значения, а не все записи.  

# Вопрос 2. Тема: Основы SQL
  
**2. Как ограничить выборку по конкретному условию?**
  
Варианты ответов:
1) SELECT * FROM table_name WHERE condition;
2) ❌ SELECT * FROM table_name ORDER BY condition;
3) SELECT * WHERE condition FROM table_name;
4) SELECT WHERE condition FROM table_name;
  
### ИИ анализ
Для фильтрации записей по условию в SQL используется ключевое слово `WHERE`.  Правильный синтаксис — `SELECT * FROM table_name WHERE condition;`.  Вариант с `ORDER BY` предназначен для сортировки, а не фильтрации, а остальные варианты нарушают правильный порядок предложений в SQL-запросе.  

# Вопрос 3. Тема: Основы SQL
  
**3. Как отсортировать результаты по убыванию значения в столбце age?**
  
Варианты ответов:
1) ❌ SELECT * FROM table_name WHERE age ORDER BY DESC;
2) SELECT * ORDER BY age FROM table_name;
3) SELECT * FROM table_name ORDER BY age DESC;
4) SELECT * FROM table_name ORDER BY DESC age;
  
### ИИ анализ
Для сортировки по убыванию используется конструкция `ORDER BY column_name DESC`.  Ключевое слово `DESC` должно следовать после имени столбца.  Правильный ответ — `SELECT * FROM table_name ORDER BY age DESC;`.  В выбранном варианте отсутствует имя столбца для `ORDER BY`, а в других нарушен порядок предложений или ключевых слов.  

# Вопрос 4. Тема: Основы SQL
  
**4. Как выбрать записи, где age меньше 30 или salary больше 50000, и отсортировать их по name?**
  
Варианты ответов:
1) ❌ SELECT * FROM table_name WHERE age < 30 AND salary > 50000 ORDER BY name;
2) SELECT * FROM table_name WHERE age < 30 OR salary > 50000 name;
3) SELECT * FROM table_name WHERE age < 30 OR salary > 50000 ORDER BY name;
4) SELECT * FROM table_name ORDER BY age < 30 OR salary > 50000, name;
  
### ИИ анализ
Для выполнения условия "ИЛИ" в SQL используется оператор `OR`.  Правильный запрос должен содержать `WHERE age < 30 OR salary > 50000`, а затем `ORDER BY name`.  Выбранный вариант использует `AND`, что означает "И", что не соответствует условию задачи.  Правильный синтаксис представлен в третьем варианте ответа.  

# Вопрос 5. Тема: Основы SQL
  
**5. Как выбрать записи, где salary больше 50000 и age больше 25?**
  
Варианты ответов:
1) SELECT * FROM table_name WHERE salary > 30000, age > 25;
2) ✅ SELECT * FROM table_name WHERE salary > 30000 AND age > 25;
3) SELECT * FROM table_name WHERE salary > 30000 NOT age > 25;
4) SELECT * FROM table_name WHERE salary > 30000 OR age > 25;
  
### ИИ анализ
Для одновременного выполнения двух условий в SQL используется логический оператор `AND`.  Правильный синтаксис — `WHERE salary > 30000 AND age > 25`.  Использование запятой или оператора `OR` неверно, так как они либо вызовут ошибку, либо изменят логику запроса на "ИЛИ".  Выбранный вариант является корректным.
