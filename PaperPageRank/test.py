import json
a = {}
a['1'] = ["C­H","Y­S"]
b = json.dumps(a,ensure_ascii=False)
print(b.encode('utf-8'))
c = json.loads(b,encoding='utf-8')
print(c)
print(c['1'][0])