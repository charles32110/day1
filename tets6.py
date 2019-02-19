import numpy as np
import matplotlib.pyplot as plt
#参数，start，stop，num（点的数量）
x_coords=np.linspace(-100,100,1000)
y_coords=np.linspace(-100,100,1000)
#用于收集各个点的list
points=[]
#收集点数
for y in y_coords:
    for x in x_coords:
        if ((x*0.03)**2+(y*0.03)**2-1)**3-(x*0.03)**2*(y*0.035)**3 <= 0:
            #将符合标准的点添加进去
            points.append({"x": x, "y": y})
#获取x的坐标,map(function, iterable, ...)，返回迭代器，这是使用匿名函数（lambda）
heart_x=list(map(lambda point:point['x'],points))
#获取y的坐标
heart_y=list(map(lambda point:point['y'],points))
#画图,其中alpha：  cmap：画图的颜色 s（size）：点的大小
plt.scatter(heart_x, heart_y, s=6, c=range(len(heart_x)), cmap="winter")
#去掉坐标轴
plt.axis("off")
# 显示
plt.show()







