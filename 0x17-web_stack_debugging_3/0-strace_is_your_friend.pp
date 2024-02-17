# This manifest fixes an apache returning 500 internal server error

file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => 'file',
  source => '/var/www/html/wp-includes/class-wp-locale.php',
  notify => Service['apache2'],
}

service { 'apache2':
  ensure => 'running',
  enable => true,
}
