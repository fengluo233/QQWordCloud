import jieba
import codecs
import sys
import pandas
import numpy as np
from wordcloud import WordCloud
import imageio
from wordcloud import WordCloud, ImageColorGenerator
from os import listdir
from os.path import isfile, join
import os

stopwords_filename = 'data/stopwords.txt'
font_filename = 'fonts/STFangSong.ttf'
template_dir = 'data/templates/'


def main(input_filename):
    content = '\n'.join([line.strip()
                         for line in codecs.open(input_filename, 'r', 'utf-8')
                         if len(line.strip()) > 0])
    stopwords = set([line.strip()
                     for line in codecs.open(stopwords_filename, 'r', 'utf-8')])

    segs = jieba.cut(content)
    words = []
    for seg in segs:
        word = seg.strip().lower()
        if len(word) > 1 and word not in stopwords:
            words.append(word)

    words_df = pandas.DataFrame({'word': words})
    words_stat = words_df.groupby(by=['word'])['word'].agg(np.size)
    words_stat = words_stat.to_frame()
    words_stat.columns = ['number']
    words_stat = words_stat.reset_index().sort_values(by="number", ascending=False)

   

    input_prefix = input_filename
    if input_filename.find('.') != -1:
        input_prefix = '.'.join(input_filename.split('.')[:-1])

    for file in listdir(template_dir):
        if file[-4:] != '.png' and file[-4:] != '.jpg':
            continue
        background_picture_filename = join(template_dir, file)
        if isfile(background_picture_filename):
            prefix = file.split('.')[0]

            bimg = imageio.imread(background_picture_filename)
            wordcloud = WordCloud(font_path=font_filename, background_color='white',
                                  mask=bimg, max_font_size=600, random_state=100)
            wordcloud = wordcloud.fit_words(
                dict(words_stat.head(100).itertuples(index=False)))

            bimgColors = ImageColorGenerator(bimg)
            wordcloud.recolor(color_func=bimgColors)

            
            wordcloud.to_file(output_filename)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('[usage] <input>')
