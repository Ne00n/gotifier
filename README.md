# gotifier

**Setup Example**<br>
```
cd /opt/
git clone https://github.com/Ne00n/gotifier.git
useradd gotifier -r -d /opt/gotifier -s /bin/bash
chown -R gotifier:gotifier /opt/gotifier/
cat <<EOF >>/usr/local/bin/gotifier
#!/bin/bash
if [[ $(id -u) -ne 0 ]] ; then echo "Please run as root" ; exit 1 ; fi
exec sudo -u gotifier python3 /opt/gotifier/cli.py "$@"
EOF
chmod +x /usr/local/bin/gotifier
```

**Example**<br>
```
gotifier add --date "06.07.2026 20:00" --message "Test" --priority 10 --repeat 2
```
