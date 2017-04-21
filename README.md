#启动django
python manage.py runserver 0.0.0.0:8000

#创建app
python manage.py startapp appname

#创建django工程
djaogo-admin startproject projectname

#生成数据库表
python manage.py makemigrations
python manage.py migrate

#管理员
python manage.py createsuperuser
python manage.py changepassword


"""

    用pymysql插件时需要在__init__.py加上
    import pymysql
    pymysql.install_as_MySQLdb
"""
