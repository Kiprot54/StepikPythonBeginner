## Цветовой микшер

Красный, синий и жёлтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
При смешивании двух основных цветов получается вторичный цвет:

- если смешать красный и синий, то получится фиолетовый;
- если смешать красный и жёлтый, то получится оранжевый;
- если смешать синий и жёлтый, то получится зелёный.
 
Напишите программу, которая считывает названия двух основных цветов для смешивания.
Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «жёлтый»,
то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета,
который получится в результате.

<br>

### *Тестовые данные:*

| Номер теста | Входные данные       | Выходные данные |
|:-----------:|----------------------|-----------------|
|      1      | красный<br>синий     | фиолетовый      |
|      2      | красный<br>блаблабла | ошибка ввода    |
|      3      | синий<br>красный     | фиолетовый      |
|      4      | красный<br>желтый    | оранжевый       |
|      5      | желтый<br>красный    | оранжевый       |
|      6      | синий<br>желтый      | зеленый         |
|      7      | желтый<br>синий      | зеленый         |
|      8      | укакуук<br>красный   | ошибка цвета    |
|      9      | ошибка<br>цвета      | ошибка цвета    |
|     10      | желтый<br>блабла90   | ошибка цвета    |
|     11      | оаволуалйц<br>желтый | ошибка цвета    |
|     12      | синий<br>лолцйуцуац  | ошибка цвета    |
|     13      | лсьукльсуд<br>синий  | ошибка цвета    |
|     14      | красный<br>красный   | красный         |
|     15      | синий<br>синий       | синий           |
|     16      | желтый<br>желтый     | желтый          |
|     13      | питон<br>питон       | ошибка цвета    |