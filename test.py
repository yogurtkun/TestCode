import re

sta = 'Natalie Kübler:L14-1085;@@@@@\n'

author_paper_string = '(.*?):(.*?)@@@@@(.*?)\n'
author_paper_pattern = re.compile(author_paper_string)

result = author_paper_pattern.findall(sta)

for item in result:
    print(item)
