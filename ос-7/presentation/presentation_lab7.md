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