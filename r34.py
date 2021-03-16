import rule34
import random
import os
from urllib import request

thingies = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM1234567890"
def extension():
	string = ""
	for x in range(16):
		string += random.choice(thingies)
	return string


rule34 = rule34.Sync()

#tags je array tagov what the fuck did you think it was
def save_img(tags):
	#sestav string k ga rab u searchu
	string = "+".join(tags)

	results = rule34.getImages(tags=string, singlePage=True, fuzzy=False)
	if len(results) == 0:
		#če nč ne najde, proba še fuzzy search k je manj accurate but oh well
		results = rule34.getImages(tags=string, singlePage=True, fuzzy=True)
		#če še zmer nć ne najde returna False
		if len(results) == 0:
			return False
	post = random.choice(results)
	with request.urlopen(post.file_url) as urlfile:
		filename = os.environ["userprofile"]+"\\hentcli/images/" + post.file_url.split("/")[-1] if post.file_url.split("/")[-1] not in os.listdir() else extension+post.file_url.split("/")[-1]
		f = open(filename, "wb")
		f.write(urlfile.read())
		f.close()
	return filename
