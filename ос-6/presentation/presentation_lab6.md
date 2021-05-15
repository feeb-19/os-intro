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

Ознакомление с файловой системой Linux, её структурой, именами и содержанием каталогов. Приобретение практических навыков по применению команд для работы с файлами и каталогами, по управлению процессами (и работами), по проверке использования диска и обслуживанию файловой системы.


# Выполнение лабораторной работы

1. Выполнил все примеры, приведённые в первой части описания лабораторной работы.![1.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.1.png)

![1.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.2.png)

![1.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.3.png)

![1.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.4.png)

![1.5](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.5.png)

![1.6](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.6.png)

![1.7](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.7.png)

![1.8](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.8.png)

![1.9](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.9.png)

![1.10](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.10.png)

![1.11](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.11.png)

![1.12](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/1.12.png)

2. Выполнил следующие действия, зафиксировав в отчёте по лабораторной работе используемые при этом команды и результаты их выполнения: 

2.1. Скопировал файл /usr/include/linux/uio.h (т.к. каталога /usr/include /sys не было) в домашний каталог и назвала его equipment.

![2.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/2.1.png)

2.2. В домашнем каталоге создал директорию ~/ski.plases. 

Команды: mkdir ski.plases

2.3. Переместил файл equipment в каталог ~/ski.plases.

Команды: mv equipment ski.plases

2.4. Переименовал файл ~/ski.plases/equipment в ~/ski.plases/equiplist. 

Команды: mv ski.plases/equipment ski.plases/equiplist

![2.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/2.2.png)

2.5. Создал в домашнем каталоге файл abc1 и скопировал его в каталог ~/ski.plases, назвал его equiplist2. 

Команды: touch abc1, cp abc1 ski.plases/equiplist2

![2.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/2.3.png)

2.6. Создал каталог с именем equipment в каталоге ~/ski.plases. 

Команды: mkdir ski.plases/equipment

2.7. Переместил файлы ~/ski.plases/equiplist и equiplist2 в каталог ~/ski.plases/equipment. 

Команды: mv ski.plases/equiplist ski.plases/equiplist2 ski.plases/equipment

2.8. Создал и переместил каталог ~/newdir в каталог ~/ski.plases и назвала его plans.

Команды: mkdir newdir, mv newdir ski.plases/plans

![2.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/2.4.png)

3. Определила опции команды chmod, необходимые для того, чтобы присвоить перечисленным ниже файлам выделенные права доступа, считая, что в начале таких прав нет: 

3.1. drwxr--r-- ... australia 

3.2. drwx--x--x ... play 

3.3. -r-xr--r-- ... my_os 

3.4. -rw-rw-r-- ... feathers

![3.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/3.1.png)

4. Проделал приведённые ниже упражнения, записывая в отчёт по лабораторной работе используемые при этом команды: 

4.1. Просмотрел содержимое файла /etc/password. 

![4.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/4.1.png)

4.2. Скопировал файл ~/feathers в файл ~/file.old. 

4.3. Переместил файл ~/file.old в каталог ~/play. 

4.4. Скопировал каталог ~/play в каталог ~/fun. 

4.5. Переместил каталог ~/fun в каталог ~/play и назвала его games. 

4.6. Лишил владельца файла ~/feathers права на чтение. 

4.7. Если попытаться просмотреть файл ~/feathers командой cat, будет отказано в доступе.

4.8 Если попытаться скопировать файл ~/feathers, будет отказано в доступе.

4.9. Дал владельцу файла ~/feathers право на чтение. 

4.10. Лишил владельца каталога ~/play права на выполнение. 

4.11. Перешел в каталог ~/play. Переход не был совершен из-за отказа в доступе. 

4.12. Дал владельцу каталога ~/play право на выполнение. 

![4.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/4.2.png)

5. Прочитал man по командам mount, fsck, mkfs, kill.

Команда mount используется для монтирования файловых систем.
Пример: mount –t ntfs /dev/cdrom ~/play

![5.1](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/5.1.png)

 Команда fsck выполняет проверку целостности файловой системы, т.е. её проверку на ошибки.
 Пример: fsck –p исправит мелкие неполадки в файловых системах по умолчанию.

![5.2](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/5.2.png)

Команда mkfs используется для создания файловых систем.

Пример: mkfs –t vfat /dev/hdb2 отформатирует диск hdb2 в fat 

![5.3](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/5.3.png)

Команда kill используется для принудительного завершения работы приложений

Пример: kill SIGKILL PID1 немедленно завершит процесс, PID которого равен PID1

![5.4](/Users/nikitafedorov/Desktop/STUDY/Операционные системы/6 лабораторная/report/images/5.4.png)

# Выводы

Ознакомился с файловой системой Linux, её структурой, именами и содержанием каталогов. Приобрел практические навыки по применению команд для работы с файлами и каталогами, по управлению процессами (и работами), по проверке использования диска и обслуживанию файловой системы.