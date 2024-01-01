# write a configuration file with puppet for ssh-client authentication


# Write the ssh-client configuration in to the ssh_config file
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  content => "\
Host isiaq
    HostName 100.25.205.228
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
