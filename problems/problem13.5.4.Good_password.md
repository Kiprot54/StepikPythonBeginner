## Good password

Напишите функцию <code>is_password_good(password)</code>, которая принимает в качестве аргумента
строковое значение пароля <code>password</code> и возвращает значение <code>True</code>,
если пароль является надёжным, или <code>False</code> в противном случае.

Пароль является надёжным, если:
- его длина не менее 8 символов; 
- он содержит как минимум одну заглавную букву (верхний регистр); 
- он содержит как минимум одну строчную букву (нижний регистр);
- он содержит хотя бы одну цифру.

***Примечание.*** Приведённый ниже код:

<pre><code>print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
</code></pre>

должен выводить:

<pre><code>True
False
</code></pre>

<br>

### *Тестовые данные:*

| Номер теста | Входные данные  | Выходные данные |
|:-----------:|-----------------|-----------------|
|      1      | aaAA12qqp       | True            |
|      2      | aa13AN          | False           |
|      3      | aaaaaaaaaaaaa   | False           |
|      4      | AAAAAAAAAAA     | False           |
|      5      | 734638763978653 | False           |
|      6      | AAPPqq9S        | True            |
|      7      | AABBccssss      | False           |
|      8      | AA23423423      | False           |
|      9      | dsas233232232   | False           |
|     10      | 99yyPPgg        | True            |
|     11      | 99yyPPg         | False           |
|     12      | ()+_№;%:        | False           |
|     13      | aaaaaaA@        | False           |