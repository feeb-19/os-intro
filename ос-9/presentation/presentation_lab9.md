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