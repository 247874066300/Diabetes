import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import  mean_squared_error
df=pd.read_csv('dataAfterClean.csv')

cols = [
        'ListYearPerson_2021','ListYearPersonPrevalence_2021',
        'IGT_2021','IGTPrevalence_2021','IFG_2021','IFGPrevalence_2021','Money20-79_2021','PersonMoney_2021','OverWeight',
        'Obesity','QualityOfLifeIndex','PurchasingPowerIndex','SafetyIndex','HealthCareIndex','CostOfLivingIndex','PollutionIndex']
cols1 = [
        #'ListYearPerson_2021',
        'ListYearPersonPrevalence_2021',
        'IGT_2021','IGTPrevalence_2021','IFG_2021', 'IFGPrevalence_2021','Money20-79_2021','PersonMoney_2021','OverWeight',
        'Obesity','QualityOfLifeIndex','PurchasingPowerIndex','SafetyIndex','HealthCareIndex','CostOfLivingIndex','PollutionIndex']
# 将相关系数矩阵以热力图的形式可视化
def ReLiShow(cols):
    cm = np.corrcoef(df[cols].values.T)
    hm= sns.heatmap(cm, cbar=True, square=True, fmt='.2f', annot=True, annot_kws={'size': 15}, yticklabels=cols,
                 xticklabels=cols)
    plt.suptitle(cols[0], color='red', fontsize=20)
    plt.show()
#  cbar=True 表示显示颜色条，square=True 表示将热力图的宽高设置为相等，annot_kws={'size':15} 表示热力图上的数值字体大小为15
#(一)ListYearPerson_2021与其的相关系数
print('(一)ListYearPerson_2021与其的相关系数')
ReLiShow(cols)
#(二)ListYearPersonPrevalence_2021与其的相关系数,
print('(二)ListYearPersonPrevalence_2021与其的相关系数')
ReLiShow(cols1)

ListYearPerson_2021_cols=['ListYearPerson_2021','IGT_2021','IFG_2021','Money20-79_2021']
ListYearPersonPrevalence_2021_cols=['ListYearPersonPrevalence_2021','OverWeight','Obesity',
                                    'SafetyIndex','HealthCareIndex','PollutionIndex']

def SanDianShow(type,X,Y,function):
        X1=[]
        if type==0:
                for i in X:
                        if i>10000:
                                X1.append(10000)
                        else:
                                X1.append(i)
        elif type==1:
                X1=X
        else:
                print("Error")
        plt.scatter(x=X1,  # 横坐标
            y=Y,  # 纵坐标
            c='red',  # 点的颜色
            )
#(三)ListYearPerson_2021与其相关系数高的参数的散点图
print('(三)ListYearPerson_2021与其相关系数高的参数的散点图')
for i in range(3):
    plt.subplot(221+i)
    plt.title(ListYearPerson_2021_cols[i+1],color='green',fontsize=10)
    SanDianShow(0,df[ListYearPerson_2021_cols[0]],df[ListYearPerson_2021_cols[i+1]],ListYearPerson_2021_cols[i+1])
plt.suptitle(ListYearPerson_2021_cols[0],color='red',fontsize=20)
plt.show()
#(四)ListYearPersonPrevalence_2021与其相关系数高的参数的散点图
print('(四)ListYearPersonPrevalence_2021与其相关系数高的参数的散点图')
for i in range(5):
    plt.subplot(321+i)
    plt.title(ListYearPersonPrevalence_2021_cols[i+1],color='green',fontsize=10)
    SanDianShow(1,df[ListYearPersonPrevalence_2021_cols[0]],df[ListYearPersonPrevalence_2021_cols[i+1]],ListYearPersonPrevalence_2021_cols[i+1])
plt.suptitle(ListYearPersonPrevalence_2021_cols[0],color='red',fontsize=20)
plt.show()

def SuiJiSenLin(List,List_YuCe):
        x=[]
        y=[]
        for i in range(len(df[List[0]])):
                a=[]
                for j in range(len(List)-1):
                        a.append(format(df[List[j+1]][i],"e"))
                x.append(a)
                y.append(format(df[List[0]][i],"e"))

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        forest = RandomForestRegressor(n_estimators=10000, random_state=0, n_jobs=-1)#分类
        forest.fit(x_train, y_train)

        y_test_pred=forest.predict(x_test)
        y_test01=[]
        for i in y_test:
            y_test01.append(float(i))
        print(y_test01)
        print(y_test_pred)
        mes=mean_squared_error(y_test01,y_test_pred)
        print(mes)
        importances = forest.feature_importances_
        plt.figure(figsize=(10, 6))
        plt.title(List[0]+"各个特征的重要程度", fontsize=18)
        plt.ylabel("import level", fontsize=15, rotation=90)
        plt.rcParams['font.sans-serif'] = ["SimHei"]
        plt.rcParams['axes.unicode_minus'] = False
        X=List[1:]
        Y=importances
        plt.bar(x=X,height=Y,width=0.25,color='steelblue')
        for a,b in zip(X,Y):   #柱子上的数字显示
           plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize=7)
        plt.show()
        b1=[]
        b2=[]
        for i in List_YuCe:
                b1.append(format(i,"e"))
        b2.append(b1)
        return float(forest.predict(b2)[0])
#(五)使用随机森林对ListYearPerson_2021的数据进行预测和得出其因素的重要性统计图
ListYearPerson_2021_YuCe=[1293.7,756.1,229.9]
#其中的三个数据分别为：'IGT_2021','IFG_2021','Money20-79_2021'
print('(五)使用随机森林对ListYearPerson_2021的数据进行预测和得出其因素的重要性统计图')
a1=SuiJiSenLin(ListYearPerson_2021_cols,ListYearPerson_2021_YuCe)
print("根据随机森林得出患病人数（1000s）:",a1)

#(六)使用随机森林对ListYearPersonPrevalence_2021的数据进行预测和得出其因素的重要性统计图
#其中的三个数据分别为：'OverWeight','Obesity','SafetyIndex','HealthCareIndex','PollutionIndex'
ListYearPersonPrevalence_2021_YuCe=[22,42,43,29,84]
print('(六)使用随机森林对ListYearPersonPrevalence_2021的数据进行预测和得出其因素的重要性统计图')
a2=SuiJiSenLin(ListYearPersonPrevalence_2021_cols,ListYearPersonPrevalence_2021_YuCe)
print("根据随机森林得出年龄调整比较患病率:",a2)


