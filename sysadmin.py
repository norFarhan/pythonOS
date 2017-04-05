#!/usr/bin/python

import os
from subprocess import Popen,PIPE


os.system('echo "This script will install LAMP stack, start services, auto enable httpd and mysqld'
          'and setup phpinfo page"')
respond = ''

# process = Popen(['apt-get', 'update'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()

respond = raw_input('are sure want to continue? y to continue n to abort :')


def installWget():
    print "Installing wget"
    os.system("yum install wget -y")
    # install = Popen(['apt-get', 'install', 'wget'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = install.communicate()
    # print stdout, stderr
    return



def installApache():
    print "Installing Apache"
    os.system("yum install httpd -y")
    # install = Popen(['yum', 'install', 'httpd'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = install.communicate()
    # print stdout
    return

def installMysql():
    print "Installing Mysql"
    os.system("yum install mysql-server -y")
    # install = Popen(['yum', 'install', 'mysql-server'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = install.communicate()
    # print stdout
    return

def installPhp():
    print "Installing php"hut
    os.system("yum install php php-mysql -y")
    # install = Popen(['yum', 'install', 'php', 'php-mysql'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = install.communicate()
    # print stdout
    return


def checkPhp():
    os.system('echo "<?php phpinfo() ?>" > /var/www/html/index.php')
    print "write index.php"
    return

def configureLAMP():
    os.system("service httpd start")
    # httpd = Popen(['service', 'httpd', 'start'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = httpd.communicate()
    # print stdout
    print "start httpd"
    os.system("service mysqld start")
    # mysqld = Popen(['service', 'mysqld', 'start'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = mysqld.communicate()
    # print stdout
    print "start mysqld"
    os.system("chkconfig httpd on")
    # chkconfigHttpd = Popen(['chkconfig', 'httpd', 'on'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = chkconfigHttpd.communicate()
    # print stdout
    print "enable httpd on boot"
    os.system("chkconfig mysqld on")
    # chkconfigMysqld = Popen(['chkconfig', 'mysql', 'on'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = chkconfigMysqld.communicate()
    # print stdout
    print "enable mysql on boot"
    return

if respond == 'y':
    installWget()
    installApache()
    installMysql()
    installPhp()
    configureLAMP()
    checkPhp()

else: exit(0)


