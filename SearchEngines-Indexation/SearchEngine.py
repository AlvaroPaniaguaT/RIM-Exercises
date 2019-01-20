from bs4 import BeautifulSoup
import _thread, queue, time, requests
import sys


def do_request(log, url):
	name = url.split("https://")[1].split("/")[0]	# Extracting the name to use on the new file created

	f = open("%s" % name, "w")
	f.write(url + "\r\n\r\n")
	html_resp = requests.get(url)	#Gets the HTML page

	f.write(html_resp.text) #Writes content on file
	soup_obj = BeautifulSoup(html_resp.text) # Pass HTML text to parse
	for a in soup_obj.find_all('a', href=True):
		new_link = None
		if 'https:' in a['href']: 	# Get only links with https:
			new_link = a['href']

		if (not new_link in q.queue) & (not new_link is None):
				q.put(a['href'])	# Put each new link in the queue if doesn't exists
	f.close()


def main_thread():
	url = q.get()
	_thread.start_new_thread(do_request,
								(time.ctime(time.time()), url))
	time.sleep(0.5)
	main_thread()

if __name__ == '__main__':
	start_url = sys.argv[1]
	q = queue.Queue(100)
	q.put(start_url)
	main_thread()