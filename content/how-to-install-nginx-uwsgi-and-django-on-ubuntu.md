Title: How to install and configure Nginx, uWSGI and Django on Ubuntu?
Slug: how-to-install-nginx-uwsgi-and-django-on-ubuntu
Date: 24-04-2013
Category: Howto
Tags: Django, Nginx, uWSGI, Ubuntu, Linux

As a Python and Django developer, one of best and fastest ways to deploy my Web aplications is the combination of [Nginx](http://nginx.org/), the high-performance Web server and [uWSGI](http://projects.unbit.it/uwsgi/).

In this tutorial, I'll describe you how to install and configure Nginx, uWSGI, VirtualENV and Django on Ubuntu.

To install all required applications, open a Terminal and run the following command:

```
sudo apt-get install nginx uwsgi uwsgi-plugin-python python-virtualenv
```

After that, go to your projects directory and create Virtual Python Environment, for example:

```
cd ~/projects
virtualenv venv
```

Activate him with a command:

```
source venv/bin/activate
```

To install Django, you can use [pip](http://www.pip-installer.org/en/latest/) or easy_install tool, I more prefer pip:

```
pip install django
```

Create new Django project:

```
django-admin.py startproject mysite
```

Now, in **/etc/nginx/sites-available** directory, create new file called **mysite.com**:

```
sudo nano /etc/nginx/sites-available/mysite.com
```

And enter the following code in it:

```
server {
  listen  80;
  server_name mysite.com www.mysite.com;
  access_log /var/log/nginx/mysite.com_access.log;
  error_log /var/log/nginx/mysite.com_error.log;

  location / {
    uwsgi_pass  unix:///tmp/mysite.com.sock;
    include     uwsgi_params;
  }

  location /media/  {
    alias /home/USER/projects/mysite/media/;
  }

  location  /static/ {
    alias  /home/USER/projects/mysite/static/;
  }
}
```

This is some basic Nginx configuration. For more, look at the [Nginx documentation](http://nginx.org/en/docs/).

To activate it, you need to create a symbolic link for a file in **/etc/nginx/sites-enabled/**:

```
sudo ln -s /etc/nginx/sites-available/mysite.com /etc/nginx/sites-enabled/
```

Configuration files for uWSGI are stored in **/etc/uwsgi/apps-available**. In this directory create new file called **mysite.com.ini**:

```
sudo nano /etc/uwsgi/apps-available/mysite.com.ini
```

And enter the following code:

```
[uwsgi]
vhost = true
plugins = python
socket = /tmp/mysite.com.sock
master = true
enable-threads = true
processes = 2
wsgi-file = /home/USER/projects/mysite/mysite/wsgi.py
virtualenv = /home/USER/projects/venv
chdir = /home/USER/projects/mysite
touch-reload = /home/USER/projects/mysite/reload
```

Enable it:

```
sudo ln-s /etc/uwsgi/apps-available/mysite.com.ini /etc/uwsgi/apps-enabled/
```

And to the end, restart a services:

```
sudo service nginx restart
sudo service uwsgi restart
```
