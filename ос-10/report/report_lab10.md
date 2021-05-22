---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №10"
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

Познакомиться с операционной системой Linux. Получить практические навыки работы с редактором Emacs.


# Выполнение лабораторной работы

**1.** Открыл emacs. 

![Screenshot 2021-05-22 at 20.19.53](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.19.53.png)

**2.** Создал файл lab07.sh с помощью комбинации Ctrl-x Ctrl-f (C-x C-f). 

![Screenshot 2021-05-22 at 20.20.15](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.20.15.png)

**3.** Набрал текст: 

\#!/bin/bash 

HELL=Hello 

function hello { 

LOCAL HELLO=World 

echo $HELLO

} 

echo $HELLO

hello 

![Screenshot 2021-05-22 at 20.20.31](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.20.31.png)

**4.** Сохранил файл с помощью комбинации Ctrl-x Ctrl-s (C-x C-s). 

**5.** Проделал с текстом стандартные процедуры редактирования, каждое действие осуществил комбинацией клавиш. 

**5.1.** Вырезал одной командой целую строку (С-k).

![Screenshot 2021-05-22 at 20.20.45](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.20.45.png)

**5.2.** Вставил эту строку в конец файла (C-y). 

![Screenshot 2021-05-22 at 20.20.54](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.20.54.png)

**5.3.** Выделил область текста (C-space). 

![Screenshot 2021-05-22 at 20.21.01](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.21.01.png)

**5.4.** Скопировал область в буфер обмена (M-w). 

**5.5.** Вставил область в конец файла.

![Screenshot 2021-05-22 at 20.21.08](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.21.08.png)

**5.6.** Вновь выделил эту область и на этот раз вырезал её (C-w). 

![Screenshot 2021-05-22 at 20.21.20](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.21.20.png)

**5.7.** Отменил последнее действие (C-x u). 

![Screenshot 2021-05-22 at 20.21.27](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.21.27.png)

**6.** Научился использовать команды по перемещению курсора. 

**6.1.** Переместил курсор в начало строки (C-a). 

![Screenshot 2021-05-22 at 20.21.39](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.21.39.png)

**6.2.** Переместил курсор в конец строки (C-e).

![Screenshot 2021-05-22 at 20.22.36](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.22.36.png)

**6.3.** Переместил курсор в начало буфера (M-<). 

![Screenshot 2021-05-22 at 20.22.48](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.22.48.png)

**6.4.** Переместил курсор в конец буфера (M->).

![Screenshot 2021-05-22 at 20.22.55](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.22.55.png)

**7.** Управление буферами. 

**7.1.** Вывел список активных буферов на экран (C-x C-b). 

![Screenshot 2021-05-22 at 20.23.06](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.23.06.png)

**7.2.** Переместился во вновь открытое окно (C-x) o со списком открытых буферов и переключился на другой буфер. 

![Screenshot 2021-05-22 at 20.23.12](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.23.12.png)

![Screenshot 2021-05-22 at 20.23.25](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.23.25.png)

![Screenshot 2021-05-22 at 20.23.32](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.23.32.png)

**7.3.** Закрыл это окно (C-x 0). 

![Screenshot 2021-05-22 at 20.23.40](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.23.40.png)

**7.4.** Теперь вновь переключался между буферами, но уже без вывода их списка на экран (C-x b).

![Screenshot 2021-05-22 at 20.23.51](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.23.51.png)

**8.** Управление окнами. 

**8.1.** Поделил фрейм на 4 части: разделил фрейм на два окна по вертикали (C-x 3), а затем каждое из этих окон на две части по горизонтали (C-x 2)

![Screenshot 2021-05-22 at 20.24.00](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.24.00.png)

![Screenshot 2021-05-22 at 20.24.06](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.24.06.png)

**8.2.** В каждом из четырёх созданных окон открыл новый буфер (файл) и ввел несколько строк текста. 

![Screenshot 2021-05-22 at 20.24.23](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.24.23.png)

**9.** Режим поиска 

**9.1.** Переключился в режим поиска (C-s) и нашел несколько слов, присутствующих в тексте.

![Screenshot 2021-05-22 at 20.24.32](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.24.32.png)

**9.2.** Переключался между результатами поиска, нажимая C-s. 

![Screenshot 2021-05-22 at 20.24.41](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.24.41.png)

**9.3.** Вышел из режима поиска, нажав C-g.

![Screenshot 2021-05-22 at 20.24.48](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.24.48.png)

**9.4.** Перешел в режим поиска и замены (M-%), ввел текст, который следует найти и заменить, нажал Enter , затем ввел текст для замены. После того как были подсвечены результаты поиска, нажал ! для подтверждения замены. 

![Screenshot 2021-05-22 at 20.25.03](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.25.03.png)

![Screenshot 2021-05-22 at 20.25.14](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.25.14.png)

**9.5.** Испробовал другой режим поиска, нажав M-s o. В отличие от обычного режима, найденный текст не подсвечивается в текущем окне, а выводится в отдельном, при чём выводится вся строка, где был найден этот текст, а также её номер

![Screenshot 2021-05-22 at 20.25.22](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/10 лабораторная/report/images/Screenshot 2021-05-22 at 20.25.22.png)

# Выводы

Познакомился с операционной системой Linux. Получил практические навыки работы с редактором Emacs.