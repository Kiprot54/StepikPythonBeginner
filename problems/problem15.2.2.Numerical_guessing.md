## Числовая угадайка

### Описание проекта

Программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
Если догадка пользователя больше случайного числа, то программа должна вывести сообщение <code>'Слишком много, попробуйте еще раз'</code>.
Если догадка меньше случайного числа, то программа должна вывести сообщение <code>'Слишком мало, попробуйте еще раз'</code>.
Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение <code>'Вы угадали, поздравляем!'</code>.

### Реализация проекта

1. Подключите модуль <code>random</code>.
2. Сгенерируйте случайное число от 1 до 100.
3. Выведите текст приветствия пользователю: <code>'Добро пожаловать в числовую угадайку'</code>.
4. Пользователь потенциально может ввести неверные данные, например, не число, или число превышающее 100. Важно предусмотреть такую возможность, чтобы программа продолжала правильно работать. Обработка такого рода ситуаций называется защитой от дурака.<br>Напишите функцию <code>is_valid()</code>, в которую передаётся один строковый аргумент. Функция возвращает значение <code>True</code>, если переданный аргумент является целым числом от 1 до 100, и <code>False</code> в противном случае.
5. Организуйте цикл, который будет запрашивать у пользователя данные (цикл может быть бесконечным (<code>while True</code>) или может использовать сигнальную метку с последующим переключением, после угадывания числа).
6. Запросите у пользователя число от 1 до 100.
7. Проверьте введённые данные с помощью функции <code>is_valid()</code>:
   - если данные некорректны, выведите текст: <code>'А может быть всё-таки введём целое число от 1 до 100?'</code> и перейдите к следующей итерации основного цикла;
   - если данные корректны, преобразуйте их к целому числу для удобства дальнейшей работы.
8. Организуйте сравнение введённого числа с загаданным числом:
   - Если введённое число меньше загаданного числа, выведите текст: <code>'Ваше число меньше загаданного, попробуйте еще разок'</code>;
   - Если введённое число больше загаданного числа, выведите текст: <code>'Ваше число больше загаданного, попробуйте еще разок'</code>;
   - Если введённое число равно загаданному числу, выведите текст: <code>'Вы угадали, поздравляем!'</code>.
9. Выведите прощальное сообщение пользователю: <code>'Спасибо, что играли в числовую угадайку. Еще увидимся...'</code>.

### Улучшения проекта:
1. Добавьте подсчет попыток, сделанных пользователем. Когда число отгадано, программа должна показать количество попыток.
2. Добавьте возможность генерации нового числа (повторная игра), после того, как пользователь угадал число.
3. Добавьте возможность указания правой границы для случайного выбора числа (от 1 до n).
 


