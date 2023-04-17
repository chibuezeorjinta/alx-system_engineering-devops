#/usr/bin/env bash
#configure a remote server for when connection is weak
scp ubuntu@
sudo ./1-install_nginx_web_server
sudo ./0-custom_http_response_header
cp 2-ssh_config ~/.ssh/ssh_config
cp ~/ssh/authorized_keys ~/ssh/backup_prior
cat school.pub >> ~/ssh/authorized_keys
cat let_me_in >> ~/ssh/authorized_keys
