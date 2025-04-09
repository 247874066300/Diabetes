import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
list=[]#1|af
CountryName=[]#国家称呼
Country_Url=[]#https://diabetesatlas.org/data/en/country/1/af.html
ListYearPerson={'2011':[],'2021':[],'2030':[],'2045':[]}#（2011-2045）该国家患病人数
ListYearPersonPrevalence={'2011':[],'2021':[],'2030':[],'2045':[]}#（2011-2045）该国家年龄调整比较患病率
IGT={'2011':[],'2021':[],'2030':[],'2045':[]}#（2011-2045）IGT患病人数
IGTPrevalence={'2011':[],'2021':[],'2030':[],'2045':[]}#（2011-2045）该国家IGT年龄调整比较患病率
IFG={'2011':[],'2021':[],'2030':[],'2045':[]}#（2011-2045）IFG患病人数
IFGPrevalence={'2011':[],'2021':[],'2030':[],'2045':[]}#（2011-2045）该国家IFG年龄调整比较患病率

#（2011-2045）该国家对糖尿病相关卫生支出（百万美元）
ListYearMoney_2021=[]#List2021Money=[]# 该国家在2021年对糖尿病相关卫生支出（百万美元）
ListYearMoney_2030=[]
ListYearMoney_2045=[]
#（2011-2045）该国家对糖尿病相关卫生的人均支出（百万美元）
ListYearMoneyPersonAverage_2021=[]#List2021MoneyPersonAverage=[]#该国家在2021年对糖尿病相关卫生的人均支出（百万美元）
ListYearMoneyPersonAverage_2030=[]
ListYearMoneyPersonAverage_2045=[]

OverWeightObesity = {'Country': [], 'OverWeight': [], 'Obesity': []}#超重和肥胖的数据

LifeIndex={'Country':[],
           'QualityOfLifeIndex':[],#生活质量指数
           'PurchasingPowerIndex':[],#购买力指数
           'SafetyIndex':[],#安全指数
           'HealthCareIndex':[],#医疗保健指数
           'CostOfLivingIndex':[],#生活成本指数
           'PollutionIndex':[]}#污染指数

def AllCountry():
    Country_url =  'https://diabetesatlas.org/data/en/'
    Country_html = requests.get(Country_url)
    Country_html.encoding = 'utf-8'
    Country_Soup = BeautifulSoup(Country_html.text,'lxml')
    tit = Country_Soup.find('select',attrs={'id':'idf-country-list'}).findAll('option')
    for i in tit[1:]:
        a=(i["value"])
        list.append(a)
        Country_Url.append('https://diabetesatlas.org/data/en/country/'+a.replace('|','/')+'.html')

def Clean(text):
    if text=='-':
        return 0
    else:
        return eval(text.replace(',',''))

def AllCountryNews01():
#获取患病人数等数据
    print(Country_Url)
    sum=0
    for url in Country_Url:
        sum=sum+1
        print(sum)
        html = requests.get(url)
        html.encoding = 'utf-8'
        Soup = BeautifulSoup(html.text,'lxml')
        tit1 = Soup.find('h1')
        CountryName.append(tit1.text)
        tit = Soup.find('table',attrs={'id':'idf-country-data'}).findAll('td')
        #数据清理
        # (一)（2011-2045）该国家患病人数
        #818.3 1606.7  2172.8  3530.7
        ListYearPerson['2011'].append(Clean(tit[1].text))
        ListYearPerson['2021'].append(Clean(tit[2].text))
        ListYearPerson['2030'].append(Clean(tit[3].text))
        ListYearPerson['2045'].append(Clean(tit[4].text))
        # (二)（2011-2045）该国家年龄调整比较患病率
        ListYearPersonPrevalence['2011'].append(Clean(tit[6].text))
        ListYearPersonPrevalence['2021'].append(Clean(tit[7].text))
        ListYearPersonPrevalence['2030'].append(Clean(tit[8].text))
        ListYearPersonPrevalence['2045'].append(Clean(tit[9].text))
        # (三)（2011-2045）IGT患病人数
        IGT['2011'].append(Clean(tit[21].text))
        IGT['2021'].append(Clean(tit[22].text))
        IGT['2030'].append(Clean(tit[23].text))
        IGT['2045'].append(Clean(tit[24].text))
        # (四)（2011-2045）该国家IGT年龄调整比较患病率
        IGTPrevalence['2011'].append(Clean(tit[26].text))
        IGTPrevalence['2021'].append(Clean(tit[27].text))
        IGTPrevalence['2030'].append(Clean(tit[28].text))
        IGTPrevalence['2045'].append(Clean(tit[29].text))
        # (五)（2011-2045）IFG患病人数
        IFG['2011'].append(Clean(tit[31].text))
        IFG['2021'].append(Clean(tit[32].text))
        IFG['2030'].append(Clean(tit[33].text))
        IFG['2045'].append(Clean(tit[34].text))
        # (六)（2011-2045）该国家IFG年龄调整比较患病率
        IFGPrevalence['2011'].append(Clean(tit[36].text))
        IFGPrevalence['2021'].append(Clean(tit[37].text))
        IFGPrevalence['2030'].append(Clean(tit[38].text))
        IFGPrevalence['2045'].append(Clean(tit[39].text))
        print(ListYearPerson,ListYearPersonPrevalence,IGT,IGTPrevalence,IFG,IFGPrevalence)
        list2=[]
        list3=[]
        for i in tit[92:95]:
            list2.append(Clean(i.text))
        for i in tit[102:105]:
            list3.append(Clean(i.text))
        #（2011-2045）该国家对糖尿病相关卫生支出（百万美元）
        ListYearMoney_2021.append(list2[0])
        ListYearMoney_2030.append(list2[1])
        ListYearMoney_2045.append(list2[2])
       #（2011-2045）该国家对糖尿病相关卫生的人均支出（百万美元）
        ListYearMoneyPersonAverage_2021.append(list3[0])
        ListYearMoneyPersonAverage_2030.append(list3[1])
        ListYearMoneyPersonAverage_2045.append(list3[2])

def Clean02(list):
    for i in range(247):
        if list[i] == '-':
            list[i] = 0
    return list
def Clean03(Country, OverWeight, Obesity, countryEnd, country):
    for i in range(len(countryEnd)):
        if country[i] not in OverWeightObesity['Country']:
            OverWeightObesity['OverWeight'][OverWeightObesity['Country'].index(countryEnd[i])] = float(
                OverWeight[Country.index(country[i])])
            OverWeightObesity['Obesity'][OverWeightObesity['Country'].index(countryEnd[i])] = float(
                Obesity[Country.index(country[i])])
def AllCountryNews02():
    # 获取国家对医疗的投入和一系列习惯等问题
    Country = []
    OverWeight = []
    Obesity = []
    data = pd.read_csv('dataAfterClean.csv')
    print(data["Country"])
    Country_url = 'https://data.worldobesity.org/tables/prevalence-of-adult-overweight-obesity-2/'
    Country_html = requests.get(Country_url)
    Country_html.encoding = 'utf-8'
    Country_Soup = BeautifulSoup(Country_html.text, 'lxml')
    tit = Country_Soup.find('table', attrs={'id': 'results', 'class': 'results'}).findAll('td')
    for i in range(247):
        Country.append(tit[0 + i * 10].text)
        OverWeight.append(tit[8 + i * 10].text)
        Obesity.append(tit[9 + i * 10].text)
    Clean02(Country)
    Clean02(OverWeight)
    Clean02(Obesity)
    print(type(Obesity[0]))
    for i in data["Country"]:
        if i in Country:
            if i not in OverWeightObesity['Country']:
                OverWeightObesity['Country'].append(i)
                OverWeightObesity['OverWeight'].append(float(OverWeight[Country.index(i)]))
                OverWeightObesity['Obesity'].append(float(Obesity[Country.index(i)]))
        else:
            print(i)
            OverWeightObesity['Country'].append(i)
            OverWeightObesity['OverWeight'].append(0)
            OverWeightObesity['Obesity'].append(0)
    countryEnd = ['Bosnia and Herz.', 'Central African Rep.', 'Channel Islands', 'Curaçao', 'Czech Rep',
                  'Dem. Rep. Congo',
                  'Dominican Rep', 'Faroe Islands', 'Guinea-Bissau', 'Lao PDR',
                  'Netherlands Antilles', 'Korea', 'Russia',
                  'South Sudan', 'State of Palestine', 'S. Sudan', 'United Republic of Tanzania']
    country = ['Bosnia and Herzegovina', 'Central African Republic', 'Chad', 'Croatia', 'Czechia',
               'Democratic Republic of Congo',
               'Dominican Republic', 'Finland', 'Guinea', 'Laos',
               'Netherlands', 'South Korea', 'Russian Federation',
               'Sudan', 'Palestine', 'Sweden', 'Tanzania']
    Clean03(Country, OverWeight, Obesity, countryEnd, country)

def Clean04(text):
    if text=='?'or text=='\n?':
        return 0
    else:
        return float(text)
def EveryCountryNews03(countryUrl):
    if countryUrl=='0' or countryUrl=='https://www.numbeo.com/quality-of-life/country_result.jsp?country=Eswatini':
        LifeIndex['QualityOfLifeIndex'].append(0)
        LifeIndex['PurchasingPowerIndex'].append(0)
        LifeIndex['SafetyIndex'].append(0)
        LifeIndex['HealthCareIndex'].append(0)
        LifeIndex['CostOfLivingIndex'].append(0)
        LifeIndex['PollutionIndex'].append(0)
    else:
        Country_html = requests.get(countryUrl)
        Country_html.encoding = 'utf-8'
        Country_Soup = BeautifulSoup(Country_html.text, 'lxml')
        tit = Country_Soup.findAll('td', attrs={'style': 'text-align: right'})
        LifeIndex['QualityOfLifeIndex'].append(Clean04(tit[0].text))
        LifeIndex['PurchasingPowerIndex'].append(Clean04(tit[1].text))
        LifeIndex['SafetyIndex'].append(Clean04(tit[2].text))
        LifeIndex['HealthCareIndex'].append(Clean04(tit[3].text))
        LifeIndex['CostOfLivingIndex'].append(Clean04(tit[5].text))
        LifeIndex['PollutionIndex'].append(Clean04(tit[8].text))
def AllCountryNews03():
#获取生活质量指数，购买力指数，安全指数，医疗保健指数，生活成本指数
    Country=[]
    CountryUrl={}
    data = pd.read_csv('dataAfterClean.csv')
    Country_url = 'https://www.numbeo.com/quality-of-life/'
    Country_html = requests.get(Country_url)
    Country_html.encoding = 'utf-8'
    Country_Soup = BeautifulSoup(Country_html.text, 'lxml')
    tit = Country_Soup.find('select', attrs={'id': 'country'}).findAll('option')
    for i in tit[1:]:
        Country.append(i.text)
        CountryUrl[i.text]='https://www.numbeo.com/quality-of-life/country_result.jsp?country='+i.text
    countryEnd=['Antigua and Barbuda', 'Bosnia and Herz.', 'Brunei Darussalam', 'Cabo Verde', 'Central African Rep.',
                'Curaçao', 'Czech Rep',  'Dem. Rep. Korea', 'Dem. Rep. Congo',
                'Dominican Rep', 'Isle of Man', 'Lao PDR',  'Micronesia (Federated States of)',
                'Netherlands Antilles', 'Réunion', 'Korea', 'Saint Kitts and Nevis',
                'Saint Vincent and the Grenadines', 'Sao Tome and Principe', 'State of Palestine', 'S. Sudan',
                'Syrian Arab Republic', 'Tokelau', 'Trinidad and Tobago', 'US Virgin Islands', 'United Republic of Tanzania']

    country=['Antigua And Barbuda','Bosnia And Herzegovina','Brunei','Cape Verde','Central African Republic',
             'Curacao','Czech Republic','Dominica','Democratic Republic of the Congo',
             'Dominican Republic','Isle Of Man','Laos','Micronesia',
             'Netherlands','Reunion','Kosovo (Disputed Territory)','Saint Kitts And Nevis',
             'Saint Vincent And The Grenadines','Sao Tome And Principe','Palestine','Sudan',
             'Syria','Timor-Leste','Trinidad And Tobago','Us Virgin Islands','Tanzania']
    a=0
    for i in data["Country"]:
        a+=1
        print(a)
        LifeIndex['Country'].append(i)
        if i in Country:
            EveryCountryNews03(CountryUrl[i])
        else:
            if i in countryEnd:
                EveryCountryNews03(CountryUrl[country[countryEnd.index(i)]])
            else:
                EveryCountryNews03('0')

def CSV():
    data={
        'Country':CountryName,
        'ListYearPerson_2011':ListYearPerson['2011'],
        'ListYearPerson_2021':ListYearPerson['2021'],
        'ListYearPerson_2030':ListYearPerson['2030'],
        'ListYearPerson_2045':ListYearPerson['2045'],
        'ListYearPersonPrevalence_2011':ListYearPersonPrevalence['2011'],
        'ListYearPersonPrevalence_2021':ListYearPersonPrevalence['2021'],
        'ListYearPersonPrevalence_2030':ListYearPersonPrevalence['2030'],
        'ListYearPersonPrevalence_2045':ListYearPersonPrevalence['2045'],
        'IGT_2011':IGT['2011'],
        'IGT_2021':IGT['2021'],
        'IGT_2030':IGT['2030'],
        'IGT_2045':IGT['2045'],
        'IGTPrevalence_2011':IGTPrevalence['2011'],
        'IGTPrevalence_2021':IGTPrevalence['2021'],
        'IGTPrevalence_2030':IGTPrevalence['2030'],
        'IGTPrevalence_2045':IGTPrevalence['2045'],
        'IFG_2011':IFG['2011'],
        'IFG_2021':IFG['2021'],
        'IFG_2030':IFG['2030'],
        'IFG_2045':IFG['2045'],
        'IFGPrevalence_2011':IFGPrevalence['2011'],
        'IFGPrevalence_2021':IFGPrevalence['2021'],
        'IFGPrevalence_2030':IFGPrevalence['2030'],
        'IFGPrevalence_2045':IFGPrevalence['2045'],
        'Money20-79_2021':ListYearMoney_2021,
        'Money20-79_2030':ListYearMoney_2030,
        'Money20-79_2045':ListYearMoney_2045,
        'PersonMoney_2021': ListYearMoneyPersonAverage_2021,
        'PersonMoney_2030': ListYearMoneyPersonAverage_2030,
        'PersonMoney_2045': ListYearMoneyPersonAverage_2045
    }
    df=pd.DataFrame(data)
    df.to_csv("data01.csv",index=False)

def Clean05():
    data = pd.read_csv('data01.csv')
    #问题是，在数据展示中，这些国家名字在爬下来的数据data01和Map中不一样，要把爬下来的个别名字进行替换
    data.replace('Russian Federation', 'Russia', inplace=True)
    data.replace('United States of America', 'United States', inplace=True)
    data.replace('Dominican Republic', 'Dominican Rep', inplace=True)
    data.replace('Venezuela (Bolivarian Republic of)', 'Venezuela', inplace=True)
    data.replace('Bolivia (Plurinational State of)', 'Bolivia', inplace=True)
    data.replace('Democratic Republic of the Congo', 'Dem. Rep. Congo', inplace=True)
    data.replace('Central African Republic', 'Central African Rep.', inplace=True)
    data.replace('Sudan', 'S.Sudan', inplace=True)
    data.replace('Iran (Islamic Republic of)', 'Iran', inplace=True)
    data.replace('North Macedonia', 'Macedonia', inplace=True)
    data.replace('Republic of Moldova', 'Moldova', inplace=True)
    data.replace('Czechia', 'Czech Rep', inplace=True)
    data.replace('Bosnia and Herzegovina', 'Bosnia and Herz.', inplace=True)
    data.replace('Viet Nam', 'Vietnam', inplace=True)
    data.replace("Lao People's Democratic Republic", 'Lao PDR', inplace=True)
    data.replace("Democratic People's Republic of Korea", 'Dem. Rep. Korea', inplace=True)
    data.replace('Republic of Korea', 'Korea', inplace=True)
    data.replace('R茅union', 'Sudan', inplace=True)
    data.replace('S.Sudan', 'S. Sudan', inplace=True)
    #香港，澳门在爬虫获取的数据中单独列出来了，下面合并到China
    data.replace('China, Hong Kong SAR','China',inplace=True)
    data.replace('China, Macao SAR', 'China', inplace=True)
    #Country01中有重复的国家名字
    Country01=data['Country'].values.tolist()
    Country02=[]
    for i in Country01:
        if i not in Country02:
            Country02.append(i)
    data2=data.groupby(['Country']).sum()
    df = pd.DataFrame(data2)
    df.insert(0,'Country',Country02)
    #df已经把重复的数据合并了
    df.to_csv("dataAfterClean.csv", index=False)

def CSV01():
    Data = pd.read_csv('dataAfterClean.csv')
    Data['OverWeight']=OverWeightObesity['OverWeight']
    Data['Obesity']=OverWeightObesity['Obesity']
    Data['QualityOfLifeIndex'] = LifeIndex['QualityOfLifeIndex']
    Data['PurchasingPowerIndex'] = LifeIndex['PurchasingPowerIndex']
    Data['SafetyIndex'] = LifeIndex['SafetyIndex']
    Data['HealthCareIndex'] = LifeIndex['HealthCareIndex']
    Data['CostOfLivingIndex'] = LifeIndex['CostOfLivingIndex']
    Data['PollutionIndex'] = LifeIndex['PollutionIndex']
    Data.to_csv("dataAfterClean.csv", index=False)

#AllCountry()
#AllCountryNews01()
#CSV()
#Clean05()
#AllCountryNews02()
#AllCountryNews03()
#CSV01()

