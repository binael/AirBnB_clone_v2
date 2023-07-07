#!/usr/bin/env bash
# A script that configures nginx and sets up web static as per specifications
sudo apt-get -y update

if ! sudo command -v nginx &> /dev/null; then
	sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Testing nginx installation" | sudo tee /data/web_static/releases/test/index.html > /dev/null

if [ -L /data/web_static/current/ ]; then
	sudo rm -R /data/web_static/current/
fi
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

loc="location /hbnb_static {"
al="alias /data/web_static/current/;"

sudo sed -i "s/server_name localhost;/server_name _;/" /etc/nginx/sites-available/default
sudo sed -i "s@root /var/www/html;@root /data/web_static/current;@" /etc/nginx/sites-available/default
sudo sed -i "/server_name _;/a \\\n\t$loc\n\t\t$al\n\t}" /etc/nginx/sites-available/default
sudo systemctl restart nginx
