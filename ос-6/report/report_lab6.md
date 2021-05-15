---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе №6"
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