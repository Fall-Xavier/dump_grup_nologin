import re, requests, bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()
id = []

def menu():
	idt = input("masukan id grup : ")
	url = "https://mbasic.facebook.com/groups/"+idt
	member_grup(url)

def member_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				idz = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if idz+"<=>"+nama in id:pass
				else:id.append(idz+"<=>"+nama);print(idz+"<=>"+nama)
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				member_grup("https://m.facebook.com"+href)
	except Exception as e:
		print(e)

menu()