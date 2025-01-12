## Is the Triangle Valid?

Напишите функцию <code>is_valid_triangle(side1, side2, side3)</code>, которая принимает в качестве аргументов три натуральных числа,
и возвращает значение <code>True</code>, если существует невырожденный треугольник со сторонами <code>side1</code>, <code>side2</code>, <code>side3</code>,
или <code>False</code> в противном случае.

***Примечание.*** Приведённый ниже код:

<pre><code>print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))
</code></pre>

должен выводить:

<pre><code>True
False
True
</code></pre>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные | Выходные данные |
|:-----------:|----------------|-----------------|
|      1      | 2<br>2<br>2    | True            |
|      2      | 2<br>3<br>10   | False           |
|      3      | 3<br>4<br>5    | True            |
|      4      | 10<br>11<br>12 | True            |
|      5      | 12<br>10<br>2  | False           |
|      6      | 100<br>1<br>2  | False           |