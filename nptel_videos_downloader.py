# Author: Kunal Kumar
# Social: twitter.com/l1v1n9h311, instagram.com/prokunal

import os,sys,wget,threading,urllib.request
from math import ceil
import requests,json
from urllib.request import Request, urlopen
print("fetching links to download...")
try:
    prefix = "https://tools.nptel.ac.in/npteldata/downloads.php?id={}".format(sys.argv[1].split('/')[-1])
    r = requests.get(prefix)
    flinks = json.loads(r.text)
except:
    print("python3 ",__file__.split('/')[-1]," course_link --videos")
    print("python3 ",__file__.split('/')[1],"course_link --assignments")
    sys.exit(0)
def video_downloader(flinks):
    links = []
    for i in flinks['data']['course_downloads']:
        links.append(i['url'])
    links = set(links)
    links = list(links)
    links.sort()
    return links

def assignments_downloader(flinks):
    links = []
    print(flinks)
    for i in flinks['data']['assignments']:
        links.append(i['url'])
    links = set(links)
    links = list(links)
    links.sort()
    return links
try:
    if sys.argv[2] == '--videos':
        links = video_downloader(flinks)
    elif sys.argv[2] == '--assignments':
        links = assignments_downloader(flinks)
    else:
        print("python3 ",__file__.split('/')[-1]," course_link --videos/--assignments")
        sys.exit(0)
except:
    pass
tmp_link = links
_dir = os.listdir(".")

for i in range(1,10,1):
  for i in tmp_link:
    if os.path.basename(i) in _dir:
      links.remove(i)
if len(links) == 0:
  print("All Videos are Downloaded Already :)")
  exit(0)

def split(links,size):
    for i in range(0,len(links),size):
        yield links[i:i+size]
      
size = ceil(len(links)/4)
link = list(split(links,size))

size_count = 0
print("Calculating Total size of all files, it may take upto 1 minute...")

for i in links:
  try:
    size = urllib.request.urlopen(i)
    size_count = size.length + size_count
  except:
    print("this link may have been moved: ",i)
    links.remove(i)
print("Total size of all files in MB is %.2fMB and in GB %.2fGB."%(size_count/1024/1024,size_count/1024/1024/1024))
def bar_progress(current, total, width=80):
    progress_message =  "Downloading: %d%% [%d MB / %d MB] " % (current / total * 100, current/1024/1024, total/1024/1024)
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()

def downloader1():
    for i in link[0]:
      filename = wget.download(i,bar=bar_progress)
      print(filename+ " Downloaded")

def downloader2():
    for i in link[1]:
      filename = wget.download(i,bar=bar_progress)
      print(filename + " Downloaded")

def downloader3():
    for i in link[2]:
      filename = wget.download(i,bar=bar_progress)
      print(filename+ " Downloaded")

def downloader4():
    for i in link[3]:
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
