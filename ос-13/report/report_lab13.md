---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №13"
subtitle: "Дисциплина: Операционные системы"
author: "Федоров Никита Сергеевич"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Изучить основы программирования в оболочке ОС UNIX. Научиться писать более сложные командные файлы с использованием логических управляющих конструкций и циклов.

# Выполнение лабораторной работы

**1.** Написал командный файл, реализующий упрощённый механизм семафоров. Командный файл в течение 2 сек. дожидается освобождения ресурса, выдавая об этом сообщение, а дождавшись его освобождения, использует его в течение 10 сек., также выдавая информацию о том, что ресурс используется соответствующим командным файлом (процессом). Запустил командный файл в одном виртуальном терминале в фоновом режиме, перенаправив его вывод в другой, в котором также был запущен этот файл, но не фоновом, а в привилегированном режиме.

![1.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/13 лабораторная/report/images/1.1.png)

(Рис. 1.1)

Его работа:

![1.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/13 лабораторная/report/images/1.2.png)

(Рис. 1.2)

![1.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/13 лабораторная/report/images/1.3.png)

(Рис. 1.3)

**2.** Реализовал команду man с помощью командного файла. Изучил содержимое каталога /usr/share/man/man1. В нем находятся архивы текстовых файлов, содержащих справку по большинству установленных в системе программ и команд. Каждый архив можно открыть командой less, сразу же просмотрев содержимое справки. Командный файл получает в виде аргумента командной строки название команды и в виде результата выдаёт справку об этой команде или сообщение об отсутствии справки, если соответствующего файла нет в каталоге man1.

Код скрипта:

![2.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/13 лабораторная/report/images/2.1.png)

(Рис. 2.1)

Его работа:

![2.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/13 лабораторная/report/images/2.2.png)

(Рис. 2.2)

**3.** Используя встроенную переменную $RANDOM, написал командный файл, генерирующий случайную последовательность букв латинского алфавита. Учел, что $RANDOM выдаёт псевдослучайные числа в диапазоне от 0 до 32767 (чтоб получился рандом от 1 до 52, берём остаток от деления $RANDOM на 52 и прибавляем у нему 1).

Код скрипта (в файле 11.txt записаны все заглавные и строчные буквы латинского алфавита по одной в строке):

![3.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/13 лабораторная/report/images/3.1.png)

(Рис. 3.1)

Его работа:

![3.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/13 лабораторная/report/images/3.2.png)

(Рис. 3.2)

# Выводы

Изучил основы программирования в оболочке ОС UNIX. Научился писать более сложные командные файлы с использованием логических управляющих конструкций и циклов.

# Использованные ресурсы

https://ruvds.com/doc/bash.pdf

https://losst.ru/komanda-tar-v-linux

