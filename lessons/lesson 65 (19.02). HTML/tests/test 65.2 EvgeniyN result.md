Вопросы с выбором варианта: 78/78%  
# Вопрос 1. Блок 3. Текстовый контент, ссылки, списки, изображения
  
### Содержание и вопросы

- Как сделать ссылку и какие бывают `href`?
- Чем `ul` отличается от `ol`?
- Зачем нужен `alt` у изображения?
- Как структурировать “карточку” проекта только HTML-ом?

### Материал (лаконично)

- Ссылка это тег `a`. Внутри должен быть текст, по которому понятно, куда ведет ссылка.
- `href` может быть:
  - обычным адресом сайта
  - якорем внутри страницы
  - `mailto:` для письма
- Списки:
  - `ul` когда порядок не важен, например “навыки”
  - `ol` когда это шаги, порядок важен
- Картинка это `img`. `alt` обязателен. Если картинка не загрузится, текст `alt` подскажет, что там должно быть.
- “Карточка” проекта это просто блок. Обычно внутри: заголовок, текст, ссылка.
  
Варианты ответов:
1) ✅ Прочитано
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 2. Практическое задание (Блок 3)
  
### Условия

Добавь контент в `index.html` пошагово:

1. В одной из секций добавь заголовок и под ним список.
2. Заполни список из 5 пунктов.
3. В секции с проектами создай контейнер для карточек.
4. Создай минимум 3 карточки. В каждой карточке сделай:
   - заголовок карточки
   - короткий текст-описание
   - ссылку
5. В шапке добавь изображение-аватар.
6. В подвале сделай блок контактов и добавь минимум 3 ссылки.
7. Проверь, что у всех `img` есть `alt`, а у всех `a` есть `href`.

Проверка:

- Все ссылки кликабельны.
- Все изображения имеют `alt`.

### Псевдокод решения

```text
IN SECTION_B
  CREATE LIST
    ADD LIST_ITEM (REPEAT 5 TIMES)

IN SECTION_C
  CREATE CARDS_CONTAINER
    REPEAT 3 TIMES
      CREATE CARD
        ADD CARD_TITLE
        ADD CARD_TEXT
        ADD CARD_LINK

IN HEADER
  ADD IMAGE_WITH_ALT

IN FOOTER
  CREATE CONTACTS_LIST
    ADD LINK_ITEM (REPEAT 3 TIMES)
END
```

### Если использовал ИИ, обязательные изменения вручную

- Замени один тип списка на другой (например, `ul` на `ol` или наоборот) и объясни почему это подходит.
- Добавь еще одну ссылку с другим типом `href` (например, `mailto:`).

---

**Вставь решение в комментарий ниже:**
  
### Ответ
<!DOCTYPE html>  
<html lang="ru">  
<head>  
<meta charset="UTF-8">  
<meta name="viewport" content="width=device-width, initial-scale=1.0">  
<title>Это просто тестовый сайт</title>  
<link rel="stylesheet" href="styles.css">  
</head>  
<body>  
	<div class="new-style">  
		<div class="avatar">  
            <img src="https://www.shutterstock.com/image-vector/user-avatar-icon-sign-profile-260nw-1145752283.jpg" alt="Аватар пользователя">  
        </div>  
  
		<header>  
			<h1>Главный заголовок этой страницы<h1>  
			<p>Сайт показывает этапы работы с версткой<p>  
			<nav>  
                <a href="#about">О себе</a> |  
				<a href="#goals">Цели</a> |  
				<a href="#hobby">Увлечения</a> |  
				<a href="#contacts">Контакты</a>  
            </nav>  
		</header>  
		<main>  
			<!-- Секция 1 -->  
			<section id="about">  
				<h2>О себе</h2>  
				<p>Меня зовут Евгений, я осваиваю веб-разработку.</p>  
			</section>  
  
			<!-- Секция 2 -->  
			<section id="goals">  
				<h2>Мои цели</h2>  
				<p>Научиться создавать красивые и современные сайты.</p>  
				<h3>Что я планирую достичь в этом году:</h3>  
  
                <ul>  
                    <li>Освоить семантическую верстку HTML5</li>  
                    <li>Выучить CSS и научиться создавать адаптивные макеты</li>  
                    <li>Изучить основы JavaScript</li>  
                    <li>Создать рабочий сайт</li>  
                    <li>Запустить собственный проект</li>  
                </ul>  
  
			</section>  
  
			<!-- Секция 3 -->  
			<section id="hobby">  
				<h2>Мои увлечения</h2>  
				<p>Увлекаюсь изготовлением кожанных изделий из натуральной кожи</p>  
			</section>  
  
  
			<img  
			src="https://photofile.ru/wp-content/uploads/2024/04/1684700436047.png"  
			alt="Пример картинки"  
			width="778"  
			height="780"  
			/>  
  
			<!-- ПОДВАЛ -->  
			<footer>  
				<section id="contacts">  
				<ul class="contacts-list">  
  
                <li><a href="https://github.com/KorolevEvgeniy" target="_blank">GitHub</a></li>  
  
                <li><a href="https://gmail.com" target="_blank">mailto:udjinnk@gmail.com</a></li>  
  
				<li><a href="https://t.me/+789870336621" target="_blank">Telegram</a></li>  
  
				</ul>  
				</section>  
				<p>2026, Все права защищены.</p>  
  
			</footer>  
		</main>  
	</div>  
</body>  
</html>  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Какой HTML-тег используется для создания обычной ссылки на другую страницу?
  
  
Варианты ответов:
1) `div`
2) `p`
3) `img`
4) `span`
5) ✅ `a`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Какой тип списка лучше подходит для раздела “навыки”, где порядок элементов не имеет значения?
  
  
Варианты ответов:
1) `form`
2) `table`
3) `nav`
4) ✅ `ul`
5) `ol`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Зачем нужен атрибут `alt` у тега изображения `img`?
  
  
Варианты ответов:
1) Для изменения размера картинки
2) Для создания отступов
3) ✅ Для текстового описания картинки
4) Для выравнивания текста
5) Для подключения CSS
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 6. Какое значение атрибута `href` используется для создания ссылки, которая открывает почтовую программу?
  
  
Варианты ответов:
1) `ftp:`
2) `http:`
3) `css:`
4) `file:`
5) ✅ `mailto:`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 7. Какие элементы обычно должны быть внутри “карточки проекта” на странице-визитке?
  
  
Варианты ответов:
1) Только картинка без текста
2) Только `meta` теги
3) Только `script` код
4) Только таблица с данными
5) ✅ Заголовок, текст, ссылка
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 8. Что нужно проверить после добавления ссылок и изображений на страницу?
  
  
Варианты ответов:
1) Что нет `footer`
2) Что `head` пустой
3) Что нет `section`
4) Что нет `main`
5) ✅ Что все ссылки имеют `href`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 9. Какое главное требование к тексту внутри ссылки для удобства пользователей?
  
  
Варианты ответов:
1) Чтобы он был на одной букве
2) ✅ Чтобы он был понятным
3) Чтобы он был скрыт стилями
4) Чтобы он был пустым
5) Чтобы он был только цифрами
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
