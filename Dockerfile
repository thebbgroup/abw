# This file describes the standard way to build ABW, using docker

# To run this image in a container in a dev vagrant box do:
#     sudo docker run -d -v /vagrant:/src <image name> -p49000:5000

from	shykes/pybuilder
maintainer	Mark Allison <mark.allison@thebbgroup.org>

# Build dependencies
run	apt-get install -y -q libpq-dev
run	apt-get install -y -q python-dev

# Install python libraries
add     ./requirements.txt /opt/apps/abw/requirements.txt
run     pip install -q -r /opt/apps/abw/requirements.txt
 
# TODO expose 5000? Probably because we can use the same port numbers in dev and production

# Run the ABW Flask app when this image is run
# (Not supported by our version of docker: workdir /src)
cmd     cd /src && python run.py
