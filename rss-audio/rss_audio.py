import urllib.request
import feedparser

# rss feed; currently configured to overmorrow's library
pod_rss = 'http://feeds.simplecast.com/YzTE_hE3';

# parse rss
feed = feedparser.parse( pod_rss )
# run `print(feed)` if you're not sure what the output format will be
entries = feed[ "entries" ]

# loop through rss feed entries
for entry in entries:
	# use audio link
	url = entry["links"][1]["href"]
	# https -> http; remove query string
	new_url = url.replace("https","http").removesuffix("?aid=rss_feed&feed=YzTE_hE3")
	# set file name to episode title
	fname = entry["title"]+".mp3"

	# save audio to root directory as file name
	try:
		data = urllib.request.urlretrieve( new_url, fname )
		
	except:
		print('URL error: ', new_url)