# This puppet manifest enable the <holberton> user to login and open files without any error messages

file { '/etc/security/limits.conf':
  ensure  => present,
  content => "holberton soft nofile 4096\nholberton hard nofile 4096\n",
  mode    => '0644',
}

# restart the operating system
service { 'ssh':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/security/limits.conf'],
}
