# QQ词云生成工具
借鉴了网上的一些结果做出来的东西，有很多小bug等待修复
## 文件结构
* data
    * templates

        存储生成的词云的轮廓形状图片

    * stopwords.txt

        存储忽略掉的关键词，可自己添加
* fonts
    
     存放字体文件
* preprocess.py

    用于去除昵称时间等不需要统计的东西

* create_word_cloud.py
    
    创建词云的python程序

## 使用方法
运行
```python
python preprocess.py filename.py
```
来删除昵称等不需要统计的文字，生成__filename.py

运行
```
python create_word_cloud.py __filename.py
```
然后就在 `out` 文件夹里边生成词云了。
## 注意
目前来说，聊天记录的名字最好是英文的，对中文的支持有一些问题