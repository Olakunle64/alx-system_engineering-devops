# install the flask package with a specific version and provider

# install python package of version 3.8.10
package { 'python3':
  ensure  => '3.8.10',
}

# ensure pip3 is install
package { 'python3-pip':
  ensure  => present,
}
# ensure pip is installed before installing flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# ensure flask is installed before installing werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
