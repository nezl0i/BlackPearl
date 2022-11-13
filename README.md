## Проект "Блог статей команды BlackPearl"
## Командная разработка по методологии Agile:Scrum

Основные системные требования:

* Win 8-10 или Ubuntu 16.04.6 LTS и выше
* Python 3.10
* SQLite 3.
* Django 4.0
* Зависимости из requirements.txt

### Установка:

1. Клонируем репозиторий:
```
git clone git@github.com:nezl0i/BlackPearl.git
```
2. Создаем виртуальное окружение и входим в него:
```
python3 -m venv venv
venv\Scripts\activate 
```
  Данный путь может отличаться в зависимости от системы.
  
3. Устанавливаем зависимости:
```
pip install -r {path_to_requirements}/requirements.txt
```
4. Подготавливаем настройки и БД:

  Создаем серектный ключ
```
nano .env		# Вводим SECRET_KEY
```
  Делаем миграции
```
python manage.py makemigrations
python manage.py migrate
```
  Создаем суперпользователя 
```     
python manage.py createsuperuser
```
### Установка тестовой базы данных:
Файл дампа тестовой базы данных можно забрать в ветке nezl0i_devel/backend/backup_13.11.json
Для установки проверьте миграции и используйте:
```
py manage.py loaddata {path_to_dump_data}/backup_13.11.json
```
  
### Запуск:
```
python manage.py runserver
```
После запуска будет показан IP. Вводим его в адресную строку браузера и наслаждаемся проектом. 


