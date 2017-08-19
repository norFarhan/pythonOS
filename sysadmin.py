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
    print "Installing php"
    os.system("apt-get install php php-mysql -y")
    return


def checkPhp():
    os.system('echo "<?php phpinfo() ?>" > /var/www/html/index.php')
    print "write index.php"
    return

def configureLAMP():
    os.system("service httpd start")
    print "start httpd"
    os.system("service mysqld start")
    print "start mysqld"
    os.system("chkconfig httpd on")
    print "enable httpd on boot"
    os.system("chkconfig mysqld on")
    print "enable mysql on boot"
    return

if respond == 'y':
    installWget()
    installApache()
    installMysql()
    installPhp()
    # configureLAMP()
    checkPhp()

else: exit(0)
