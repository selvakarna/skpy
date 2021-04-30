# import requests 
# from bs4 import BeautifulSoup 

# specify the URL of the archive here 
## https://drive.google.com/file/d/1ZSTADvi2bVNL2EUmY_DsgJh-PfWXEl9Q/view?usp=sharing>
# archive_url ="https://drive.google.com/file/d/1ZSTADvi2bVNL2EUmY_DsgJh-PfWXEl9Q/view?usp=sharing>"
# archive_url="https://drive.google.com/file/d/1ZSTADvi2bVNL2EUmY_DsgJh-PfWXEl9Q/"
  #################Code Link:

  ## https://likegeeks.com/downloading-files-using-python/ 
import requests

url =r"https://3.bp.blogspot.com/-SVZ-ciC7WeA/WTLepcXi__I/AAAAAAAAAAQ/RNMvQjAgqZsBrLkYW5h6psBrXcqqHHwiQCLcB/s1600/sk.jpg"
# url=r'https://youtu.be/4T5lMHI6ovI'
myfile = requests.get(url, allow_redirects=True)

open(r'D:\Work\Development\Automation\mailfilt\mailfilter\out\fg.png', 'wb').write(myfile.content)
