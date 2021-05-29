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

