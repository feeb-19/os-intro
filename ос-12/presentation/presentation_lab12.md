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

