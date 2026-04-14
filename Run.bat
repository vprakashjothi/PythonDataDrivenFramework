@echo off
rmdir /s /q allure-results
rmdir /s /q allure-report

python -m pytest -n 2 --alluredir=allure-results
allure serve allure-results
pause