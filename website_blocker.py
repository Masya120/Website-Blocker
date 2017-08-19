import time
from datetime import datetime as dt

# Use hosts_temp to test script on a copy of hosts in the same directory as script
hosts_temp = "hosts"

# Use hosts_path when you want to edit the actual hosts file on a Linux system
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"

# Update this list with websites that you want blocked during "working hours"
website_list = ["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()            
    time.sleep(60)

