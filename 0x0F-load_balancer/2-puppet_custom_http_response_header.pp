# creating a puppet to set up a nginx web server on a server
# the nginx should listen to port 80
# The redirection must be a "301 Moved Permanently"

# update the server
exec { 'apt-update':
  command => 'apt-get -y update',
  path    => '/usr/bin',
}

# install nginx
package { 'nginx':
  ensure => installed,
}

# allow the webserver to listion on port 80
exec { 'Nginx HTTP':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
}

# ensure this directory has the mode
file { '/var/www':
  ensure => 'directory',
  mode   => '0755'
}

# ensure a /var/www/html is present
file { '/var/www/html':
  ensure => 'directory',
}

# create a file with a content
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!'
}

# create a file with a content
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!'
}

$serverblock="server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;
        # add a custom header to the response header
        add_header X-Served-By ${hostname};

        location /redirect_me {
                # First attempt to serve request as file, then
                # add a redirection to a particular url
                return 301 https://www.chess.com/;
        }
        # add a custome error page
        error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /usr/share/nginx/html;
                internal;
        }
}"
# configure the default server block
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $serverblock
}
# restart nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
