## Магические даты

Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними двумя цифрами года.

Напишите функцию <code>is_magic(date)</code>, которая принимает в качестве аргумента
строковое представление корректной даты и возвращает значение <code>True</code>, если дата является магической,
или <code>False</code> в противном случае.

***Примечание.*** Приведённый ниже код:

<pre><code>print(is_magic('10.06.1960'))
print(is_magic('11.06.1960'))
</code></pre>

должен выводить:

<pre>
True
False
</pre>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные | Выходные данные |
|:-----------:|----------------|-----------------|
|      1      | 10.06.1960     | True            |
|      2      | 15.03.1945     | True            |
|      3      | 03.11.2033     | True            |
|      4      | 03.11.2032     | False           |
|      5      | 15.12.1234     | False           |
|      6      | 10.09.1990     | True            |