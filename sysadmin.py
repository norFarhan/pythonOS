#!/usr/bin/python

import os


os.system('echo "This script will install LAMP stack, start services, auto enable httpd and mysqld'
          'and setup phpinfo page"')
respond = ''


respond = raw_input('are sure want to continue? y to continue n to abort :')

def installWget():
    print "Installing wget"
    os.system("apt-get install wget -y")
    return

def installApache():
    print "Installing Apache"
    os.system("apt-get install apache2 -y")
    return

def installMysql():
    print "Installing Mysql"
    os.system("apt-get install mysql-server -y")
    return

def installPhp():
    print "Installing Php and all dependencies"
    os.system("apt-get install php7.0 libapache2-mod-php7.0 -y")
    return


def checkPhp():
    os.system('echo "<?php phpinfo() ?>" > /var/www/html/index.php')
    print "Create index.php"
    return

def configureLAMP():

	# Services
    print "Starting Apache2"
    os.system("service apache2 start")
    print "Starting Mysql"
    os.system("service mysql start")

	# On boot enable
    print "Enabling Apache2 and Mysql start on boot"
    os.system("systemctl enable apache2 && systemctl enable mysql")
    return

if respond == 'y':
    installWget()
    installApache()
    installMysql()
    installPhp()
    configureLAMP()
    checkPhp()

else: exit(0)
