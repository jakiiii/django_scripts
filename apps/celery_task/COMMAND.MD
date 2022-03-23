# Celery Command

### Install RabbitMQ (Ubuntu Linux 20.04LTS)
    sudo apt-get install rabbitmq-server


#### Run RabbitMQ-Server:**
    sudo systemctl start rabbitmq-server
    sudo systemctl stop rabbitmq-server
    sudo systemctl status rabbitmq-server


### Install celery
    pip install celery

#### Run celery for task:
    celery -A <project_name> worker -l info
    celery -A <project_name> worker --loglevel=info
    celery -A NAMEOFINSTANCE worker --loglevel=info
    
    [Windows OS]
    celery -A core worker -l info --pool=solo


### Start Flower:
    celery -A django_scripts flower --port=5555

flower documentation: [https://flower.readthedocs.io/en/latest/]

### django-celery-beat:
    celery -A <project_name> beat -l INFO  # For deeper logs use DEBUG
    celery -A <project_name> worker -B -l INFO

*You can also embed beat inside the worker by enabling the workers -B option*

####Database scheduler
    celery -A <project_name> beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler


## crontab() Execute every minute.
    crontab(minute=0, hour=0) Execute daily at midnight.
    
    crontab(minute=0, hour='*/3') Execute every three hours: midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm.
    
    crontab(minute=0, hour='0,3,6,9,12,15,18,21') Same as previous.
    
    crontab(minute='*/15') Execute every 15 minutes.
    
    crontab(day_of_week='sunday') Execute every minute (!) at Sundays.
    
    crontab(minute='*', hour='*', day_of_week='sun') Same as previous.
    
    crontab(minute='*/10', hour='3,17,22', day_of_week='thu,fri') Execute every ten minutes, but only between 3-4 am, 5-6 pm, and 10-11 pm on Thursdays or Fridays.
    
    crontab(minute=0, hour='*/2,*/3') Execute every even hour, and every hour divisible by three. This means: at every hour except: 1am, 5am, 7am, 11am, 1pm, 5pm, 7pm, 11pm
    
    crontab(minute=0, hour='*/5') Execute hour divisible by 5. This means that it is triggered at 3pm, not 5pm (since 3pm equals the 24-hour clock value of “15”, which is divisible by 5).
    
    crontab(minute=0, hour='*/3,8-17') Execute every hour divisible by 3, and every hour during office hours (8am-5pm).
    
    crontab(0, 0, day_of_month='2') Execute on the second day of every month.
    
    crontab(0, 0, day_of_month='2-30/2') Execute on every even numbered day.
    
    crontab(0, 0, day_of_month='1-7,15-21') Execute on the first and third weeks of the month.
    
    crontab(0, 0, day_of_month='11', month_of_year='5') Execute on the eleventh of May every year.
    
    crontab(0, 0, month_of_year='*/3') Execute every day on the first month of every quarter.


### # CELERY CACHE
    python manage.py createcachetable --dry-run
