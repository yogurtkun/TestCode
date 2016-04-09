import re

#在应用关系中，判断引用是否合理

def compare_year(id1,id2):
    year1 = re.findall('[A-Z](\d{2})-',id1)[0]
    year2 = re.findall('[A-Z](\d{2})-',id2)[0]

    year1 = int(year1)
    year2 = int(year2)

    year1 = year1 - 100 if year1 > 50 else year1
    year2 = year2 - 100 if year2 > 50 else year2

    return year1 >= year2

def clean_list(x):
    while '' in x:
        x.remove('')
