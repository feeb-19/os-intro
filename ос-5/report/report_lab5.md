---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №5"
subtitle: "Дисциплина — Операционные системы"
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

Приобретение практических навыков взаимодействия пользователя с системой посредством командной строки.


# Выполнение лабораторной работы

**1.**Определил полное имя вашего домашнего каталога.

![1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/1.png)

**2.1.** Перешел в каталог /tmp.

![2.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/2.1.png)

**2.2.** Вывел на экран содержимое каталога /tmp. Для этого использовал команду ls с различными опциями. ls без опций выводит просто список файлов. ls –a выводит также имена скрытых файлов. ls –F позволяет узнать тип файлов. ls –l выводит подробную информацию о файлах. Сочетание опций, например, -aFl, позволяет узнавать информацию, выводимую при использовании каждой из этих опций.

 ![2.2.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/2.2.1.png)

![2.2.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/2.2.2.png)

![2.2.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/2.2.3.png)

![2.2.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/2.2.4.png)

![2.2.5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/2.2.5.png)

**2.3.** Определил, что в каталоге /var/spool есть подкаталог с именем cron
![2.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/2.3.png)

**2.4.** Перешел в свой домашний каталог и вывела на экран его содержимое. Владельцем файлов и каталогов являюсь я.

![2.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/2.4.png)

**3.1.** В домашнем каталоге создал новый каталог с именем newdir. 

**3.2.** В каталоге ~/newdir создал новый каталог с именем morefun.
![3.1-3.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/3.1-3.2.png)

**3.3.** В домашнем каталоге создал одной командой три новых каталога с име- нами letters, memos, misk. Затем удалил эти каталоги одной командой. 

![3.3.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/3.3.1.png)

![3.3.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/3.3.2.png)

**3.4.** Попробовал удалить ранее созданный каталог ~/newdir командой rm. Каталог не был удалён.![3.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/3.4.png)

**3.5.** Удалил каталог ~/newdir/morefun из домашнего каталога. Каталог был удалён
![3.5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/3.5.png)

**4.** С помощью команды man определил, какую опцию команды ls нужно использовать для просмотра содержимого не только указанного каталога, но и подкаталогов, входящих в него – это опция -R. 
![4.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/4.1.png)

![4.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/4.2.png)



**5.** С помощью команды man определил набор опций команды ls, позволяющий отсортировать по времени последнего изменения выводимый список содержимого каталога с развёрнутым описанием файлов. Это опции –lt.

![5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/5.png)

**6.** Использовал команду man для просмотра описания следующих команд: cd, pwd, mkdir, rmdir, rm.  

![6.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/6.1.png)

Опции cd:
 **-P** — позволяет следовать по символическим ссылкам перед тем, как будут обработаны все переходы «..»

**-L** — переходит по символическим ссылкам только после того, как были обработаны «..»;

Опции pwd:

**-L**- Выводить логическое имя текущего рабочего каталога

**-P** - Выводить физическое имя текущего рабочего каталога (все символические ссылки разыменовываются)

![6.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/6.3.png)

Опции mkdir:

**-m** – задание режима доступа

**-p** – позволяет создавать сразу несколько вложенных каталогов. Например, с использованием этой опции можно создать каталог /tmp/local, даже если каталога /tmp до этого не существовало.

![6.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/6.4.png)

Опции rmdir:

**-p** – удаляет не только выбранный каталог, но и все вышележащие пустые каталоги

![6.5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/6.5.png)

Опции rm:

**-f** – не выдаются сообщения о несуществующих файлах или файлах, прав на удаление которых у пользователя нет. Сообщение об ошибке выводится только при попытке удаления каталога.

**-i** – при удалении выводится запрос подтверждения

**-r, -R** -  удаление рекурсивно. Позволяет удалять каталоги с содержимым

**-d** – удаление пустых каталогов.

![6.6](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/6.6.png)

**7.** Используя информацию, полученную при помощи команды history, выполнил модификацию и исполнение нескольких команд из буфера команд.!

![7.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/7.1.png)

![7.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/5 лабораторная/report/images/7.2.png)

# Выводы

Я приобрел практических навыков взаимодействия пользователя с системой посредством командной строки.