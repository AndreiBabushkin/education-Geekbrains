create database sample; -- Создаю базу данных sample
use sample;
-- Далее выхожу из MySQL
mysqldump-u root-p example > example.sql-- Создаю дамп базы данных example
mysql sample < example.sql -- разворачиваю дамп в базу данных sample




