#! /bin/sh
#! /bin/bash
sudo apt-get install tasksel
tasksel install openssh-server
systemtcl enable ssh
sudo systemtcl start ssh
mkdir -p $HOME/.ssh
chmod 0700 $HOME/.ssh
ssh-keygen
ssh -keygen -t rsa 4096
cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chmod -R go= ~/.ssh && cat >> ~/.ssh/authorized_keys"
ssh username@server_IP
sudo nano /etc/ssh/sshd_config
