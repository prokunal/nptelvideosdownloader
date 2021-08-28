# Author: Kunal Kumar
# Social: twitter.com/pr0kunal, instagram.com/prokunal

import os,sys,wget,urllib.request,threading
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


prefix = "https://nptel.ac.in"
course_link = sys.argv[1]
req = Request(course_link)
html_page = urlopen(req)
soup = BeautifulSoup(html_page,"lxml")
temp_links = []

for link in soup.findAll('a'):
  temp_links.append(link.get('href'))

links = []
for i in temp_links:
  if i.endswith('.mp4') or i.endswith('.MP4') or i.endswith('.mP4') or i.endswith('.Mp4'):
    links.append(prefix+i)

tmp_link = links
_dir = os.listdir(".")

for i in range(1,10,1):
  for i in tmp_link:
    if os.path.basename(i) in _dir:
      links.remove(i)
if len(links) == 0:
  print("All Videos are Downloaded Already :)")
  exit(0)
l1 = round(len(links)/4)

link1 = links[0:l1]
link2 = links[l1:l1+l1]
link3 = links[l1+l1:l1+l1+l1]
link4 = links[l1+l1+l1:l1+l1+l1+l1]

size_count = 0
print("Calculating Total size of all files, it may take upto 1 minute...")

for i in links:
  size = urllib.request.urlopen(i)
  size_count = size.length + size_count

print("Total size of all files in MB is %.2f and in GB %.2f"%(size_count/1024/1024,size_count/1024/1024/1024))
def bar_progress(current, total, width=80):
  progress_message = "Downloading: %d%% [%.2f / %.2f] mb " % (current / total * 100/1024/1024, current/1024/1024, total/1024/1024)
  sys.stdout.write("\r" + progress_message)
  sys.stdout.flush()

def downloader1():
    for i in link1:
      filename = wget.download(i,bar=bar_progress)
      print(filename+ " Downloaded")

def downloader2():
    for i in link2:
      filename = wget.download(i,bar=bar_progress)
      print(filename + " Downloaded")

def downloader3():
    for i in link3:
      filename = wget.download(i,bar=bar_progress)
      print(filename+ " Downloaded")

def downloader4():
    for i in link4:
      filename = wget.download(i,bar=bar_progress)
      print(filename + " Downloaded")        
t1 = threading.Thread(target=downloader1, name='d1')
t2 = threading.Thread(target=downloader2,name='d2')
t3 = threading.Thread(target=downloader3, name='d3')
t4 = threading.Thread(target=downloader4,name='d4')
t1.start()
t2.start()
t3.start()
t4.start()





