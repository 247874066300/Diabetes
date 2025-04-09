import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

'''
dataCountry,data['Country']  数据——国家
dataShuJu,data['2021_0_13']  数据——给的数据
title,"world"——地图名字
subtitle,"999"——副标题
range_text_2,#图例的文字
split_number,#如果是连续数据分成几段
pieces，[0,360000]
html01:地图存放路径
'''
def MapWord(dataCountry,dataShuJu,title,subtitle,range_text_2,pieces,html01):
    print(pieces[-1])
    c=(
        Map(init_opts=opts.InitOpts(width="1400px",height='600px',theme='vintage'))#图表大小
        .add(
            "",#系列名称
            [list(z) for z in zip(dataCountry,dataShuJu)],#使用数据
            "world",#地图格式world_世界地图，China_中国地图
            is_map_symbol_show=False,)#是否显示红色小圆点
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))#标签不显示（国家名称不显示）
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=title,#主标题
                pos_left='20%',#位置
                subtitle=subtitle#副标题
            ),  # 位置
            visualmap_opts=opts.VisualMapOpts(#图列设置
                type_='color',#映射方式：color或者size
                max_=pieces[-1],
                min_=pieces[0],
                range_text=['',range_text_2],#图例的文字
                orient='vertical',#图例的方式水平，水平horizontal  竖直vertical
                is_inverse=False,#是否反转

            ),
        )
    )
    c.render(html01)
data=pd.read_csv('dataAfterClean.csv')
pieces=[0,150000]
#MapWord(data['Country'],data['ListYearPerson_2021'],"2021年全球","2021年患病人口",'患病人口(in 1000s)',pieces,"002.html")
#MapWord(data['Country'],data['IGT_2011'],"2011年全球","2011年IGT患病人口",'患病人口(in 1000s)',pieces,"IGT.html")

import matplotlib.pyplot as plt
from matplotlib import rcParams
#该国家患病人数,IGT,IFG以及年龄调整比较患病率在（2011-2045）的变化
#type：类型：①''：年龄调整比较患病率②'IFG'：IFG③'IGT':IGT
#Country--国家名称：'China'
def Change(type,Country):
    data=pd.read_csv('dataAfterClean.csv')
    row_data=data[data['Country']==Country]
    print(row_data.iloc[0])
    datas=[]
    if type=='':
        datas=row_data.iloc[0].tolist()[1:9]
    elif type=='IGT':
        datas=row_data.iloc[0].tolist()[9:17]
    elif type=='IFG':
        datas= row_data.iloc[0].tolist()[17:25]
    else:
        print('error01')
    print(datas)
    rcParams['font.family']=rcParams['font.sans-serif']='SimHei'
    ax=plt.figure().add_subplot()
    labels=[2011,2021,2030,2045]
    cordx=range(len(labels))#x轴刻度的位置
    F1=ax.bar(x=cordx,height=datas[0:4],width=0.25,color='red')
    ax.legend(F1,'患病人数')
    ax.set_ylabel("患病人数（in 1000s）")
    ax.set_xticks(cordx)
    ax.set_xticklabels(labels)
    print(len(labels))
    ax.set_title(Country+"2011-2045"+type+"患病人数和年龄调整比较患病率")

    plt.twinx()
    plt.plot(cordx, datas[4:8], ls='--', lw=2, color='c', marker='v', ms=10, mfc='k', label=type+'年龄调整比较患病率')
    plt.legend(loc='upper right')
    plt.ylabel("单位（%）",  loc="center")
    plt.show()
#Change('','China')
#Change('IFG','Armenia')
#在2021-2045国家对糖尿病的资金投入
def MoneyChange(Country):
    data=pd.read_csv('dataAfterClean.csv')
    row_data=data[data['Country']==Country]
    datas= row_data.iloc[0].tolist()[25:31]
    print(datas)
    rcParams['font.family']=rcParams['font.sans-serif']='SimHei'
    ax=plt.figure().add_subplot()
    labels=[2021,2030,2045]
    cordx=range(len(labels))#x轴刻度的位置
    F1=ax.bar(x=cordx,height=datas[0:3],width=0.25,color='red')
    ax.legend(F1,'总投入',loc='upper left')
    ax.set_ylabel("单位（百万美元）")
    ax.set_xticks(cordx)
    ax.set_xticklabels(labels)
    print(len(labels))
    ax.set_title(Country+"在2021-2045年对糖尿病的资金投入")

    plt.twinx()
    plt.plot(cordx, datas[3:6], ls='--', lw=2, color='c', marker='v', ms=10, mfc='k', label='人均资金投入')
    plt.legend(loc='upper right')
    plt.ylabel("单位（美元）",  loc="center")
    plt.show()
#data=pd.read_csv('dataAfterClean.csv')
#pieces=[0,150000]
#(一)世界地图
#MapWord(data['Country'],data['ListYearPerson_2021'],"2021年全球","2021年患病人口",'患病人口(in 1000s)',pieces,"002.html")

#(二)折线统计图
#Change('','China')
##type：类型：①''：年龄调整比较患病率②'IFG'：IGT③'IGT':IGT
##Country--国家名称：'China'

#(三)折线统计图
#MoneyChange('China')


