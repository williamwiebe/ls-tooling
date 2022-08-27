import urllib.request
import feedparser

# rss feed; currently configured to overmorrow's library
pod_rss = 'http://feeds.simplecast.com/YzTE_hE3';

# parse rss; run `print(feed)` after if you're not sure what the output format will be
feed = feedparser.parse( pod_rss )
entries = feed[ "entries" ]

# loop through rss feed entries
for entry in entries:
	# for overmorrow's library, the key-value pair is 'image': {'href': `url`}
	url = entry["image"]["href"]
	# https -> http; remove query string
	new_url = url.replace("https","http").removesuffix("?aid=rss_feed")
	# set file name to episode title
	fname = entry["title"]+".png"

	# save image to root directory as file name
	try:
		data = urllib.request.urlretrieve( new_url, fname )
		
	except:
		print('URL error: ', new_url)