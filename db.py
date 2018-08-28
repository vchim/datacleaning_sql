#-*-coding:utf-8-*-

import pandas as pd
from sqlalchemy import create_engine

db_info = {'user': 'root',
           'password': 'chelsea1228',
           'host': 'localhost',
           'database': 'mysql'  # 这里我们事先指定了数据库，后续操作只需要表即可
           }

# 这里直接使用pymysql连接,echo=True，会显示在加载数据库所执行的SQL语句。
engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s/%(database)s?charset=utf8' % db_info,
                       encoding='utf-8')

a = pd.read_sql_table(table_name ='zyb_know_how', con = engine)
b = pd.read_sql_table(table_name ='kmt_question', con = engine)
c = pd.read_sql_table(table_name ='kmt_question_know', con = engine)
d = pd.read_sql_table(table_name ='zyb_know_how_details', con = engine)
e = pd.read_sql_table(table_name ='zyb_know_how_details_kd', con = engine)
f = pd.read_sql_table(table_name ='zyb_know_how_details_sort', con = engine)
g = pd.read_sql_table(table_name ='zyb_know_how_special_topic', con = engine)
h = pd.read_sql_table(table_name ='zyb_special_topic', con = engine)
i = pd.read_sql_table(table_name ='zyb_special_topic_details', con = engine)

# 保存成csv格式
# a.to_csv('zyb_know_how.csv', encoding='utf-8', index=False)
# b.to_csv('kmt_question.csv', encoding='utf-8', index=False)
# c.to_csv('kmt_question_know.csv', encoding='utf-8', index=False)
# d.to_csv('zyb_know_how_details.csv', encoding='utf-8', index=False)
# e.to_csv('zyb_know_how_details_kd.csv', encoding='utf-8', index=False)
# f.to_csv('zyb_know_how_details_sort.csv', encoding='utf-8', index=False)
# g.to_csv('zyb_know_how_special_topic.csv', encoding='utf-8', index=False)
# h.to_csv('zyb_special_topic.csv', encoding='utf-8', index=False)
# i.to_csv('zyb_special_topic_details.csv', encoding='utf-8', index=False)
