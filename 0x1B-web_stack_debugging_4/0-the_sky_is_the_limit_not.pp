#Testing how well our web server setup featuring Nginx is doing under pressure 
exec { 'nginx limit':
    command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
    provider => shell,
}
