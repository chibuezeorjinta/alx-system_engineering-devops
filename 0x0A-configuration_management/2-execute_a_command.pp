# Kill a process
exec {'kill-process':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
