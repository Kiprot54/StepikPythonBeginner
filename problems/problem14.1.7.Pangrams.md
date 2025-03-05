## Панграммы

Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов,
чтобы можно было в одной фразе рассмотреть все глифы.

Напишите функцию <code>is_pangram(text, language)</code>, которая принимает в качестве аргумента строку текста на языке <code>language</code>
и возвращает значение <code>True</code>, если текст является панграммой, или <code>False</code> в противном случае.

***Примечание 1.*** Гарантируйте, что введённая строка содержит только буквы соответствующего алфавита и пробелы.

***Примечание 2.*** Приведённый ниже код:

<pre><code>print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))
</code></pre>

должен выводить:

<pre>
True
True
False
</pre>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные                                                       | Выходные данные |
|:-----------:|----------------------------------------------------------------------|-----------------|
|      1      | Jackdaws love my big sphinx of quartz                                | True            |
|      2      | The five boxing wizards jump quickly                                 | True            |
|      3      | The quick brown fox jumps over the lazy dog                          | True            |
|      4      | Crazy Fredrick bought many very exquisite opal jewels                | True            |
|      5      | jsdfhsadfhkljsad                                                     | False           |
|      6      | Crazy Fredrick bought many very exquisite opal jewel                 | True            |
|      7      | razy Fredrick bought many very exquisite opal                        | False           |
|      8      | Съешь ещё этих мягких французских булок да выпей чаю                 | True            |
|      9      | Осенний холодный ветер кружит опавшие листья в парке у старого моста | False           |
|     10      | Шифровка текста для быстрого изучения языка                          | True            |
|     11      | Громкий ветер завывает в тёмных пещерах старого каменного ущелья     | False           |
|     12      | Каждый охотник желает знать где сидит фазан юркий                    | True            |
|     13      | Хитрая лисица бежит через овраг пугая чужих зайцев                   | True            |
|     14      | Южный экзотический фрукт в чай добавляют как лимон                   | True            |