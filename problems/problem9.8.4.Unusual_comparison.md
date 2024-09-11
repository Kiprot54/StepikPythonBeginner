## Необычное сравнение

На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно, не учитывая регистр и игнорируя все небуквенные символы.
Программа должна вывести сообщение о том, равны ли строки в результате такой проверки.

**Примечание.** Разберём 1-й тест:
<div style="background-color: #ffff; display: inline-block;">
<img src="../img/problem9.8.4.webp" alt="Необычное сравнение" width="500">
</div>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные                                        | Выходные данные |
|:-----------:|-------------------------------------------------------|-----------------|
|      1      | Ab4c1$#ddd<br>a_b_c##DDD70                            | YES             |
|      2      | n5#e6vER<br>+NEV-er                                   | YES             |
|      3      | с-э-м<br>С-Э-Э-М                                      | NO              |
|      4      | -r-u-s-s-i-a-<br>R+U+S+S+I+A                          | YES             |
|      5      | e==C=/I(k)A<br>E__ci/33336996-a                       | NO              |
|      6      | TIMUR🔥<br>timur😎                                    | YES             |
|      7      | scorpion🦂<br>scorpion_666K                           | NO              |
|      8      | Душнила_best__<br>душнила --- BEST____                | YES             |
|      9      | p___yth589on<br>+*/python45                           | YES             |
|     10      | поколение python<br>ПОКОЛЕНИЕ PYTHON                  | YES             |
|     11      | perm<br>perm                                          | YES             |
|     12      | Still don't know my name<br>still do not know my name | NO              |
|     13      | Hello,     world!!!!<br>helloworld                    | YES             |
|     14      | ++exa/-mple<br>/*exa++mple                            | YES             |