import json
import pickle


# 打开文件
with open('./sites.dat', 'rb') as f:
    load = pickle.load(f)
# print(load)
info = json.loads(json.dumps(load))

for i in info['indexer']:
    # print(i)
    if i['domain'] == 'https://chdbits.co/':
        i['domain'] = 'https://ptchdbits.co/'
    if i['domain'] == 'https://www.hdarea.co/':
        i['domain'] = 'https://hdarea.club/'


print(info)

with open('data/sites.dat', 'wb') as f:
    pickle.dump(info, f, pickle.HIGHEST_PROTOCOL)
