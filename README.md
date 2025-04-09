# 基于IDF的全球糖尿病数据分析

Global diabetes data analysis based on IDF  

**汇报时间**：2024年5月  
---
**特别说明**：该项目的网址是2024年4月之前使用的，不能保证后期能够正常使用（网站数据更新，数据删除等可能造成404）


---

## 目录
1. [选题背景](#选题背景)  
2. [数据获取与清洗](#数据获取与清洗)  
3. [数据展示与可视化](#数据展示与可视化)  
4. [建模与预测](#建模与预测)  
5. [小组分工](#小组分工)  

---

## 选题背景
2021年全球约有5.37亿成年人患有糖尿病，而预计到2030年，这一数字将增至6.43亿。同时，2021年约有670万人死于糖尿病。糖尿病已成为全球性的重大公共卫生问题，对人们的健康和生命安全造成了严重威胁。


### 研究意义
- **数据来源**：
-               国际糖尿病联盟（IDF）糖尿病地图集（[官网链接](https://diabetesatlas.org/data/en/country/1/af.html)）。
- ![示例图像](/image/Http/糖尿病.png)
-               Numbeo（[官网链接](https://www.numbeo.com/quality-of-life/)）
- ![示例图像](/image/Http/Numbeo.png)
-               全球肥胖观察网站（[官网链接](https://data.worldobesity.org/tables/prevalence-of-adult-overweight-obesity-2/)）
- ![示例图像](/image/Http/肥胖网.png)
- **全球现状**（2021年）：  
  - 糖尿病患者：5.37亿成年人（20-79岁），其中2.4亿未确诊。  
  - 死亡人数：670万（平均每5秒1人死亡）。  
  - 预测：2030年患者数将增至6.43亿。  
- **补充概念**：  
  - **IGT（糖耐量减低）**：糖尿病前期状态，增加2型糖尿病风险。
  -  
  - **IFG（空腹血糖受损）**：空腹血糖异常，提示糖尿病风险。  

---

## 数据获取与清洗
### 数据来源
1. **IDF官网**：爬取222个国家2011-2045年的数据，包括：  
   - 糖尿病患病率、IGT/IFG人数及患病率、医疗支出等。  
2. **补充数据**：  
   - 肥胖率、超重率（Numbeo网站）。  
   - 生活质量指数、污染指数等（全球肥胖观察网站）。  

### 数据处理
- **爬虫工具**：BeautifulSoup解析HTML，提取国家名称、数据链接及表格内容。  
- **清洗步骤**：  
  - 处理无效数据（如`--*`）。  
  - 统一国家名称（如修正“Hong Kong”为“China”）。  
  - 填充缺失值（超重/肥胖数据缺失时设为0）。  

---

## 数据展示与可视化
### 1. 全球地图
- **2021年糖尿病年龄调整患病率**：  
  - 中国患病率较高（示例：智利为10.8%）。  
- **2021年IGT患病率**：中国最高（40.4%）。  
- **2021年医疗支出**：中国、美国支出最高（加拿大：142亿美元）。  

**优势**：直观展示国家间差异，快速识别异常值。  

### 2. 折线图
- **趋势对比**：同一国家不同年份或不同国家间对比。  
  - 示例：中国患病人数及患病率均高于俄罗斯（原因：人口老龄化、饮食结构等）。  

---

## 建模与预测
### 1. 相关性分析
- **热力图**：  
  - 正相关：肥胖率（0.48）、超重率（0.57）、污染指数（0.55）。  
  - 负相关：安全指数（-0.58）、医疗指数（-0.61）。  

### 2. 预测模型
| 模型                | MSE   | 预测结果（示例）       |
|---------------------|-------|------------------------|
| 梯度提升回归（GBR） | 7.67  | 预测值：13.24%（实际：10.9%） |
| 随机森林            | 6.30  | 预测值：10.9%（与实际一致）  |

**特征重要性**（随机森林）：  
- 超重、肥胖、安全指数、医疗指数、污染指数贡献均衡（重要性0.17-0.22）。  

---

## 小组分工
| 任务                | 负责人       |
|---------------------|--------------|
| 项目规划与协调      | 伍鑫         |
| 爬虫开发            | 伍鑫         |
| 数据清洗与预处理    | 乔妍妍       |
| 数据分析与可视化    | 杨若妍       |
| 机器学习建模        | 伍鑫、杨若妍 |

---

**感谢阅读！**  
完整代码及数据见项目仓库。  
