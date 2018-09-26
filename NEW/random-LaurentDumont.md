## My little cheat sheet

Random things that I can use at a later date.

### Foreman

Switch to the US Locale when systemm was installed with something else.
1. Show current locale with ```locale -a```
2. If ```en_US.utf8``` is missing from that list - Step 3
3. Use the following command ```dpkg-reconfigure locales``` to add ```en_US.utf8``` as the default system locale.
4. Restart postgreslsql with ```systemctl restart postgresql```
5. Restart the Foreman Installer with ```foreman-installer```

Reset the admin password because sometimes passwords are hard.
1. sudo foreman-rake permissions:reset

### Galera and Mariadb
1. Create a real admin user with all permissions to mimic root access.
2. ```CREATE USER 'lanets'@'%' IDENTIFIED BY 'test'; ```
3. ```GRANT ALL PRIVILEGES ON *.* TO 'lanets'@'%' WITH GRANT OPTION;```


### Linux Hardware
Slow speed with Intel N-6300 and Debian 8/9 (and probably many others)
1. ```echo "options iwlwifi 11n_disable=1 swcrypto=1" | sudo tee -a /etc/modprobe.d/iwlwifi.conf```
2. ```sudo modprobe -rv iwldvm```
3. ```sudo modprobe -v iwldvm```

### Ansible
Wrong version being used under user ENV but not under sudo. That was midly frustrating to say the least. For some reason, running ```ansible --version``` always showed 2.3.1.0 despite the fact that 2.4.1.0 was the only one installed.

I think what ended up happening is that I previously installed Ansible either manually or through Python pip which for some reason confused Ansible.
1. I removed everything under ```/usr/lib/python2.7/dist-packages/ansible/``` and ```/home/laurent/.local/lib/python2.7/site-packages/```

### Lenovo
Find laptop serial number.
1. Elevated CMD/PS prompt.
2. ```wmic bios get serialnumber```

### iPerf
```./iperf.exe -c 64.119.215.114 -u -b 200m -i 2 -t 100```

### Tectonic / DNSMask

```sudo docker run -d --rm --cap-add=NET_ADMIN --net=host quay.io/coreos/dnsmasq \
  -d -q \
  --dhcp-range=10.9.100.10,10.9.100.50 \
  --enable-tftp --tftp-root=/var/lib/tftpboot \
  --dhcp-userclass=set:ipxe,iPXE \
  --dhcp-boot=tag:#ipxe,undionly.kpxe \
  --dhcp-host=c0:ff:ee:00:00:15,10.9.100.3 \
  --dhcp-host=c0:ff:ee:00:00:16,10.9.100.4 \
  --dhcp-host=c0:ff:ee:00:00:17,10.9.100.5 \
  --dhcp-option=3,10.9.100.1 \
  --dhcp-boot=tag:ipxe,http://matchbox.event.lanets.ca:8080/boot.ipxe \
  --address=/matchbox.example/192.168.1.2 \
  --log-queries \
  --log-dhcp```
