# Use puppet to make changes to an ssh client configuration file

file {'~/.ssh/config':
  ensure  => 'present',
  content  => @(END),
    Host isiaq
      HostName 100.25.205.228
      User ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  END
}
