# Web-tools

### Описание проекта 

Сайт с микро-инструментами, которые я сам периодически могу использовать при работе в интернете. Среди них — сжатие картинок, сокращение ссылок, транслитерация текста на латиницу для поисковиков, подсчет количества символов, генератор паролей, получение информации о домене и скачивание видео с платформы YouTube.
 
Реализован на фреймворке FastAPI.

![image](https://user-images.githubusercontent.com/113205906/222952482-a924894e-c7a5-4fe9-b837-5d15c9cfc645.png)
  
Ссылка: https://web-tools.webtm.ru/  
  
• Для CRUD-методов использовался SQLAlchemy.  
• Фронтэнд-часть представлена шаблонами Jinja2 и JS-скриптами.   
• Для микро-инструментов использовались различные python-библиотеки, либо внутренняя логика.    
• В качестве базы данных используется PostgreSQL.  
• Деплой производился с помощью Docker Compose в связке с Nginx.  
• Ssl-сертификат сгенерирован с помощью центра сертификации Let's encrypt. 


### Стэк разработки:

• FastAPI: 0.85.0   
• Uvicorn: 0.18.3   
• Jinja2: 3.1.2    
• PostgreSQL, Psycopg2-binary: 2.9.5  
• SQLAlchemy: 1.4.44  
• Python-whois: 0.8.0  
• Pytube: 12.1.0   
и другие. Подробнее в **requirements.txt**

### Запуск

Файл docker-compose размещается в стартовый каталог на сервере.  

Команда для запуска:  
```docker
docker compose -f docker-compose.yaml up -d
```

Локальный запуск самого приложения без базы данных прокси-сервера:  
```python
uvicorn main:app –reload –port 8000
```
