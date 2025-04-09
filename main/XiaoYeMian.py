import tkinter as tk
import tkinter.messagebox
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
df=pd.read_csv('dataAfterClean.csv')
class page1:
    def __init__(self,master:tk.Tk):
        self.root=master
        self.root.geometry('600x300')
        self.root.title("小页面运行")

        self.page = tk.Frame(self.root)
        self.page.grid(row=0, column=0, rowspan=2)

        tk.Label(self.page, text="(一)随机森林_预测_患病人数(1000s):").grid(row=1, column=1)
        tk.Label(self.page, text="IGT患病人数（1000s）：").grid(row=2, column=1)
        self.IGT = tk.Entry(self.page, textvariable=tk.StringVar())
        self.IGT.grid(row=2, column=2, columnspan=6)
        tk.Label(self.page, text="IFG患病人数（1000s）：").grid(row=3, column=1)
        self.IFG = tk.Entry(self.page, textvariable=tk.StringVar())
        self.IFG.grid(row=3, column=2, columnspan=6)
        tk.Label(self.page, text="国家资金的投入（百万美元）：").grid(row=4, column=1)
        self.Money = tk.Entry(self.page, textvariable=tk.StringVar())
        self.Money.grid(row=4, column=2, columnspan=6)
        tk.Button(self.page, text="预测上传", command=self.ListYearPerson_2021YuCe).grid(row=5, column=1)

        tk.Label(self.page, text="(二)随机森林_预测_年龄调整比较患病率:").grid(row=6, column=1)
        tk.Label(self.page, text="成人超重患病率（%）").grid(row=7, column=1)
        self.OverWeight = tk.Entry(self.page, textvariable=tk.StringVar())
        self.OverWeight.grid(row=7, column=2, columnspan=6)
        tk.Label(self.page, text="成人肥胖患病率（%）").grid(row=8, column=1)
        self.Obesity = tk.Entry(self.page, textvariable=tk.StringVar())
        self.Obesity.grid(row=8, column=2, columnspan=6)
        tk.Label(self.page, text="安全指标").grid(row=9, column=1)
        self.SafetyIndex = tk.Entry(self.page, textvariable=tk.StringVar())
        self.SafetyIndex.grid(row=9, column=2, columnspan=6)
        tk.Label(self.page, text="医疗保健指标").grid(row=10, column=1)
        self.HealthCareIndex = tk.Entry(self.page, textvariable=tk.StringVar())
        self.HealthCareIndex.grid(row=10, column=2, columnspan=6)
        tk.Label(self.page, text="生活污染指数").grid(row=11, column=1)
        self.PollutionIndex = tk.Entry(self.page, textvariable=tk.StringVar())
        self.PollutionIndex.grid(row=11, column=2, columnspan=6)

        tk.Button(self.page, text="预测上传", command=self.ListYearPersonPrevalence_2021YuCe).grid(row=12,column=1)

        self.ListYearPerson_2021_cols = ['ListYearPerson_2021', 'IGT_2021', 'IFG_2021', 'Money20-79_2021']
        self.ListYearPersonPrevalence_2021_cols = ['ListYearPersonPrevalence_2021', 'OverWeight', 'Obesity',
                                              'SafetyIndex', 'HealthCareIndex', 'PollutionIndex']
    def SuiJiSenLin(self,List,List_YuCe):
            x = []
            y = []
            for i in range(len(df[List[0]])):
                a = []
                for j in range(len(List) - 1):
                    a.append(format(df[List[j + 1]][i], "e"))
                x.append(a)
                y.append(format(df[List[0]][i], "e"))
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
            forest = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)  # 分类
            forest.fit(x_train, y_train)
            b1 = []
            b2 = []
            for i in List_YuCe:
                b1.append(format(i, "e"))
            b2.append(b1)
            return float(forest.predict(b2)[0])

    def ListYearPerson_2021YuCe(self):
        ListYearPerson_2021_YuCe=[float(self.IGT.get()),float(self.IFG.get()),float(self.Money.get())]
        a1 = self.SuiJiSenLin(self.ListYearPerson_2021_cols,ListYearPerson_2021_YuCe)
        tkinter.messagebox.showinfo(title='随机森林', message='随机森林_患病人数(1000s):\n'+str(a1))
    def ListYearPersonPrevalence_2021YuCe(self):
        ListYearPersonPrevalence_2021_YuCe=[float(self.OverWeight.get()),float(self.Obesity.get()),float(self.SafetyIndex.get()),float(self.HealthCareIndex.get()),float(self.PollutionIndex.get())]
        a2 = self.SuiJiSenLin(self.ListYearPersonPrevalence_2021_cols,ListYearPersonPrevalence_2021_YuCe)
        tkinter.messagebox.showinfo(title='随机森林', message='随机森林_年龄调整比较患病率:\n'+str(a2))
if __name__=='__main__':
    root=tk.Tk()
    page1(root)
    root.mainloop()