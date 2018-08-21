from bs4 import  BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#Python 2 soup=BeautifulSoup(html)
soup=BeautifulSoup(html,"lxml")
#soup=BeautifulSoup(open('index.html'))
#print(soup.prettify())
#print(soup.title)
print(soup.a)
soup.name
soup.head.name
soup.p.attrs
soup.p.p['class']
soup.p['class']="newClass"
del soup.p['class']
#inner text
print(soup.p.string)

#View trees
soup.head.contents
soup.head.contents[0]
soup.head.children
for child in  soup.body.children:
    print(child)
for child in soup.descendants:
    print(child)
soup.p.parent.name
content = soup.head.title.string
for parent in  content.parents:
    print(parent.name)
soup.p.next_sibling
soup.p.prev_sibling
soup.head.next_element
soup.find_all('b')