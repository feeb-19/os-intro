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
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono

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



