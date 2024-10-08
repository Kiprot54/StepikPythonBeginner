## Порядок книг

Все книги в домашней библиотеке Душнилы, друга Сэма, должны быть обязательно отсортированы по возрастанию:
сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям. Напишите программу, которая проверяет, верно ли отсортированы книги.

На вход вашей программе поступает число <code>n</code>, а затем – <code>n</code> строк, каждая строка представляет собой книгу в следующем формате:

<code><фамилия автора> <инициалы автора>, «<название книги>»</code>

Программа должна вывести сообщение о том, отсортированы ли книги в соответствии с пожеланиями Душнилы.

**Примечание 1.** Обратите внимание, что Душнила игнорирует инициалы автора при сортировке книг.

**Примечание 2.** Книги в наборе могут повторяться.

**Примечание 3.** Будем считать, что фамилия автора состоит из одного слова.

<br>

### *Тестовые данные:*

| Номер теста | Входные данные                                                                                                                                                                                                      | Выходные данные |
|:-----------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
|      1      | 5<br>Гоголь Н.В., «Мертвые души»<br>Гончаров И.А., «Обломов»<br>Пушкин А.С., «Капитанская дочка»<br>Тургенев И.С., «Ася»<br>Тургенев И.С., «Первая любовь»                                                          | YES             |
|      2      | 3<br>Толстой А.Н., «Петр Первый»<br>Толстой А.Н., «Хмурое утро»<br>Толстой Л.Н., «Война и мир»                                                                                                                      | NO              |
|      3      | 4<br>Достоевский Ф.М., «Идиот»<br>Достоевский Ф.М., «Братья Карамазовы»<br>Достоевский Ф.М., «Игрок»<br>Достоевский Ф.М., «Преступление и наказание»                                                                | NO              |
|      4      | 5<br>Гоголь Н.В., «Тарас Бульба»<br>Толстой Л.Н., «Анна Каренина»<br>Толстой Л.Н., «Детство»<br>Толстой Л.Н., «Отрочество»<br>Толстой Л.Н., «Юность»                                                                | YES             |
|      5      | 6<br>Булгаков М.А., «Мастер и Маргарита»<br>Булгаков М.А., «Собачье сердце»<br>Гоголь Н.В., «Шинель»<br>Чехов А.П., «Человек в футляре»<br>Чехов А.П., «Тоска»<br>Шолохов М.А., «Судьба человека»                   | NO              |
|      6      | 8<br>Бунин И.А., «Завтра»<br>Горький М., «Детство»<br>Горький М., «На дне»<br>Островский А.Н., «Гроза»<br>Платонов А.П., «Завтра»<br>Толстой Л.Н., «Детство»<br>Толстой А.Н., «Петр Первый»<br>Тургенев И.С., «Ася» | YES             |
|      7      | 1<br>Короленко В.Г., «В дурном обществе»                                                                                                                                                                            | YES             |
|      8      | 2<br>Толстой Л.Н., «Детство»<br>Горький М., «Детство»                                                                                                                                                               | NO              |
|      9      | 3<br>Горький М., «Детство»<br>Горький М., «На дне»<br>Горький М., «Мать»                                                                                                                                            | NO              |
|     10      | 3<br>Блок А.А., «На железной дороге»<br>Блок А.А., «На лугу»<br>Блок А.А., «На поле Куликовом»                                                                                                                      | YES             |