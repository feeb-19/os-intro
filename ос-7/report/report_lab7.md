---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №7"
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

Ознакомление с инструментами поиска файлов и фильтрации текстовых данных. Приобретение практических навыков по управлению процессами (и заданиями), по проверке использования диска и обслуживанию файловых систем.


# Выполнение лабораторной работы

**1.** Осуществил вход в систему, используя соответствующее имя пользователя.

**2.** Записал в файл file.txt названия файлов, содержащихся в каталоге /etc. Дописал в этот же файл названия файлов, содержащихся в вашем домашнем каталоге.

![Screenshot 2021-05-14 at 18.22.37](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/2.1.png)

Запустил ls с выводом в консоль для проверки записанного в файл:

![Screenshot 2021-05-14 at 18.24.33](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/2.2.png)

![Screenshot 2021-05-14 at 18.24.38](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/2.3.png)

Всё записалось верно.

**3.** Вывел имена всех файлов из file.txt, имеющих расширение .conf, после чего запиcал их в новый текстовой файл conf.txt. ![3.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/3.1.png)

![3.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/3.2.png)

**4.** Определил, какие файлы в вашем домашнем каталоге имеют имена, начинающиеся с символа c. Сделала это двумя способами.

![4.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/4.1.png)

В отличие от find, grep не выводит скрытые файлы.

![4.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/4.2.png)

**5.** Вывел на экран (постранично) имена файлов из каталога /etc, начинающиеся с символа h.

![5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/5.png)

…

**6-7.** Запустил в фоновом режиме процесс, который будет записывать в файл ~/logfile файлы, имена которых начинаются с log. Удалила файл ~/logfile.

![6](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/6.png)

 **8.** Запустил из консоли в фоновом режиме редактор gedit

 **9.** Определил идентификатор процесса gedit, используя команду ps, конвейер и фильтр grep. Идентификатор можно определить более простым способом – он выводится при запуске процесса.

![8](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/8.png)

**10.** Прочел справку (man) команды kill, после чего использовал её для завершения процесса gedit.

![10.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/10.1.png)

![10.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/10.2.png)

 **11.** Выполнил команды df и du, предварительно получив более подробную информацию об этих командах, с помощью команды man.

![11.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/11.1.png)

![11.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/11.2.png)

**12.** Воспользовавшись справкой команды find, вывел имена всех директорий, имеющихся в моём домашнем каталоге.

![12](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/7 лабораторная/report/images/12.png)

# Выводы

Ознакомился с инструментами поиска файлов и фильтрации текстовых данных. Приобрел практические навыки по управлению процессами (и заданиями), по проверке использования диска и обслуживанию файловых систем.