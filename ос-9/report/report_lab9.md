---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №9"
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

Познакомиться с операционной системой Linux. Получить практические навыки работы с редактором vi, установленным по умолчанию практически во всех дистрибутивах


# Выполнение лабораторной работы

***Задание 1. Создание нового файла с использованием vi***

**1.** Создал каталог с именем ~/work/os/lab06.

Команды: mkdir –p ./work/os/lab06

![2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.png)

**2.** Перешел во вновь созданный каталог.

Команды: cd ./work/os/lab06 

 **3.** Вызвал vi и создал файл hello.sh 

Команды: vi hello.sh

![3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/3.png)

**4.** Нажал клавишу i и ввел следующий текст. 

\#!/bin/bash 

HELL=Hello 

function hello { 

LOCAL HELLO=World 

echo $HELLO

} 

echo $HELLO 

hello 

![4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/4.png)

**5.** Нажал клавишу Esc для перехода в командный режим после завершения ввода текста. 

**6.** Нажал : для перехода в режим последней строки и внизу моего экрана появилось приглашение в виде двоеточия.

![6](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/6.png)

**7.** Нажал w (записать) и q (выйти), а затем нажал клавишу Enter для сохранения моего текста и завершения работы. 

**8.** Сделал файл исполняемым 

Команды: chmod +x hello.sh 

![8](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/8.png)

***Задание 2. Редактирование существующего файла***

**1.** Вызвал vi на редактирование файла 

Команды: vi hello.sh 

![2.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.1.png)

**2.** Установил курсор в конец слова HELL второй строки.

![2.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.2.png)

**3.** Перешел в режим вставки и заменил на HELLO. Нажал Esc для возврата в командный режим.

**4.** Установил курсор на четвертую строку и стёр слово LOCAL командой dw

![2.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.4.png)

**5.** Перешел в режим вставки и набрал следующий текст: local, нажал Esc для возврата в командный режим.

![2.5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.5.png)

**6.** Установил курсор на последней строке файла. Вставил после неё строку, содержащую следующий текст: echo $HELLO.

Команды:G, o

**7.** Нажал Esc для перехода в командный режим. 

![2.7](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.7.png)

**8.** Удалил последнюю строку командой dd

![2.8](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.8.png)

**9.** Ввел команду отмены изменений u для отмены последней команды.

![2.9](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.9.png)

**10.** Ввел символ : для перехода в режим последней строки. Записал произведённые изменения и вышла из vi.

![2.10](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/9 лабораторная/report/images/2.10.png)

# Выводы

Познакомился с операционной системой Linux. Получил практические навыки работы с редактором vi, установленным по умолчанию практически во всех дистрибутивах.