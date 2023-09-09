import requests
import lxml.html
from lxml import etree

def get_titles (html_text):
    tree = lxml.html.document_fromstring (html_text)
