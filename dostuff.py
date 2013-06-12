import urllib2

req = urllib2.Request('http://www.daim.co.uk')
response = urllib2.urlopen(req)
the_page = response.read()
#print the_page

for line in the_page.splitlines():
    if ".jpg" in line:
        print line
