from lxml import etree, html

document_root = html.fromstring("<html><body><h1>hello world</h1></body></html>")
print(etree.tostring(document_root, encoding='unicode', pretty_print=True))