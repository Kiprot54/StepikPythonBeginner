## Правильный многоугольник

Напишите программу, которая на вход получает длину стороны правильного многоугольника <code>a</code> и количество его сторон <code>n</code> и находит площадь указанного правильного многоугольника.

**Примечание.** Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь правильного многоугольника с длиной стороны <code>a</code> и количеством сторон <code>n</code> вычисляется по формуле:

<pre>
        n * a<sup>2</sup> 
S = ---------------
     4 * tg(π / n)
</pre>

<img src="/img/problem6.3.5.png" alt="Правильный многоугольник" width="500">

<br>

### *Тестовые данные:*

| Номер теста | Входные данные | Выходные данные    |
|:-----------:|----------------|--------------------|
|      1      | 3<br>2.0       | 1.7320508075688779 |
|      2      | 4<br>10.5      | 110.25             |
|      3      | 5<br>7.78      | 104.13774429380925 |
|      4      | 17<br>100.0    | 227354.9189841655  |
|      5      | 1000<br>45.0   | 161143849.7364349  |