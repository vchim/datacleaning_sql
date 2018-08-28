#-*-coding:utf-8-*-
'''
    to find duplicated questions
'''
import pandas as pd

def find_question(aset,dataframe):
    for know in aset:
        # 提取指定知识点的dataframe
        df = dataframe[dataframe['how_details_id']== know]
        index = df.index
        # 寻找重复的题目，return True or False
        df_1 = df.duplicated(['question', 'option_content'], keep=False)
        list = df_1.tolist()
        for j in range(len(list)):
            if list[j]:
                series = df.loc[index[j], ['how_details_id','question','question_id']]
                print series

if __name__ == '__main__':
    # read files
    kmt_question = pd.read_csv('kmt_question.csv',encoding='utf-8')
    kmt_question_know = pd.read_csv('kmt_question_know.csv',encoding='utf-8')
    zyb_know_how = pd.read_csv('zyb_know_how.csv',encoding='utf-8')
    zyb_know_how_details = pd.read_csv('zyb_know_how_details.csv',encoding='utf-8')
    zyb_know_how_details_sort = pd.read_csv('zyb_know_how_details_sort.csv',encoding='utf-8')
    zyb_special_topic = pd.read_csv('zyb_special_topic.csv',encoding='utf-8')
    zyb_special_topic_details = pd.read_csv('zyb_special_topic_details.csv',encoding='utf-8')

    # find English questions
    kmt_question_en = kmt_question[kmt_question['course_name']== u'英语']
    kmt_question_know_en = kmt_question_know[kmt_question_know['course_name']== u'英语']
    zyb_know_how_en = zyb_know_how[zyb_know_how['course_name']== u'英语']
    zyb_know_how_details_sort_en = zyb_know_how_details_sort[zyb_know_how_details_sort['course_name']== u'英语']

    # kmt_question_en.to_csv('kmt_question_en.csv', encoding='utf-8', index=False)
    # kmt_question_know_en.to_csv('kmt_question_know_en.csv', encoding='utf-8', index=False)
    # zyb_know_how_en.to_csv('zyb_know_how_en.csv',encoding='utf-8', index=False)
    # zyb_know_how_details_sort_en.to_csv('zyb_know_how_details_sort_en.csv',encoding='utf-8', index=False)

    # 按年级和学期排好序
    zyb_know_how_details_sortgrade_en = zyb_know_how_details_sort_en.sort_values(['grade_num','semester'])
    # zyb_know_how_details_sortgrade_en.to_csv('zyb_know_how_details_sortgrade_en.csv',encoding='utf-8', index=False )

    result_1 = pd.merge(zyb_know_how_details_sortgrade_en, kmt_question_know_en[['question_id','how_details_id']], how='left', on='how_details_id')
    result_2 = pd.merge(result_1, kmt_question_en[['question_id','question','option_content']], how='left', on='question_id')
    result_2.drop(['id','type','course_name','grade','lib_id','create_time','how_id','num'], axis=1, inplace=True)
    # 去除重复的记录
    result_3 = result_2.drop_duplicates()
    # 提取不同年级的数据
    three = result_3[result_3['grade_num']==3]
    four = result_3[result_3['grade_num']==4]
    five = result_3[result_3['grade_num']==5]
    six = result_3[result_3['grade_num']==6]
    # 提取不同学期的数据
    three_1 = three[three['semester'] == 1.0]
    four_1 = four[four['semester'] == 1.0]
    five_1 = five[five['semester'] == 1.0]
    six_1 = six[six['semester'] == 1.0]
    three_2 = three[three['semester'] == 2.0]
    four_2 = four[four['semester'] == 2.0]
    five_2 = five[five['semester'] == 2.0]
    six_2= six[six['semester'] == 2.0]
    # three_1.to_csv('three_1.csv',encoding='utf-8', index=False )
    # three_2.to_csv('three_2.csv',encoding='utf-8', index=False )
    # four_1.to_csv('four_1.csv',encoding='utf-8', index=False )
    # four_2.to_csv('four_2.csv',encoding='utf-8', index=False )
    # five_1.to_csv('five_1.csv',encoding='utf-8', index=False )
    # five_2.to_csv('five_2.csv',encoding='utf-8', index=False )
    # six_1.to_csv('six_1.csv',encoding='utf-8', index=False )
    # six_2.to_csv('six_2.csv',encoding='utf-8', index=False )
    three_11 = pd.read_csv('three_1.csv',encoding='utf-8')
    three_22 = pd.read_csv('three_2.csv',encoding='utf-8')
    four_11 = pd.read_csv('four_1.csv',encoding='utf-8')
    four_22 = pd.read_csv('four_2.csv',encoding='utf-8')
    five_11 = pd.read_csv('five_1.csv',encoding='utf-8')
    five_22 = pd.read_csv('five_2.csv',encoding='utf-8')
    six_11 = pd.read_csv('six_1.csv',encoding='utf-8')
    six_22= pd.read_csv('six_2.csv',encoding='utf-8')

    did_31 = three_11['how_details_id'].tolist()
    did_31 = set(did_31)
    did_32 = three_22['how_details_id'].tolist()
    did_32 = set(did_32)
    did_41 = four_11['how_details_id'].tolist()
    did_41 = set(did_41)
    did_42 = four_22['how_details_id'].tolist()
    did_42 = set(did_42)
    did_51 = five_11['how_details_id'].tolist()
    did_51 = set(did_51)
    did_52 = five_22['how_details_id'].tolist()
    did_52 = set(did_52)
    did_61 = six_11['how_details_id'].tolist()
    did_61 = set(did_61)
    did_62 = six_22['how_details_id'].tolist()
    did_62 = set(did_62)

    find_question(did_62,six_22)


