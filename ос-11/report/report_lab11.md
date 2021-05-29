---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №11"
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

 Изучить основы программирования в оболочке ОС UNIX/Linux. Научиться писать небольшие командные файлы.

# Выполнение лабораторной работы

**1.** Написал скрипт, который при запуске делает резервную копию самого себя (то есть файла, в котором содержится его исходный код). При этом файл архивируется архиватором gzip. Способ использования команд архивации узнал, изучив справку.

![1.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/1.1.png)

(Рис. 1.1)

Его работа:

![1.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/1.2.png)

(Рис. 1.2)

![1.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/1.3.png)

(Рис. 1.3)

![1.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/1.4.png)

(Рис. 1.4)

**2.** Написал пример командного файла, обрабатывающего любое произвольное число аргументов командной строки, в том числе превышающее десять. Скрипт может последовательно распечатывать значения всех переданных аргументов.

![2.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/2.1.png)

(Рис. 2.1)

![2.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/2.2.png)

(Рис. 2.2)

**3.** Написал командный файл, который является аналогом команды ls, без использования самой этой команды и команды dir. Файл выдает информацию о нужном каталоге и выводит информацию о возможностях доступа к файлам этого каталога.

![3.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/3.1.png)

(Рис. 3.1)

![3.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/3.2.png)

(Рис. 3.2)

**4.** Написал командный файл, который получает в качестве аргумента командной строки формат файла (.txt, .doc, .jpg, .pdf и т.д.) и вычисляет количество таких файлов в указанной директории. Путь к директории также передаётся в виде аргумента командной строки.

![4.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/4.1.png)

(Рис. 4.1)

![4.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/11 лабораторная/report/images/4.2.png)

(Рис. 4.2)

# Выводы

В ходе работы изучил основы программирования в оболочке ОС UNIX/Linux и научился писать небольшие командные файлы.

# Использованные ресурсы

https://routerus.com/gzip-command-in-linux/

https://losst.ru/napisanie-skriptov-na-bash

