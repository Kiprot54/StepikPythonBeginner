## Простой шифр

На вход программе подаётся строка текста. Напишите программу, которая переводит каждый её символ
в соответствующий ему код из таблицы символов Unicode.

<br>

### *Тестовые данные:*

| Номер теста | Входные данные                                   | Выходные данные                                                                                                                                     |
|:-----------:|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|      1      | <pre>Hello world!</pre>                          | 72 101 108 108 111 32 119 111 114 108 100 33                                                                                                        |
|      2      | <pre>husdfjhsdjfhjsdfhjksdfkhsdfsdljfhsdlj</pre> | 104 117 115 100 102 106 104 115 100 106 102 104 106 115 100 102 104 106 107 115 100 102 107 104 115 100 102 115 100 108 106 102 104 115 100 108 106 |
|      3      | <pre>JDFHJSDFHSDLFJHSDJLASDLJ</pre>              | 74 68 70 72 74 83 68 70 72 83 68 76 70 74 72 83 68 74 76 65 83 68 76 74                                                                             |
|      4      | <pre>47374583758934758934708</pre>               | 52 55 51 55 52 53 56 51 55 53 56 57 51 52 55 53 56 57 51 52 55 48 56                                                                                |
|      5      | <pre>#@$@#$#%$^$^&%^&</pre>                      | 35 64 36 64 35 36 35 37 36 94 36 94 38 37 94 38                                                                                                     |