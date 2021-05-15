---
## Front matter
lang: ru-RU
title: Structural approach to the deep learning method
author: |
	Leonid A. Sevastianov\inst{1,3}
	\and
	Anton L. Sevastianov\inst{1}
	\and
	Edik A. Ayrjan\inst{2}
	\and
	Anna V. Korolkova\inst{1}
	\and
	Dmitry S. Kulyabov\inst{1,2}
	\and
	Imrikh Pokorny\inst{4}
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
	\and
	\inst{2}LIT JINR, Dubna, Russian Federation
	\and
	\inst{3}BLTP JINR, Dubna, Russian Federation
	\and
	\inst{4}Technical University of Košice, Košice, Slovakia
date: NEC--2019, 30 September -- 4 October, 2019 Budva, Montenegro

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
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