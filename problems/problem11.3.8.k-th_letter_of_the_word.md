## k-ая буква слова

На вход программе подаётся натуральное число <code>n</code> и <code>n</code> строк, а затем число <code>k</code>.
Напишите программу, которая выводит <code>k</code>-ую букву из введённых строк на одной строке без пробелов.

**Примечание.** Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при выводе нужно игнорировать.

<br>

### *Тестовые данные:*

| Номер теста | Входные данные                                                        | Выходные данные |
|:-----------:|-----------------------------------------------------------------------|-----------------|
|      1      | 5<br>abcdef<br>bcdefg<br>cdefgh<br>defghi<br>efghij<br>2              | bcdef           |
|      2      | 5<br>aaaaa<br>bbbb<br>ccc<br>dd<br>e<br>3                             | abc             |
|      3      | 5<br>aaaaa<br>bbbbb<br>ccccc<br>ddddd<br>eee<br>5                     | abcd            |
|      4      | 10<br>aaaaa<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>a<br>3         | a               |
|      5      | 10<br>aaaaa<br>a<br>a<br>a<br>a<br>bbbbb<br>a<br>a<br>a<br>a<br>3     | ab              |
|      5      | 10<br>aaaaa<br>a<br>a<br>a<br>a<br>a<br>adddd<br>a<br>a<br>acccc<br>5 | adc             |