# CHANGE THE AMOUNT OF OPEN FILES FROM NGINX DEFAULT FILE

exec {'nginx_restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}

exec {'ULIMIT_EDIT':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['nginx_restart'],
}
