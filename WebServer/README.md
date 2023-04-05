I am running my webserver on Apache 2.0 !

To install apache 2.0 on your Pi :  sudo apt-get install apache2
To check your Pi ip : hostname -I 

Now type your Pi ip on your browser : http://"YOUR_IP"/ 
* For example : http://192.186.1.2/ . This page should show basic information about Apache server written in the file index.html on your Pi!
* index.html is located in : /var/www/html/index.html

Now we can delete index.html and create a clean one with the same name as we want to write our own web page!
To remove a file in system files you should have root access in the terminal:
* You can write sudo before every command : sudo rm index.html
* You can have root access everytime : sudo su  and if required enter your Pi password!
* To remove a file : (sudo) rm index.html
* To create a new one : (sudo) touch index.html

Further I will be in root access , so I will not use sudo in every command line!

Now you should enable cgi scripts run by apache2!

1) create cgi-bin direction next to html direction in /var/www/
2) Open the file "/etc/apache2/sites-enabled/000-default.conf"
3) Put this lines in to the file: 
    ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
    <Directory "/var/www/cgi-bin/">
    Options +ExecCGI
    AddHandler cgi-script .cgi
    Order allow,deny
    Allow from all
    </Directory>
4) enter command : a2enmod cgi 
5) restart apache2 : systemctl restart apache2

* If your apache can not restart : go the /etc/apache2/ and type : apache2ctl configtest
This should tell the mistakes you made in 000-default.conf by enabling cgi scripts!

You can create your cgi scripts in your cgi-bin direction!
* After creating your cgi script file, you should make them executable by : chmod +x "filename.cgi"

To access : your cgi script on the browser : "ip_of_pi"/cgi-bin/"filename-cgi"

Try example date.cgi which shows date on the browser!
