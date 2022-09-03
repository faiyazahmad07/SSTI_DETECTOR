# SSTI_DETECTOR
This tool tries to automate the process of ssti finding for you. It first send request to the url that you have supplied and if the payload is executed in the response then it will confirm the vulnerability.


# INSTALLATION

1. Clone this file in linux
2. In terminal, type "sudo bash install.sh"
3. Installation will be completed

# USAGE

GET:
python3 ssti.py -u <url> --get 1

POST:
python3 ssti.py -p <url> --post 1 -p  param1,param2

SCAN LIST OF URLS:
python3 ssti.py -f <filename>.txt

# Custom Payloads

We can add custom payloads in this tool. Just open the "payload.json" file and add your paylaod like:
{
  "payload":"${7*7}",
  "output":"49"
}

# SCREENSHOT

![ssti](https://user-images.githubusercontent.com/63125338/188286083-cca8f634-5fbd-4022-b0e8-88183c376e99.png)

Visit https://bepractical.tech for more such tools/content/services  YouTube: https://youtube.com/c/BePracticalTech
