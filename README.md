# Лабы сетевое программирование
 > Замечание: *данный репозиторий создан с целью  размещения лабораторных работ по дисциплине "Сетевое Программирование".*
+ ## Лабораторная работа №3,4 "Вывод расписания группы студентов"
	#### **Задания**
	1. Через библиотеку get получить расписание группы студентов с сайта БИИК.
	2. Сделать парсинг кода полученного с сайта.
	3. Сохранить расписание.
	4. Вывести в консоли расписание на завтра.
	#### **Руководство по сборке и запуске проекта**
	1. Клонирование репозитория
		```
		$ git clone https://github.com/MacloMen336/SP_work/
		```
	2. Клонирование репозитория
		```
		установить нужные для выполнения программы библиотеки, указанные в pip.txt
		$ pip install bs4
		$ pip install requests
		```
	3. Замена сайта
		```
		в файле Web_site.py изменить сайт на нужный
		'rasp_i_101': 'YOUR_SITE'
		```
	4. Запуск программы
		```
		$ python3 get.py
		```
