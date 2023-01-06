
import matplotlib.pyplot as plt
x=('2001','2002','2003','2004','2005','2006','2007')
y=('12000','35000','56000','78000','130000','85000','450000')
plt.xlabel('year')
plt.ylabel('car value')
plt.title('value depreciation',loc='left')
plt.plot(marker='*',Color='blue',ms='10')
plt.plot(LineStyle='dash-dot',LineColor='cyan')
plt.show()

