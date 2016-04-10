Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config
We to configure nginx as a reverse proxy server for gunicorn wsgi server.

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com
* then put it under /etc/nginx/sites-available/
* then create a sym link to it under /etc/nginx/sites-enabled/

For example: for superlists.wintextiles.com you can do the following:
```bash
# sed out SITENAME in the template with acutal site name and then
# create the actual conf file under /etc/nginx/sites-available
yan@ec2-server:$ sed "s/SITENAME/superlists.wintextiles.com/g" \
   deploy_tools/nginx.template.conf | sudo tee \
   /etc/nginx/sites-available/superlists.wintextiles.com
# then enable the site. You basically need to create a sym link to the above file
# under /etc/nginx/sites-enabled/
yan@ec2-server:$ sudo ln -s ../sites-available/superlists.wintextiles.com \
   /etc/nginx/sites-enabled/superlists.wintextiles.com
```
Repeat for superlists-staging.wintextiles.com

## Upstart Job 
We need the upstart file so that gunicorn server (which is running the website) will automatically start at boot time.

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

For example: 
```bash
yan@ec2-server:$ sed "s/SITENAME/superlists.wintextiles.com/g" \
    deploy_tools/gunicorn-upstart.template.conf | sudo tee \
    /etc/init/gunicorn-superlists.wintextiles.com
```
Repeat the same for superlists-staging.wintextiles.com

## Folder structure:
Assume we have a user account on the ec2 server at /home/yan.

```
/home/yan

└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
```

