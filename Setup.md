sudo easy_install pip
sudo pip install virtualenv
sudo pip install virtualenvwrapper --ignore-installed six
printf '# virtualenv\n' >> ~/.bash_profile
printf 'export WORKON_HOME=~/.virtualenvs\n' >> ~/.bash_profile
printf 'source /usr/local/bin/virtualenvwrapper.sh\n' >> ~/.bash_profile
source ~/.bash_profile
mkdir -p $WORKON_HOME
mkvirtualenv default
sudo easy_install pip
pip install --upgrade pip
ssh-keygen
