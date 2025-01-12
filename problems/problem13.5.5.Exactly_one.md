## Ровно в одном

Напишите функцию <code>is_one_away(word1, word2)</code>, которая принимает в качестве аргументов два слова
<code>word1</code> и <code>word2</code> и возвращает значение <code>True</code>,
если слова имеют одинаковую длину и отличаются ровно в одном символе, или <code>False</code> в противном случае.

***Примечание.*** Приведённый ниже код:

<pre><code>print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
</code></pre>

должен выводить:

<pre><code>True
True
False
False
</code></pre>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные             | Выходные данные |
|:-----------:|----------------------------|-----------------|
|      1      | bike<br>hike               | True            |
|      2      | water<br>wafer             | True            |
|      3      | abcd<br>abpo               | False           |
|      4      | abcd<br>abcde              | False           |
|      5      | abcd1234567<br>abcd1234568 | True            |
|      6      | abcd<br>abcd               | False           |
|      7      | aab<br>aba                 | False           |
|      8      | abcd<br>dcba               | False           |
|      9      | aab<br>abb                 | True            |
|     10      | hello<br>hell              | False           |