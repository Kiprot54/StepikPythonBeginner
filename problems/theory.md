# "Поколение Python": курс для начинающих

## Содержание

<a href="#h22">2.2. Команды print и input</a><br>
<a href="#h24">2.4. Целочисленная арифметика. Часть 1</a><br>
<a href="#h25">2.5. Целочисленная арифметика. Часть 2</a><br>
<a href="#h41">4.1. Выбор из двух</a><br>
<a href="#h42">4.2. Логические операции</a><br>
<a href="#h61">6.1. Числовые типы данных: int, float</a><br>
<a href="#h62">6.2. Строковый тип данных</a><br>
<a href="#h63">6.3. Модуль math</a><br>
<a href="#h71">7.1. Цикл for</a><br>
<a href="#h72">7.2. Цикл for: функция range</a><br>
<a href="#h73">7.3. Частые сценарии</a><br>
<a href="#h74">7.4. Цикл while</a><br>
<a href="#h91">9.1. Индексация</a><br>
<a href="#h92">9.2. Срезы</a><br>
<a href="#h93">9.3. Методы строк</a><br>
<a href="#h96">9.6. Форматирование строк</a><br>
<a href="#h97">9.7. Строки в памяти компьютера, таблица символов Unicode</a><br>

## 2. Ввод-вывод данных

### <span id="h22">2.2. *Команды print и input*</span>

<code>print()</code> - выводит данные на экран (в консоль)

<code>print(data1, [data2], ..., [dataN], [sep=' '], [end = '\n'])</code> - полная запись<br>
<code>data1-dataN</code> - данные, которые нужно вывести на экран.<br>
<code>sep</code> - разделитель, который ставится между аргументами (по умолчанию равен пробелу - ' '). Необязательный параметр.<br>
<code>end</code> - определяет, что нужно поставить в конце вывода (по умолчанию равен символу перевода строки - '\n' ). Необязательный параметр.

*Примеры:*

<code>print('Python')</code><br>
<code>print('Я', 'учусь', 'программировать', 'на', 'Python!')</code><br>
<code>print(24)</code><br>
<code>print()</code>

---

<code>input()</code> - считывает данные, введённые с клавиатуры

*Примеры:*

<code>input()</code><br>
<code>nput('Введи что-нибудь: ')</code>

---

Переменные - "области в памяти", которые мы для нашего удобства можем назвать каким-то именем.

1. В имени переменной рекомендуется использовать только латинские буквы a-z, A-Z, цифры и символ нижнего подчеркивания (_);
2. Имя переменной не может начинаться с цифры;
3. Имя переменной не может содержать пробелы;
4. Имя переменной по возможности должно отражать ее назначение.

*Примеры:*

<code>s = 'строка'</code><br>
<code>n = 12</code><br>
<code>name = input('Введи своё имя: ')</code><br>
<code>name, surname = input('Введи своё имя: '), input('Введи свою фамилию: ')</code>

### <span id="h24">2.4. *Целочисленная арифметика. Часть 1*</span>

*Основные операции с числами:*<br>
<code>a = 4</code><br>
<code>b = 2</code><br>
<code>+</code> - сложение (a + b)<br>
<code>-</code> - вычитание (a - b)<br>
<code>*</code> - умножение (a * b)<br>
<code>/</code> - деление (a / b)

---

<code>int()</code> - преобразует строку к целому числу

<code>str()</code> - преобразует число к строке

### <span id="h25">2.5. *Целочисленная арифметика. Часть 2*</span>

*Дополнительные операции с числами:*<br>
<code>**</code> - Возведение в степень (a<sup>b</sup>)<br>
<code>%</code> - Остаток от деления (a % b)<br>
<code>//</code> - Целочисленное деление (a // b)

*Примеры:*

<code>a = 5</code><br>
<code>b = 2</code><br>
<code>print(a ** b)  # 25</code><br>
<code>print(a % b)  # 1</code><br>
<code>print(a // b)  # 2</code><br>

<br>

## 4. Условный оператор

### <span id="h41">4.1. *Выбор из двух*</span>

#### Условный оператор if-elif-else

<pre>
    if <условие 1>:
        <блок кода 1>
    [elif <условие 2>:
        <блок кода 2>]
    ...
    [elif <условие N>:
        <блок кода N>]
    [else:
        <блок кода>]
</pre>

#### Операторы сравнения

<code>a == b</code> - a равно b<br>
<code>a < b</code> - a меньше b<br>
<code>a > b</code> - a больше b<br>
<code>a <= b</code> - a меньше либо равно b<br>
<code>a >= b</code> - a больше либо равно b<br>
<code>a != b</code> - a не равно b<br>

<code>a == b == с</code>
<code>1 <= x <= 10</code>

### <span id="h42">4.2. *Логические операции*</span>

<code>and</code> — логическое умножение;<br>
<code>or</code> — логическое сложение;<br>
<code>not</code> — логическое отрицание.

|   a   |   b   | a and b |
|:-----:|:-----:|:-------:|
| False | False |  False  |
| False | True  |  False  |
| True  | False |  False  |
| True  | True  |  True   |

|   a   |   b   | a or b |
|:-----:|:-----:|:------:|
| False | False | False  |
| False | True  |  True  |
| True  | False |  True  |
| True  | True  |  True  |

|   a   | not a |
|:-----:|:-----:|
| False | True  | 
| True  | False |

<br>

## 6. Типы данных

### <span id="h61">6.1. *Числовые типы данных: int, float*</span>

<code>int(a)</code> - преобразует данные <code>a</code> к целому числу<br>
<code>float(a)</code> - преобразует данные <code>a</code> к числу с плавающей точкой

<code>min()</code> - найти минимальное значение;<br>
<code>max()</code> - найти максимальное значение;<br>
<code>abs()</code> - найти модуль числа;

### <span id="h62">6.2. *Строковый тип данных*</span>

<code>str()</code> - преобразовать к строке<br>
<code>len()</code> - найти длину строки

<code>s1 = 'ab'</code><br>
<code>s2 = 'cd'</code><br>
<code>print(s1 + s2)  # 'abcd'</code> - Конкатенация строк<br>
<code>print(s1 * 3)  # 'ababab'</code> - Умножение строки на число<br>
<code>print('a' in a)  # True</code> - Проверка нахождения одной строки в другой<br>
<code>print('c' in a)  # False</code><br>

### <span id="h63">6.3. *Модуль math*</span>

**Варианты импорта модуля**

<code>import math</code><br>
<code>num = math.sqrt(2)</code><br>
<code>print(num)</code>

<code>from math import *</code> - импортирует все функции из модуля<br>
<code>num = sqrt(2)</code><br>
<code>print(num)</code>

<code>from math import sqrt, ceil</code> - импортирует определённые функции из модуля<br>
<code>print(sqrt(25))</code><br>
<code>print(ceil(34.7))</code>

---

#### Список функций модуля math

|                                       Функция | Описание                                                                                                                                             |
|----------------------------------------------:|------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                **Округления** |                                                                                                                                                      |
|                                        abs(x) | Модуль числа x (абсолютная величина)                                                                                                                 |
|                                       ceil(x) | Округляет число x вверх («потолок»)                                                                                                                  |
|                                      floor(x) | Округляет число x вниз («пол»)                                                                                                                       |
|                                         int() | Округляет число в сторону нуля                                                                                                                       |
|                                      round(x) | Округляет число x до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа (банковское округление) |
|                                   round(x, n) | Округляет число x до n знаков после точки                                                                                                            |
| **Корни, логарифмы,<br> степени и факториал** |                                                                                                                                                      |
|                                  factorial(n) | Факториал натурального числа n                                                                                                                       |
|                                        log(x) | Натуральный логарифм числа x. Основание натурального логарифма равно числу e                                                                         |
|                                     log(x, b) | Логарифм числа x по основанию b                                                                                                                      |
|                                      log10(x) | Десятичный логарифм числа x. Основание десятичного логарифма равно числу 10                                                                          |
|                                     pow(x, n) | Возведение числа x в степень n                                                                                                                       |
|                                       sqrt(x) | Квадратный корень числа x                                                                                                                            |
|                             **Тригонометрия** |                                                                                                                                                      |
|                                       acos(x) | Возвращает угол в радианах от 0 до π, косинус которого равен x                                                                                       |
|                                       asin(x) | Возвращает угол в радианах от −π/2 до π/2, синус которого равен x                                                                                    |
|                                       atan(x) | Возвращает угол в радианах от −π/2 до π/2, тангенс которого равен x                                                                                  |
|                                   atan2(y, x) | Полярный угол (в радианах) точки с координатами (x, y)                                                                                               |
|                                        cos(x) | Косинус угла x, задаваемого в радианах                                                                                                               |
|                                    degrees(x) | Преобразует угол x, заданный в радианах, в градусы                                                                                                   |
|                                    radians(x) | Преобразует угол x, заданный в градусах, в радианы                                                                                                   |
|                                        sin(x) | Синус угла x, задаваемого в радианах                                                                                                                 |
|                                        tan(x) | Тангенс угла x, задаваемого в радианах                                                                                                               |

<br>

#### Список констант модуля math

| Константа | Описание                                       |
|----------:|------------------------------------------------|
|         e | Число e = 2.718281828459045 (константа Эйлера) |
|        pi | Число π = 3.141592653589793                    |

<br>

## 7. Циклы for и while

### <span id="h71">7.1. *Цикл for*</span>

<pre>
    for <название переменной цикла> in range(<количество повторений>):
        <блок кода>
</pre>

Переменная цикла последовательно принимает значения, указанные в функции range().

*Пример:*

Код:
<pre><code>
for i in range(10):
    print(i)
</code></pre>

нужно читать так: для i, последовательно принимающего значения в диапазоне (0; 10), вывести на экран i.

### <span id="h72">7.2. *Цикл for: функция range*</span>

Функция <code>range()</code> генерирует последовательность чисел.

<code>range(n)</code> - генерирует последовательность чисел от <code>0</code> до <code>n-1</code>.<br>
<code>range(n, m)</code> - генерирует последовательность чисел от <code>n</code> до <code>m-1</code>. <code>n</code> - старт последовательности (включительно). <code>m</code> - стоп последовательности (не включительно).<br>
<code>range(n, m, k)</code> - генерирует последовательность чисел от <code>n</code> до <code>m-1</code> с шагом <code>k</code>. <code>n</code> - старт последовательности (включительно). <code>m</code> - стоп последовательности (не включительно). <code>k</code> - величина шага последовательности.<br>

*Примеры:*<br>
<code>range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9</code><br>
<code>range(3, 10)  # 3, 4, 5, 6, 7, 8, 9</code><br>
<code>range(3, 10, 2)  # 3, 5, 7, 9</code><br>
<code>range(10, -10, -3)  # 10, 7, 4, 1, -2, -5, -8</code>

### <span id="h73">7.3. *Частые сценарии*</span>

#### Подсчет количества

<pre><code>
    counter = 0
    for _ in range(10):
        num = int(input())
        if num > 10:
            counter = counter + 1
    
    print('Было введено', counter, 'чисел, больших 10.')
</code></pre>

#### Вычисление суммы

<pre><code>
    total = 0
    for _ in range(10):
        num = int(input())
        if num > 10:
            total = total + num
    
    print('Сумма чисел больших 10 равна',  total)
</code></pre>

#### Вычисление произведения

<pre><code>
    total = 0
    for _ in range(10):
        num = int(input())
        if num > 10:
            total = total * num
    
    print('Произведение чисел больших 10 равно',  total)
</code></pre>

#### Обмен значений переменных

Универсальный способ:
<pre><code>
temp = x
x = y
y = temp
</code></pre>

На Python:<br>
<code>x, y = y, x</code><br>
<code>a, b, c, d = d, c, a, b</code>

#### Сигнальные метки

<pre><code>
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная') 
elif flag == True:
    print('Число простое')
else:
    print('Число составное')
</code></pre>

#### Максимум

<pre><code>
largest = 0
for _ in range(10):
    num = int(input())    
    if num > largest:
        largest = num

print('Наибольшее число равно', largest) 
</code></pre>

#### Минимум

<pre><code>
smallest = 0
for _ in range(10):
    num = int(input())    
    if num < smallest:
        smallest = num

print('Наименьшее число равно', smallest) 
</code></pre>

#### Расширенные операторы присваивания

<code>a += b  # То же, что и a = a + b</code>

### <span id="h74">7.4. *Цикл while*</span>

<pre>
    while <условие>:
        <блок кода>
</pre>

Блок кода выполняется до тех пор, пока условие == True.

*Пример:*

Код:

<pre><code>
i = 0
while i < 10:
    print(i)
    i += 1
</code></pre>

можно читать так: пока i меньше 10, вывести на экран i, и прибавить к i единицу.

### <span id="h76">7.6. *break, continue и else*</span>

<code>break</code> - прерывает ближайший цикл for или while.

<code>continue</code> - позволяет перейти к следующей итерации цикла for или while до завершения всех команд в теле цикла.

<br>

## 9. Строковый тип данных

### <span id="h91">9.1. *Индексация*</span>

#### Индексация строк

<code>s = 'abcdef'</code><br>
<code>print(s[0]) # 'a'</code><br>
<code>print(s[1]) # 'b'</code><br>
<code>print(s[5]) # 'f'</code><br>
<code>print(s[len(s) - 1]) # 'f'</code><br>
<code>print(s[-1]) # 'f'</code><br>
<code>print(s[-3]) # 'd'</code><br>
<code>print(s[-5]) # 'a'</code>

#### Итерирование строк

<pre><code>
s = 'abcdef'
for i in range(len(s)):
    print(s[i])
# a
# b
# c
# d
# e
# f
</code></pre>

<pre><code>
s = 'abcdef'
for c in s:
    print(c)
# a
# b
# c
# d
# e
# f
</code></pre>

### <span id="h92">9.2. *Срезы*</span>

Срез <code>s[n, m, k]</code> создает подстроку строки s.

<code>n</code> - индекс, с которого начинается срез (включительно). Обязательный параметр.<br>
<code>m</code> - индекс, с которого начинается срез (не включительно). Необязательный параметр.<br>
<code>k</code> - шаг среза. Необязательный параметр.

*Примеры:*
<code>s = 'abcdefghij'</code>

| Программный код |       Результат        | Пояснение                                                         |
|----------------:|:----------------------:|-------------------------------------------------------------------|
|          s[2:5] |          cde           | строка, состоящая из символов с индексами 2, 3, 4                 |
|           s[:5] |         abcde          | первые пять символов строки                                       |
|           s[5:] |         fghij          | строка, состоящая из символов с индексами от 5 до конца           |
|          s[-2:] |           ij           | последние два символа строки                                      |
|            s[:] |       abcdefghij       | вся строка целиком                                                |
|        s[1:7:2] |          bdf           | строка состоящая из каждого второго символа с индексами от 1 до 6 |
|         s[::-1] |       jihgfedcba       | строка в обратном порядке, так как шаг отрицательный              |

### <span id="h93">9.3. *Методы строк*</span>

Метод — функция, применяемая к объекту. Метод вызывается в виде <имя_объекта>.<имя_метода(параметры)>.

|        Метод | Программный код                                                                                                                                                                                                             | Результат                                                                              | Пояснение                                                                                                                                                                                                                                                                                                           |
|-------------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| capitalize() | <pre><code>s = 'foO BaR BAZ quX'<br>print(s.capitalize())</code></pre>                                                                                                                                                      | <pre><code><br>Foo bar baz qux</code></pre>                                            | Метод <code>capitalize()</code> возвращает копию строки <code>s</code>, в которой первый символ имеет верхний регистр, а все остальные символы имеют нижний регистр. Символы, не являющиеся буквами алфавита, остаются неизменными.                                                                                 |
|      count() | <pre><code>s = 'foo goo moo'<br>print(s.count('oo'))<br>print(s.count('oo', 0, 8))</code></pre>                                                                                                                             | <pre><code><br>3<br>2</code></pre>                                                     | Метод <code>count(\<sub>, \<start>, \<end>)</code> считает количество непересекающихся вхождений подстроки <code>\<sub></code> в исходную строку <code>s</code>.                                                                                                                                                    |
|   endswith() | <pre><code>s = 'foobar'<br>print(s.endswith('bar'))<br>print(s.endswith('baz'))</code></pre>                                                                                                                                | <pre><code><br>True<br>False</code></pre>                                              | Метод <code>endswith(\<suffix>, \<start>, \<end>)</code> определяет, оканчивается ли исходная строка s подстрокой <code>\<suffix></code>. Метод возвращает значение <code>True</code>, если исходная строка оканчивается на подстроку <code>\<suffix></code>, или <code>False</code> в противном случае.            |
|       find() | <pre><code>s = 'foo bar foo baz foo qux'<br>print(s.find('foo'))<br>print(s.find('bar'))<br>print(s.find('qu'))<br>print(s.find('python'))</code></pre>                                                                     | <pre><code><br>0<br>4<br>20<br>-1</code></pre>                                         | Метод <code>find(\<sub>, \<start>, \<end>)</code> находит индекс первого вхождения подстроки <code>\<sub></code> в исходной строке <code>s</code>. Если строка <code>s</code> не содержит подстроки <code>\<sub></code>, то метод возвращает значение <code>-1</code>.                                              |
|      index() | <pre><code>s = 'foo bar foo baz foo qux'<br>print(s.index('foo'))<br>print(s.index('bar'))<br>print(s.index('qu'))<br>print(s.index('python'))</code></pre>                                                                 | <pre><code><br>0<br>4<br>20<br>ValueError: substring not found</code></pre>            | Метод <code>index(\<sub>, \<start>, \<end>)</code> идентичен методу <code>find(\<sub>, \<start>, \<end>)</code>, за тем исключением, что он вызывает ошибку <code>ValueError: substring not found</code>во время выполнения программы, если подстрока <code>\<sub></code> не найдена.                               |
|    isalnum() | <pre><code>s1 = 'abc123'<br>s2 = 'abc$*123'<br>s3 = ''<br>s4 = 'BEEGEEK'<br>s5 = '2202'<br><br>print(s1.isalnum())<br>print(s2.isalnum())<br>print(s3.isalnum())<br>print(s4.isalnum())<br>print(s5.isalnum())</code></pre> | <pre><code><br><br><br><br><br><br>True<br>False<br>False<br>True<br>True</code></pre> | Метод <code>isalnum()</code> определяет, состоит ли исходная строка из буквенно-цифровых символов. Метод возвращает значение <code>True</code>, если исходная строка является непустой и состоит только из буквенно-цифровых символов, или <code>False</code> в противном случае.                                   |
|    isalpha() | <pre><code>s1 = 'ABCabc'<br>s2 = 'abc123'<br>s3 = ''<br><br>print(s1.isalpha())<br>print(s2.isalpha())<br>print(s3.isalpha())</code></pre>                                                                                  | <pre><code><br><br><br><br>True<br>False<br>False</code></pre>                         | Метод <code>isalpha()</code> определяет, состоит ли исходная строка только из буквенных символов. Метод возвращает значение <code>True</code>, если исходная строка является непустой и состоит только из буквенных символов, или <code>False</code> в противном случае.                                            |
|    isdigit() | <pre><code>s1 = '1234567'<br>s2 = 'abc123'<br>s3 = ''<br><br>print(s1.isdigit())<br>print(s2.isdigit())<br>print(s3.isdigit())</code></pre>                                                                                 | <pre><code><br><br><br><br>True<br>False<br>False</code></pre>                         | Метод <code>isdigit()</code> определяет, состоит ли исходная строка только из цифровых символов. Метод возвращает значение <code>True</code>, если исходная строка является непустой и состоит только из цифровых символов, или <code>False</code> в противном случае.                                              |
|    islower() | <pre><code>s1 = 'abc'<br>s2 = 'abc1$d'<br>s3 = 'Abc1$D'<br>s4 = '1234'<br>s5 = '+-*/'<br><br>print(s1.islower())<br>print(s2.islower())<br>print(s3.islower())<br>print(s4.islower())<br>print(s5.islower())</code></pre>   | <pre><code><br><br><br><br><br><br>True<br>True<br>False<br>False<br>False</pre>       | Метод <code>islower()</code> определяет, являются ли все буквенные символы исходной строки строчными (имеют нижний регистр). Метод возвращает значение <code>True</code>, если все буквенные символы исходной строки являются строчными, или <code>False</code> в противном случае.                                 |
|    isspace() | <pre><code>s1 = '       '<br>s2 = 'abc1$d'<br>s3 = ''<br><br>print(s1.isspace())<br>print(s2.isspace())<br>print(s3.isspace())</code></pre>                                                                                 | <pre><code><br><br><br><br>True<br>False<br>False</pre>                                | Метод <code>isspace()</code> определяет, состоит ли исходная строка только из пробельных символов. Метод возвращает значение <code>True</code>, если строка состоит только из пробельных символов, или <code>False</code> в противном случае.                                                                       |
|    isupper() | <pre><code>s1 = 'ABC'<br>s2 = 'ABC1$D'<br>s3 = 'Abc1$D'<br>s4 = '5678'<br>s5 = '!?_&'<br><br>print(s1.isupper())<br>print(s2.isupper())<br>print(s3.isupper())<br>print(s4.isupper())<br>print(s5.isupper())</code></pre>   | <pre><code><br><br><br><br><br><br>True<br>True<br>False<br>False<br>False</pre>       | Метод <code>isupper()</code> определяет, являются ли все буквенные символы исходной строки заглавными (имеют верхний регистр). Метод возвращает значение <code>True</code>, если все буквенные символы исходной строки являются заглавными, или <code>False</code> в противном случае.                              |
|      lower() | <pre><code>s = 'FOO Bar 123 baz qUX'<br>print(s.lower())</code></pre>                                                                                                                                                       | <pre><code><br>foo bar 123 baz qux</code></pre>                                        | Метод <code>lower()</code> возвращает копию строки <code>s</code>, в которой все символы имеют нижний регистр.                                                                                                                                                                                                      |
|     lstrip() | <pre><code>s = '     foo bar foo baz foo qux      '<br>print(s.lstrip())</code></pre>                                                                                                                                       | <pre><code><br>foo bar foo baz foo qux⎵ ⎵ ⎵ ⎵ ⎵ ⎵</pre>                                | Метод <code>lstrip()</code> возвращает копию строки <code>s</code>, у которой удалены все пробелы, стоящие в начале строки. Метод <code>lstrip()</code> может принимать на вход опциональный аргумент <code>\<chars></code> – строку, которая определяет набор символов для удаления.                               |
|    replace() | <pre><code>s = 'foo bar foo baz foo qux'<br>print(s.replace('foo', 'grault'))<br>print(s.replace('foo', 'grault', 2))</pre>                                                                                                 | <pre><code><br>grault bar grault baz grault qux<br>grault bar grault baz foo qux</pre> | Метод <code>replace(\<old>, \<new>)</code> возвращает копию строки <code>s</code> со всеми вхождениями подстроки <code>\<old></code>, замененными на <code>\<new></code>. Метод <code>replace()</code> может принимать опциональный третий аргумент <code>\<count></code>, который определяет количество замен.     |
|      rfind() | <pre><code>s = 'foo bar foo baz foo qux'<br>print(s.rfind('foo'))<br>print(s.rfind('bar'))<br>print(s.rfind('qu'))<br>print(s.rfind('python'))</code></pre>                                                                 | <pre><code><br>0<br>4<br>20<br>ValueError: substring not found</code></pre>            | Метод <code>rfind(\<sub>, \<start>, \<end>)</code> идентичен методу <code>find(\<sub>, \<start>, \<end>)</code>, за тем исключением, что он ищет первое вхождение подстроки <code>\<sub></code>, начиная с конца строки <code>s</code>.                                                                             |
|     rindex() | <pre><code>s = 'foo bar foo baz foo qux'<br>print(s.rindex('foo'))<br>rindex(s.rfind('bar'))<br>print(s.rindex('qu'))<br>print(s.rindex('python'))</code></pre>                                                             | <pre><code><br>0<br>4<br>20<br>-1</code></pre>                                         | Метод <code>rindex(\<sub>, \<start>, \<end>)</code> идентичен методу <code>index(\<sub>, \<start>, \<end>)</code>, за тем исключением, что он ищет первое вхождение подстроки <code>\<sub></code>, начиная с конца строки <code>s</code>.                                                                           |
|     rstrip() | <pre><code>s = '     foo bar foo baz foo qux      '<br>print(s.rstrip())</code></pre>                                                                                                                                       | <pre><code><br>⎵ ⎵ ⎵ ⎵ ⎵ ⎵foo bar foo baz foo qux</pre>                                | Метод <code>rstrip()</code> возвращает копию строки <code>s</code>, у которой удалены все пробелы, стоящие в конце строки.  Метод <code>rstrip()</code> может принимать на вход опциональный аргумент <code>\<chars></code> – строку, которая определяет набор символов для удаления.                               |
| startswith() | <pre><code>s = 'foobar'<br>print(s.startswith('foo'))<br>print(s.startswith('baz'))</code></pre>                                                                                                                            | <pre><code><br>True<br>False</code></pre>                                              | Метод <code>startswith(\<suffix>, \<start>, \<end>)</code> определяет, начинается ли исходная строка <code>s</code> подстрокой <code>\<suffix></code>. Если исходная строка начинается с подстроки <code>\<suffix></code>, метод возвращает значение <code>True</code>, а если нет, то значение <code>False</code>. |
|      strip() | <pre><code>s = '     foo bar foo baz foo qux      '<br>print(s.strip())</code></pre>                                                                                                                                        | <pre><code><br>foo bar foo baz foo qux</pre>                                           | Метод <code>strip()</code> возвращает копию строки <code>s</code>, у которой удалены все пробелы, стоящие в начале и конце строки. Метод <code>strip()</code> может принимать на вход опциональный аргумент <code>\<chars></code> – строку, которая определяет набор символов для удаления.                         |
|   swapcase() | <pre><code>s = 'FOO Bar 123 baz qUX'<br>print(s.swapcase())</code></pre>                                                                                                                                                    | <pre><code><br>foo bAR 123 BAZ Qux</code></pre>                                        | Метод <code>swapcase()</code> возвращает копию строки <code>s</code>, в которой все символы, имеющие верхний регистр, преобразуются в символы нижнего регистра и наоборот.                                                                                                                                          |
|      title() | <pre><code>s = "what's happened to ted's IBM stock?"<br>print(s.title())</code></pre>                                                                                                                                       | <pre><code><br>What'S Happened To Ted'S Ibm Stock?</code></pre>                        | Метод <code>title()</code> возвращает копию строки <code>s</code>, в которой первый символ каждого слова переводится в верхний регистр.                                                                                                                                                                             |
|      upper() | <pre><code>s = 'FOO Bar 123 baz qUX'<br>print(s.upper())</code></pre>                                                                                                                                                       | <pre><code><br>FOO BAR 123 BAZ QUX</code></pre>                                        | Метод <code>upper()</code> возвращает копию строки <code>s</code>, в которой все символы имеют верхний регистр.                                                                                                                                                                                                     |

### <span id="h96">9.6. *Форматирование строк*</span>

#### Метод format()

*Примеры:*

<pre><code>
birth_year = 1992
text = 'My name is Timur, I was born in {}'.format(birth_year)

print(text)  # <em>My name is Timur, I was born in 1992.</em>
</code></pre>

<pre><code>
birth_year = 1992
name = 'Timur'
profession = 'math teacher'
text = 'My name is {}, I was born in {}, I work as a {}.'.format(name, birth_year, profession)

print(text)  # <em>My name is Timur, I was born in 1992, I work as a math teacher.</em>
</code></pre>

<pre><code>
birth_year = 1992
name = 'Timur'
profession = 'math teacher'
text = 'My name is {2}, I was born in {1}, I work as a {0}.'.format(profession, birth_year, name)

print(text)  # <em>My name is Timur, I was born in 1992, I work as a math teacher.</em>
</code></pre>

<pre><code>
name = 'Timur'
city = 'Moscow'
text1 = 'My name is {0}-{0}-{0}!'.format(name, city)
text2 = '{1} is my city and {0} is my name!'.format(name, city)

print(text1)  # <em>My name is Timur-Timur-Timur!</em>
print(text2)  # <em>Moscow is my city and Timur is my name!</em>
</code></pre>

#### f-строки

*Пример:*

<pre><code>
first_name = 'Taylor'
last_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = f'{first_name} {last_name} is a very famous singer from the {country}. She was born on {birth_date} in {birth_place}.'

print(text)  # <em>Taylor Swift is a very famous singer from the USA. She was born on 1989/12/13 in West Reading, Pennsylvania.</em>
</code></pre>

### <span id="h97">9.7. *Строки в памяти компьютера, таблица символов Unicode*</span>

Юникод — это не кодировка. Это именно таблица символов. Первые 128 кодов таблицы символов Unicode совпадают с ASCII.

То, как символы с соответствующими кодами будут храниться в памяти компьютера, зависит от конкретной кодировки,
базирующейся на Юникоде. Например, UTF-8.

#### Функция ord

Функция <code>ord</code> позволяет определить код некоторого символа в таблице символов Unicode.

#### Функция chr

Функция <code>chr</code> позволяет определить по коду символа сам символ. Аргументом данной функции является численный код.

Функции <code>ord</code> и <code>chr</code> являются взаимнообратными.

<br>

## Встроенные функции

| Функция | Программный код                                                                                        | Результат                    | Пояснение                                                                                                                                             |
|--------:|--------------------------------------------------------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
|   abs() | <pre><code>n = -5<br>print(abs(n))</code></pre>                                                        | <code>5</code>               | Найти модуль числа                                                                                                                                    |
|   chr() | <pre><code>chr1 = chr(65)<br>chr2 = chr(75)<br>chr3 = chr(110)<br>print(chr1, chr2, chr3)</code></pre> | <code>A K n</code>               | Функция <code>chr</code> позволяет определить по коду символа сам символ. Аргументом данной функции является численный код.                           |
| float() | <pre><code>n = '5.3'<br>print(float(n))</code></pre>                                                   | <code>5.3</code>             | Преобразовать к числу с плавающей точкой                                                                                                              |
| input() |                                                                                                        | <code></code>                | Считать с клавиатуры                                                                                                                                  |
|   int() | <pre><code>n = '5.3'<br>print(int(n))</code></pre>                                                     | <code>5</code>               | Преобразовать к целому числу                                                                                                                          |
|   len() | <pre><code>s = 'string'<br>print(len(s))</code></pre>                                                  | <code>6</code>               | Найти длину строки или списка                                                                                                                         |
|   max() | <pre><code>n = 5<br>m = 6<br>print(max(n, m))</code></pre>                                             | <code>6</code>               | Найти максимальное значение                                                                                                                           |
|   min() | <pre><code>n = 5<br>m = 6<br>print(min(n, m))</code></pre>                                             | <code>5</code>               | Найти минимальное значение                                                                                                                            |
|   ord() | <pre><code>num1 = ord('A')<br>num2 = ord('B')<br>num3 = ord('a')<br>print(num1, num2, num3)</pre>      | <code>65 66 97</code>        | Функция <code>ord</code> позволяет определить код некоторого символа в таблице символов Unicode. Аргументом данной функции является одиночный символ. |
| print() | <pre><code>print('Вывожу на экран')</code></pre>                                                       | <code>Вывожу на экран</code> | Вывести на экран                                                                                                                                      |
|   str() | <pre><code>n = 5<br>print(str(n))</code></pre>                                                         | <code>'5'</code>             | Преобразовать к строке                                                                                                                                |