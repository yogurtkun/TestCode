import re
import html

str = 'H&#246;ir, world'

utf_pattern = re.compile('&#(\d{3});')

result = html.unescape(str)

print(result)

