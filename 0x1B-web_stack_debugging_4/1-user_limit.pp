# Increase the system amount of files that can be opened by a user

exec {'hard':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['soft'],
}

exec {'soft':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
