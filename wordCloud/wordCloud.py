# -*- utf-8 -*-
# import PyQt5
import matplotlib
print(matplotlib.get_backend())
# matplotlib.use('agg')
matplotlib.use('Qt5Agg')
print(matplotlib.get_backend())
from wordcloud import WordCloud,ImageColorGenerator
print(matplotlib.get_backend())
import matplotlib.pyplot as plt
print('matplotlib.pyplot',matplotlib.get_backend())

import os
import json
from tqdm import tqdm
from itertools import groupby

stop_words = os.getcwd() + '/data/stopwords.txt'
#定义wordcloud中文体文件的路径
font = os.getcwd() + '/msyh.ttf/msyh.ttf'
#{"artist": "","artist_other":"", "title": "", "labels": {"": "", ...},
# "summary": "...", "intro": "..."}
data = []
with open(os.getcwd()+'/data/hudongbaike_artist_urls_enOther.json','r+',encoding='utf-8') as fr:
    ls = fr.readlines()
    for l in tqdm(ls):
        data.append(json.loads(l.strip(),encoding='utf-8'))
print('data:',len(data))
words = []
for d in tqdm(data):
    ds = set()
    ds.update([d['artist'],d['artist_other'],d['title']])
    for l in d['labels']:
        ds.update([d['labels'][l]])
    words = words + list(ds)
print('words:',len(words),words[:5])
words_sort = sorted(words)
words_gb = dict()
for k, g in groupby(words_sort):
    words_gb[k] = len(list(g))
print('words_groupby:',len(words_gb),words_gb['画家'],type(words_gb))
wc = WordCloud(font_path=font,background_color='white',max_font_size=80)
wordcld = wc.fit_words(words_gb)

plt.imshow(wordcld)
plt.axis('off')
plt.show()

wordcld.to_file(os.getcwd()+'/result/wordcloud.jpg')
