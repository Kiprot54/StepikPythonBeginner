## Змеиный регистр

Напишите функцию <code>convert_to_python_case(text)</code>, которая принимает в качестве аргумента строку
в «верблюжьем регистре» и преобразует его в «змеиный регистр».

***Примечание 2.*** Приведённый ниже код:

<pre><code>print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
</code></pre>

должен выводить:

<pre><code>this_is_camel_cased
is_prime_number
</code></pre>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные          | Выходные данные             |
|:-----------:|-------------------------|-----------------------------|
|      1      | ThisIsCamelCased        | this_is_camel_cased         |
|      2      | IsPrimeNumber           | is_prime_number             |
|      3      | ConvertToInt32          | convert_to_int32            |
|      4      | MyMethodThatDoSomething | my_method_that_do_something |
|      5      | IsHeFreeToG             | is_he_free_to_go            |
|      6      | FBIIsWatchingYou        | f_b_i_is_watching_you       |