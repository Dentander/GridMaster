# GridMaster - язык программирования движения исполнителя по двумерной сетке
Команда 4FUN представляет приложение, позволяющее начинающим программистам начать свой путь изучения с простого и наглядного языка програмирования - GridMaster

### Пример работы проекта
![screenshot](https://github.com/Dentander/GridMaster/assets/86656216/5915f04f-1b73-4d14-bc63-596c8dffc684)
### Структура проекта
![structure](https://github.com/Dentander/GridMaster/assets/86656216/aa5ebf14-f48f-4edc-9a2f-266c42619970)
Command – базовый класс от которого все остальные команды наследуются. Они делятся на 4 вида:

•	 Blocks – команды с вложенными структурами

•	 Movement – команды отвечающие за передвижение

•	 Variables - команды отвечающие за работу с переменными

•	 Unknown – команды отвечающие за обработку неизвестных команд 

Все эти команды добавляются в Interpreter. Он предоставляет функционал, который GUI привязывает к интерфейсу.
# Скачивание
### Проекта для пользователей Windows
1) Скачиваете [ZIP архив](https://github.com/Dentander/GridMaster/releases/download/Windows/GridMaster.-.Windows.zip)
2) Разорхивируйте
3) Звпустите GridMaster.exe) 
### Проекта для пользователей Linux

### Исходного кода
1) Запускаете PyCharm
2) Нажимаете Get From VCS
3) В URL указываете https://github.com/Dentander/GridMaster
4) Нажимаете Clone -> Trust Project -> Install Requirement 
5) Нажимаете Run и готово)
