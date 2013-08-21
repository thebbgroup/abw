# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "ubuntu-docker"
  config.vm.box_url = "http://cm3.beatbullying.org/cheeseshop/ubuntu-docker.box"
  config.vm.forward_port 49000, 8080

  # TODO replace this build step with 'docker pull' of a prebuilt
  # image (once we have a private image repo)
  pkg_cmd = "IMAGE=$(cd /vagrant && sudo docker build -q .); "
  # TODO has to be easier way to get image id (use -t?)
  pkg_cmd << "IMAGE=$(echo $IMAGE | rev | cut -f1 -d' ' | rev); "
  pkg_cmd << "sudo docker run -d -v /vagrant:/src -p 49000:5000 $IMAGE"
  config.vm.provision :shell, :inline => pkg_cmd
end
