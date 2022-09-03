import optparse
import requests
import json
from urllib.parse import urlparse
from colorama import Fore
import pyfiglet
import time

optparse = optparse.OptionParser()
optparse.add_option("-u",dest="domain",help="Enter URL")
optparse.add_option("--post",help="POST Request")
optparse.add_option("--get",help="GET Request")
optparse.add_option("-p",dest="params",help="Enter Parameter")
optparse.add_option("-f",dest="file",help="Scan file e.g urls.txt")
output, args = optparse.parse_args()

#print(output.post)
#print(output.get)
#print(output.parameter)

print(pyfiglet.figlet_format("SSTI SCANNER"))
time.sleep(1)
print("\t\t#Coded With L0VE: BePractical")
time.sleep(1)
print("\t\thttps://bepractical.tech/\n")


def param_replace(url,payload):
	parsed_url = urlparse(url)
	query = parsed_url.query
	#print(query)
	if len(query) == 0:
		#print(1)
		return query
	try:
		queries = query.split("&")
		for i in queries:
			param_val = i.split("=")[1]
			query = query.replace(f"={param_val}",f"={payload}")
	except:
		pass
	return query

def parse_url(url,payload):
	param_val = []
	parsed_url = urlparse(url)
	scheme = parsed_url.scheme
	netloc = parsed_url.netloc
	path = parsed_url.path
	query = param_replace(url,payload)
	#query = query.replace("=",payload)
	fragment = parsed_url.fragment
	if len(urlparse(url).query) == 0:
		return f"{scheme}://{netloc}{path}{query}{fragment}"
	return f"{scheme}://{netloc}{path}?{query}{fragment}"

#parse_url("https://test.com/?id=test&spiderman=no_test","{4*4}")

#param_replace("https://test.com/?id=batm&spiderman=no_test","{4*4}")

def open_data(filename):
	with open(filename,"r") as f:
		data = json.load(f)
		f.close()
	print(Fore.BLUE + f"[+]{len(data)} PAYLOAD LOADED")
	return data

def scan_get(url):
	data = open_data("payload.json")
	for i in data:
		payload = i['payload']
		out = i['output']
		f_url = parse_url(url,payload)
		#print(f_url)
		response = requests.get(f_url).text
		if type(out) == type(['a','b','c']):
			#print(payloads['output'])
			for i in out:
				#print(i)
				if i in response:
					print(Fore.RED + f"[+] VULNERABLE\nURL:{f_url}\n------------------")
					continue
		else:
			if out in response:
				#print(f_url + "  " + out)
				print(Fore.RED + f"[+] VULNERABLE\nURL:{f_url}\n----------------------")
def scan_post(url,params):
	data = open_data("payload.json")
	final_param = {}
	for payloads in data:
		if type(params) == type("batman"):
			final_param[params] = payloads[payload]
		for j in params:
			final_param[j] = payloads["payload"]
		response = requests.post(url,data=final_param).text
		if type(payloads['output']) == type([1,2,3]):
			#print(payloads['output'])
			for i in payloads['output']:
				#print(i)
				if i in response:
					print(Fore.RED + f"[+] VULNERABLE\nURL:{url}\nPAYLOAD:{payloads['payload']}\n------------------")
					continue
		else:
			if payloads['output'] in response:
				print(Fore.RED + f"[+] VULNERABLE\nURL:{url}\nPAYLOAD:{payloads['payload']}")
		final_param = {}

if output.post:
	try:
		param = output.params.split(",")
	except:
		param = output.params
	finally:
		scan_post(output.domain,param)
elif output.file:
	with open(output.file,"r") as url_data:
		urls = url_data.read().split()
		for url in urls:
			print(Fore.BLUE + f"[+] TESTING {url}")
			scan_get(url)
elif output.get:
	scan_get(output.domain)

#scan_post("http://10.10.11.170:8080/search",["name"])
#scan_get("http://172.24.101.190/?name=faiyaz&batman=2")
#print(parse_url("http://localhost/","#{4*4}"))
