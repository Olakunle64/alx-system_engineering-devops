# install the flask package with a specific version and provider

package { 'flask':
  ensure   => '2.1.0',
  provider  => 'pip3',
}
