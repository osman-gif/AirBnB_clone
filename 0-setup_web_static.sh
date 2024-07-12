#!/usr/bin/env bash
apt-get update
apt-get install -y nginx
service nginx start

if [ ! -d "/data/web_static/releases/test/" ]; then
	mkdir -p "/data/web_static/releases/test/"
fi
if [ ! -d "/data/web_static/shared/" ]; then
	mkdir -p "/data/web_static/shared/"
fi

html="<p> Wow, it works <p>"

echo "$html" | tee -a /data/web_static/releases/test/index.html

current_link="/data/web_static/current"
target_folder="/data/web_static/releases/test"

if [ -L "$current_link" ]; then
    rm "$current_link"
fi

ln -s "$target_folder" "$current_link"

sudo chown -R ubuntu:ubuntu "/data"

server="
server {
	listen 80;
	listen [::]:80;
	server_name ajangosman.tech;
	index index.html;
	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files "$uri" "$uri/" =404;
	}
}"
echo "$server" | sudo tee -a /etc/nginx/sites-available/default
service nginx restart

