:: В каталоге проекта ibcntr (в среде venv)
:: - обновляет модули из requirements.txt
:: - если файл базы данных отсутствует или нулевой длины - создает базу данных
:: - запускает проект
@echo off
Set db=ibcntr\db.sqlite
Set /a new_db=0
@echo renew requirements.txt
@pip freeze > requirements.txt

if NOT exist %db% Set /a new_db=1
FOR %%I IN (%db%) DO Set sz=%%~zI
if '%sz%'=='0' Set /a new_db=1

if %new_db% EQU 1 (
	echo create empty database
	python -c "from ibcntr import db, create_app, models; db.create_all(app=create_app())"
)

flask run