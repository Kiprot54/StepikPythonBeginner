## Популяция

На вход программе подаются три натуральных числа <code>m</code>, <code>p</code>, <code>n</code>:

- <code>m</code>: стартовое количество организмов;
- <code>p</code>: среднесуточное увеличение в %;
- <code>n</code>: количество дней для размножения.

Напишите программу, которая предсказывает размер популяции организмов с 1-го по n-й день (включительно).
Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.

**Подсказка.** В 1-й день у нас есть количество организмов <code>m</code>,
которое во 2-й день увеличится на <code>p</code>%.
Во 2-й день, значит, у нас уже будет <code>m + m (p / 100) = m(1 + (p / 100))</code> организмов.
В 3-й день, соответственно, у нас уже будет <code>m(1 + p / 100) *  (1 + p / 100) * (p / 100) = m (1 + p / 100)<sup>2</sup></code> организмов и т.д.
Соответственно, в <code>n</code>-й день у нас будет <code>m * (1 + p / 100)<sup>n - 1</sup></code> организмов.

<br>

### *Тестовые данные:*

| Номер теста | Входные данные  | Выходные данные                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:-----------:|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      1      | 10<br>50<br>6   | 1 10.0<br>2 15.0<br>3 22.5<br>4 33.75<br>5 50.625<br>6 75.9375                                                                                                                                                                                                                                                                                                                                                                                                                 |
|      2      | 100<br>25<br>1  | 1 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|      3      | 120<br>25<br>4  | 1 120.0<br>2 150.0<br>3 187.5<br>4 234.375                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|      4      | 7<br>10<br>20   | 1 7.0<br>2 7.700000000000001<br>3 8.470000000000002<br>4 9.317000000000004<br>5 10.248700000000005<br>6 11.273570000000007<br>7 12.400927000000008<br>8 13.64101970000001<br>9 15.005121670000012<br>10 16.505633837000016<br>11 18.15619722070002<br>12 19.971816942770023<br>13 21.968998637047026<br>14 24.16589850075173<br>15 26.582488350826907<br>16 29.240737185909598<br>17 32.16481090450056<br>18 35.38129199495062<br>19 38.91942119444569<br>20 42.81136331389026 |
|      5      | 100<br>75<br>15 | 1 100.0<br>2 175.0<br>3 306.25<br>4 535.9375<br>5 937.890625<br>6 1641.30859375<br>7 2872.2900390625<br>8 5026.507568359375<br>9 8796.388244628906<br>10 15393.679428100586<br>11 26938.938999176025<br>12 47143.143248558044<br>13 82500.50068497658<br>14 144375.876198709<br>15 252657.78334774077                                                                                                                                                                          |
|      6      | 10<br>50<br>7   | 1 10.0<br>2 15.0<br>3 22.5<br>4 33.75<br>5 50.625<br>6 75.9375<br>7 113.90625                                                                                                                                                                                                                                                                                                                                                                                                  |