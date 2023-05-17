# Increase files for holberton user
exec {'edit':
  provider  =>  shell,
  command   =>  'sudo sed -i 's\^holberton hard nofile 5\holberton hard nofile 4000\' /etc/security/limits.conf',
  command   =>  'sudo sed -i 's\^holberton soft nofile 4\holberton soft nofile 4000\' /etc/security/limits.conf',
}
