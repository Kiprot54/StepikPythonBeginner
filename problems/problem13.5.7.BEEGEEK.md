## BEEGEEK

BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид <code>a:b:c</code>, где <code>a</code>, <code>b</code> и <code>c</code> –
натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

- число <code>a</code> – должно быть палиндромом;
- число <code>b</code> – должно быть простым;
- число <code>c</code> – должно быть чётным.

Напишите функцию <code>is_valid_password(password)</code>, которая принимает в качестве аргумента
строковое значение пароля <code>password</code> и возвращает значение <code>True</code>,
если пароль является действительным паролем BEEGEEK банка, или <code>False</code> в противном случае.

***Примечание.*** Приведённый ниже код:

<pre><code>print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
</code></pre>

должен выводить:

<pre><code>True
False
False
False
</code></pre>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные               | Выходные данные |
|:-----------:|------------------------------|-----------------|
|      1      | 15551:7:290                  | True            |
|      2      | 155561:7:290                 | False           |
|      3      | 15551:72:290                 | False           |
|      4      | 15551:7:291                  | False           |
|      5      | 155351:70:290                | False           |
|      6      | 1551151:700:2901             | False           |
|      7      | 11111:71:90000               | True            |
|      8      | 24422442:181:890000          | True            |
|      9      | 1221:101:22:22               | False           |
|     10      | 1221:101:22:221221:101:22:22 | False           |
|     11      | 1991:1:20                    | False           |
|     12      | 121:2:2                      | True            |