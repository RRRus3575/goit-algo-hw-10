## Висновок

**Обчислення методом Монте-Карло**:

- Метод Монте-Карло використовується для обчислення визначеного інтегралу шляхом генерації випадкових точок у межах інтегрування та оцінки середнього значення функції у цих точках.
- У цьому випадку, ми обчислили інтеграл функції \(f(x) = x^2\) на інтервалі від 0 до 2.
- Результат, отриманий методом Монте-Карло, залежить від кількості згенерованих випадкових точок. При збільшенні кількості точок точність обчислень зростає.

**Перевірка результату за допомогою функції `quad`**:

- Функція `quad` з бібліотеки SciPy використовує більш точний чисельний метод для обчислення визначених інтегралів.
- У нашому випадку, функція `quad` обчислила інтеграл функції \(f(x) = x^2\) на інтервалі від 0 до 2 і надала результат разом з оцінкою помилки.

**Висновок**:

- Метод Монте-Карло є корисним інструментом для оцінки інтегралів, особливо у випадках, коли аналітичне розв'язання є складним або неможливим.
- Однак, для простих функцій і обмежених інтервалів, таких як у нашому прикладі, точніші чисельні методи, такі як ті, що використовуються у функції `quad`, зазвичай надають більш точні результати.
- Метод Монте-Карло може бути менш точним, але з достатньою кількістю випадкових точок він може наблизитися до точного значення інтегралу.

Таким чином, метод Монте-Карло надає гнучкий підхід до чисельного інтегрування, але для підвищення точності його результатів зазвичай потрібно більше обчислювальних ресурсів. У випадках, коли доступні точніші чисельні методи, вони можуть бути більш ефективними та точними.
