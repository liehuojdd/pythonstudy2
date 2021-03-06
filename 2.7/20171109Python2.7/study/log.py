import sys, logging
import mechanize

logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

browser = mechanize.Browser()
browser.set_debug_http(True)
browser.set_debug_responses(True)
browser.set_debug_redirects(True)
response = browser.open("http://python.org/")