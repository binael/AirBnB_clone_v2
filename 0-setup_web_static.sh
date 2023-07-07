#!/usr/bin/env bash
# A script that configures nginx and sets up web static as per specifications
apt-get -y update

if ! command -v nginx &> /dev/null; then
	apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Testing nginx installation" | tee /data/web_static/releases/test/index.html > /dev/null

if [ -L /data/web_static/current/ ]; then
	rm -R /data/web_static/current/
fi
ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/

loc="location /hbnb_static {"
al="alias /data/web_static/current/;"

sed -i "s/server_name localhost;/server_name _;/" /etc/nginx/sites-available/default
sed -i "s@root /var/www/html;@root /data/web_static/current;@" /etc/nginx/sites-available/default
sed -i "/server_name _;/a \\\n\t$loc\n\t\t$al\n\t}" /etc/nginx/sites-available/default

service nginx start
