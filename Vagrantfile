# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.network :forwarded_port, guest: 5000, host: 8080

$script = <<SCRIPT

apt-get update
apt-get -yq install git curl python-pip python-dev libxml2-dev libxslt-dev libpq-dev postgresql gcc make binutils libjpeg-dev libpng-dev libxrender1 libfontconfig1

curl -sL https://deb.nodesource.com/setup | sudo bash -
sudo apt-get install nodejs

sudo /usr/bin/npm install -g less

pip install -U pip
cd /vagrant
/usr/local/bin/pip install -U -r requirements.txt

SCRIPT

  config.vm.provision "shell", inline: $script

end
