import re
websitesi = "www.alierbey.com"
result = re.findall("^www\.+[a-z]+\.com$",websitesi)

if (result):
    print("websitesidir")
else:
    print("websitesi değildir.")
