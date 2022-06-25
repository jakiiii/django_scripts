## GUNICORN CONFIGURATION
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sammy/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```


## NGINX CONFIGURATION
```
server{
        listen 80;
        server_name <domain_name>;

        location /static/ {
                root /home/dev/culture_website/main/static;
        }

        location /media/ { 
                root /home/dev/culture_website
        }

        location / { 
                include proxy_params;
                proxy_pass http://unix:/home/dev/culture_website;
        }
}
```

