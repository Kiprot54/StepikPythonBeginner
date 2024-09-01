## Google search 2

На вход программе подаётся натуральное число <code>n</code>, затем <code>n</code> строк, затем число <code>k</code> —
количество поисковых запросов, затем <code>k</code> строк — поисковые запросы.
Напишите программу, которая выводит все введённые строки, в которых встречаются одновременно все поисковые запросы.

**Примечание.** Поиск не должен быть чувствителен к регистру символов.

<br>

### *Тестовые данные:*

| Номер теста | Входные данные                                                                                                                                                                                                                                                              | Выходные данные                                                                                                    |
|:-----------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
|      1      | 5<br>Язык Python прекрасен<br>C# - отличный язык программирования<br>Stepik - отличная платформа<br>BEEGEEK FOREVER!<br>язык Python появился 20 февраля 1991<br>2<br>язык<br>python                                                                                         | Язык Python прекрасен<br>язык Python появился 20 февраля 1991                                                      |
|      2      | 6<br>A caelo usque ad BEEGEEK centrum<br>A capillo usque ad ungues<br>A capite ad calcem beegeek<br>Ab absurdo beegeeK<br>Ab BEEGEEK equis ad asinos<br>Ab hoedis scindere oves<br>1<br>Beegeek                                                                             | A caelo usque ad BEEGEEK centrum<br>A capite ad calcem beegeek<br>Ab absurdo beegeeK<br>Ab BEEGEEK equis ad asinos |
|      3      | 5<br>Язык Python прекрасен<br>C# - отличный язык программирования<br>Stepik - отличная платформа<br>BEEGEEK FOREVER!<br>язык Python появился 20 февраля 1991<br>3<br>язык<br>python<br>прекрасен                                                                            | Язык Python прекрасен                                                                                              |
|      4      | 6<br>Язык Python прекрасен<br>C# - отличный язык программирования<br>Stepik - отличная платформа<br>BEEGEEK qwerty FOREVER навсегда! gaga<br>язык Python появился 20 февраля 1991<br>пчела beegeek лучшая как всегдаgaga qwerty<br>4<br>beegeek<br>Всегда<br>gaga<br>qwerty | BEEGEEK qwerty FOREVER навсегда! gaga<br>пчела beegeek лучшая как всегдаgaga qwerty                                |
|      5      | 5<br>Python прекрасен<br>C# - отличный язык программирования<br>Stepik - отличная платформа<br>BEEGEEK FOREVER!<br>язык Python появился 20 февраля 1991<br>2<br>язык<br>python                                                                                              | язык Python появился 20 февраля 1991                                                                               |