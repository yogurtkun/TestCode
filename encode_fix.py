import html

with open('./titleset.txt','r') as file:
    read_file = file.read()

new_file = html.unescape(read_file)

with open('./new_titleset.txt','w') as file:
    file.write(new_file)