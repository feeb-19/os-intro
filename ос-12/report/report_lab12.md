---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №12"
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

Изучить основы программирования в оболочке ОС UNIX. Научится писать более сложные командные файлы с использованием логических управляющих конструкций и циклов.

# Выполнение лабораторной работы

**1.** Используя команды getopts grep, написал командный файл, который анализирует командную строку с ключами: 

– -i inputfile — прочитать данные из указанного файла; 

– -o outputfile — вывести данные в указанный файл; 

– -p шаблон — указать шаблон для поиска; 

– -C — различать большие и малые буквы; 

– -n — выдавать номера строк.

а затем ищет в указанном файле нужные строки, определяемые ключом -p. 

![1.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/1.1.png)

(Рис. 1.1)

Его работа:

![1.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/1.2.png)

(Рис. 1.2)

![1.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/1.3.png)

(Рис. 1.3)

![1.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/1.4.png)

(Рис. 1.4)

![1.5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/1.5.png)

(Рис. 1.5)

![1.6](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/1.6.png)

(Рис. 1.6)![1.7](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/1.7.png)

(Рис. 1.7)

![1.8](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/1.8.png)

(Рис. 1.8)

**2.** Написал на языке Си программу, которая вводит число и определяет, является ли оно больше нуля, меньше нуля или равно нулю. Затем программа завершается с помощью функции exit(n), передавая информацию о коде завершения в оболочку. Командный файл вызывает эту программу и, проанализировав с помощью команды $?, выдаёт сообщение о том, какое число было введено. 

Код на C++:

![2.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/2.1.png)

(Рис. 2.1)

Код скрипта:

![2.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/2.2.png)

(Рис. 2.2)

Его работа:

![2.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/2.3.png)

(Рис. 2.3)

![2.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/2.4.png)

(Рис. 2.4)

**3.** Написал командный файл, создающий указанное число файлов, пронумерованных последовательно от 1 до N (например, 1.tmp, 2.tmp, 3.tmp,4.tmp и т.д.). Число файлов, которые необходимо создать, передаётся в аргументы командной строки. Этот же командный файл удаляет все созданные им файлы (если они существуют). 

Код скрипта:

![3.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/3.1.png)

(Рис. 3.1)

Его работа:

![3.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/3.2.png)

(Рис. 3.2)

**4.** Написал командный файл, который с помощью команды tar запаковывает в архив все файлы в указанной директории. Модифицировала его так, чтобы запаковывались только те файлы, которые были изменены менее недели тому назад (использовав команду find).

Код скрипта:

![4.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/4.1.png)

(Рис. 4.1)

Его работа:

![4.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/4.2.png)

(Рис. 4.2)

![4.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/4.3.png)

(Рис. 4.3)

После модификации:

![4.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/4.4.png)

(Рис. 4.4)

![4.5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/4.5.png)

(Рис. 4.5)

![4.6](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/12 лабораторная/report/images/4.6.png)

(Рис. 4.6)

# Выводы

Изучил основы программирования в оболочке ОС UNIX. Научился писать более сложные командные файлы с использованием логических управляющих конструкций и циклов.

# Использованные ресурсы

https://ruvds.com/doc/bash.pdf

https://losst.ru/komanda-tar-v-linux

