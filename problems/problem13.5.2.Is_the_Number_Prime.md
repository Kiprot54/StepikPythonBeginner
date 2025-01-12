## Is the Number Prime?

Напишите функцию <code>is_prime(num)</code>, которая принимает в качестве аргумента натуральное число
и возвращает значение <code>True</code>, если число является простым, или <code>False</code> в противном случае.

***Примечание.*** Приведённый ниже код:

<pre><code>print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
</code></pre>

должен выводить:

<pre><code>False
False
True
</code></pre>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные | Выходные данные |
|:-----------:|----------------|-----------------|
|      1      | 1              | False           |
|      2      | 10             | False           |
|      3      | 2              | True            |
|      4      | 17             | True            |
|      5      | 101            | True            |
|      6      | 100            | False           |
|      7      | 360000         | False           |
|      8      | 121            | False           |
|      9      | 3              | True            |
|     10      | 4              | False           |
|     11      | 5              | True            |
|     12      | 6              | False           |
|     13      | 7              | True            |