# Модуль `file_operations`

Небольшой модуль для работы с файлами и шаблонами.

## Как установить

Скопируйте к себе файл [file_operations.py](#file-file_operations-py).

Сразу проверьте работу этого модуля. Подлючите `file_operations.py` к своей программе и попробуйте вывести его версию:

```python3
from file_operations import VERSION

print(VERSION)
```

В консоли отобразится число — версия модуля.

## Как заполнить файл по шаблону

Функция `render_template()` принимает на вход:

- Путь до файла с шаблоном
- Путь, по которому сохранить результат
- Словарь с контекстом

Функция открывает файл и ищет там фразы, выделенные фигурными скобками. Фразы она заменит на строки, которые ей передали. Результат сохранится по указанному пути.

Например, пусть в файле `template.txt` лежит следующий шаблон:
```python3
{name} живёт в {town} и любит {thing}.
```

Заполним шаблон:
```python3
import file_operations

context = {
  "name": "Серёжа",
  "town": "Новосибирске",
  "thing": "яблоки"
}

file_operations.render_template("template.txt", "result.txt", context)
```

Создастся новый файл `result.txt`, в котором будет написано:
```python3
Серёжа живёт в Новосибирске и любит яблоки.
```

## Функция умеет работать с картинками в формате `.svg`.

Например, есть такая картинка `template.svg`:

![sample_text](https://dvmn.org/filer/canonical/1551790036/67/?per=123)

Её тоже можно преобразовать:
```python3
import file_operations

context = {
  "my_text_1": "Презентация",
  "my_text_2": "на тему",
  "my_text_3": "Картинки"
}

file_operations.render_template("template.svg", "result.svg", context)
```
Получится новая картинка:

![sample_text](https://dvmn.org/filer/canonical/1551791313/68/?per=123)

## Пути к файлам

Функция `render_template` работает не с названиями файлов, а с путями к ним. Так, вы можете отделить шаблоны и итоговые SVG от самой программы — её скрипта. Вот пример со структурой катологов:

```
.
├── main.py
├── src
│   └── template.svg
└── output
    └── svg
        └── result.svg
```

Чтобы функция `render_template` нашла файлы передайте ей два относительных пути: один к шаблону и второй к файлу, куда сохранить результат:

```python
file_operations.render_template("src/template.svg", "output/svg/result.svg", {})
```

Обратите внимание на слеши `/`. В OC Linux, Mac или в сервисе Repl.it имена каталогов и файлов в пути разделяются прямым слешем `/`, в Windows для этого используется обратный слеш `\`. Для создания кроссплатформенной программы воспользуйтесь [os.path.join](https://stackoverflow.com/questions/2422798/python-os-path-join-on-windows).