# (https?)://(www)?(\.?\w+\.)(com|org)(.+)
import re

search = re.search(r'(https?)://(www)?(\.?\w+\.)(com|org)(.+)', \
r"http://www.elzero.org:8888/link.php \
https://elzero.org:8888/link.php \ 
http://www.elzero.com/link.py \
https://elzero.com/link.py \
http://www.elzero.net \
https://elzero.net")

print(search)
