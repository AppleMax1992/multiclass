# coding:utf-8
from numpy.lib.arraysetops import unique
from pandas.core.indexes.base import Index
import pymongo
import pandas as pd
import re
import collections
# 连接数据库
client = pymongo.MongoClient('localhost',27017) #创建链接客户端
db=client['kg_test'] #创建数据库连接
collection=db['result'] #连接集合
collection_pro=db['db_triples']
text_data=collection.find() #查找
triples_data=collection_pro.find() #查找
# print(text_data)
# 读取数据
# print(triples_data)
res = []
for item in triples_data:
   res.append( re.sub(r'[’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+','',item['attr']) )
unique_res =  set(res)
# print(unique_res)
# 提取key的集合
# for key, value in text_data.iteritems():
#     print(key, value)
key = []
value = []
def anyls(a):     
    dic = collections.Counter(a)
    for i in dic:
         key.append(i)
         value.append(dic[i])
        #  print(i,',',dic[i])
    # return  dic

anyls(res)
# print(dic)
# print(key)
# print(value)
csvpd =  pd.DataFrame({'name':key,'value':value})
csvres = csvpd.sort_values(by=['value'],axis = 0,ascending = False)

csvres.to_csv('res.csv',index=None,encoding='utf_8_sig')

props = csvres['name'][0:10]
# print(props)
prepare_list = {}
for i in props:
    prepare_list[i] = []
# print(prepare_list)
    # propsarr.append(i=[])
# print(propsarr)
name = []
text = []
cid = []
for index,item in enumerate(text_data):
    # if(index < 1):
    if (item['attr'] and len(item['attr'])>0):
        # print(item)
        cid.append(index)
        name.append(re.sub(r'[’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+','',item['_id']))
        # print(re.sub('\s+'," ",item['text']))
        text.append(re.sub('\s+'," ",item['text']))
        # text.append(item['text'])
        # print(len(item['attr'])>0)
        for prop in prepare_list :
            flag = 0
            for i in item['attr']:
                if(i['attr'] == prop):
                    flag = 1
            prepare_list[prop].append(flag)

                

# 中文名,6527
# 外文名,3810
# 别名,441
# 拼音,326
# 国籍,318
# 本名,229
# 作者,175
# 类型,120
# 书名,116
# 作品名称,82
# 性质,77
# for item in prepare_list:
#     print(len(prepare_list[item]))
# print(len(text))
# print(text)
print('开始导出')
csvpd =  pd.DataFrame({'id':cid,'name':name,'text':text,'中文名':prepare_list['中文名'],'外文名':prepare_list['外文名'],'别名':prepare_list['别名'],'拼音':prepare_list['拼音'],'国籍':prepare_list['国籍'],'本名':prepare_list['本名'],'作者':prepare_list['作者'],'类型':prepare_list['类型'],'书名':prepare_list['书名'],'作品名称':prepare_list['作品名称']})
csvpd.to_csv('./resFin.csv',index=None,encoding='utf_8_sig')
# res_list.append({'entity':item['name'],'text':its['text'],item['attr']:item['value']})
# res = pd.DataFrame.from_dict(res_list,orient='index', columns=['entity', 'text'])
print('完成导出')
# res.to_csv('res.csv',encoding='utf-8')
# l = [1,2,3,4,5]
# pd.DataFrame(l).to_csv('res.csv')

    # l=len(its['result']['data']['list']['results']) #获取['result']>['data']>['list']>['results']下的子项目数量
    # for i in range(0,l):
    #     print("No:",i)
    #     print(its['result']['data']['list']['results'][i]['title'])
    # break