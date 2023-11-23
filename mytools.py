# 导入各种包
import pandas as pd
from pyreadstat import pyreadstat
import matplotlib.pyplot as plt



def 绘制饼图(数据表, 变量):
 # 定义数据  
  labels = ['A', 'B', 'C', 'D'] 
  sizes = [15, 30, 45, 10] 
# 绘制饼图  
  plt.pie(sizes, labels=labels, autopct='%1.1f%%') 
# 添加图例  
  plt.legend() 
# 显示图形  
  plt.show()


#绘图设置
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体

#读取spss格式数据

def 绘制单个类别变量柱状图(数据表,变量:str):
    
    # 生成x、y轴方向的坐标
  x = 数据表['变量'].value_counts().index
  y = 数据表['变量'].value_counts(normalize=True).values * 100
# 创建图
  fig, ax = plt.subplots()
# 绘制柱状图
  rects1 = ax.bar(x, y)
# 设置x轴变量名称
  ax.set_xlabel(ymax=100)
# 设置y轴最大值
  ax.set_ylim(ymax=100)
# 在柱上方显示对应的值
  ax.bar_label(rects1, fmt="%.1f", padding=3)
# 显示图形
plt.show()







def 读取spss数据(文件所在位置及名称):
    result,metadata = pyreadstat.read_sav(
        文件所在位置及名称, apply_value_formats=True,
        formats_as_ordered_category=True)
    国家认同原始表, metadata = pyreadstat.read_sav(r'data/identity.sav',
    apply_value_formats=True,formats_as_ordered_category=True)
    return result,metadata


def 有序变量描述统计函数(表名,变量名):
    result = 表名['变量名'].value_counts(sort=False)
    描述统计表 = pd.DataFrame(result)
    描述统计表['比例'] = 描述统计表['count']/描述统计表['count'].sum()
    描述统计表['累计比例'] = 描述统计表['比例'].cumsum()
    return 描述统计表

def 数值变量描述统计1(数据表, 变量名):
    result = 数据表[变量名].describe()
    中位数 = result['median']
    平均值 = result['mean']
    标准差 = result['std']
    return 中位数, 平均值, 标准差

def 数值变量描述统计(数据表, 变量名):
    """ 对数值变量进行描述统计 """
    result = 数据表[变量名].describe()
    return result


def goodmanKruska_tau_y(df, x: str, y: str) -> float:
    """ 计算两个定序变量相关系数tau_y """
    """ 取得条件次数表 """
    cft = pd.crosstab(df[y], df[x], margins=True)
    """ 取得全部个案数目 """
    n = cft.at['All', 'All']
    """ 初始化变量 """
    E_1 = E_2 = tau_y = 0

    """ 计算E_1 """
    for i in range(cft.shape[0] - 1):
        F_y = cft['All'][i]
        E_1 += ((n - F_y) * F_y) / n
    """ 计算E_2 """
    for j in range(cft.shape[1] - 1):
        for k in range(cft.shape[0] - 1):
            F_x = cft.iloc[cft.shape[0] - 1, j]
            f = cft.iloc[k, j]
            E_2 += ((F_x - f) * f) / F_x
    """ 计算tauy """
    tau_y = (E_1 - E_2) / E_1

    return tau_y

def 相关系数强弱判断(相关系数值):
    """ 相关系数强弱的判断 """
    if 相关系数值 >= 0.8:
        return '极强相关'
    elif 相关系数值 >= 0.6:
        return '强相关'
    elif 相关系数值 >= 0.4:
        return '中等程度相关'
    elif 相关系数值 >= 0.2:
        return '弱相关'
    else:
        return '极弱相关或无相关'

def 制作交叉表(数据表, 自变量, 因变量):
    return pd.crosstab(数据表[自变量], 数据表[因变量], normalize='columns', margins=True)




