# increase the file descriptor limit on nginx web server to prevent failed requests

file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT=\"-n 4096\"\n",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
