# a puppet script that kill a process running

exec {'condition':
  command  => '/bin/pkill killmenow',
  onlyif  => "/bin/ps aux | grep -q '[k]illmenow'",
}