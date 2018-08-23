import matplotlib.pyplot as plt
import csv

laser_y = []
radar_y = []
x = []
nis_p = []

count = 0
with open('./data/laser_nis.dat','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        count += 1
        for i,nis in enumerate(row):
            laser_y.append(float(nis))
            nis_p.append(7.8)
            x.append(i*count)
            print(i*count)
plt.figure()
plt.plot(x, laser_y, label='NIS Laser')
plt.plot(x,  nis_p, label='95%')
plt.xlabel('samples')
plt.ylabel('LASER NIS')
plt.title('Laser NIS')
plt.legend()

with open('./data/radar_nis.dat','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        count += 1
        for i,nis in enumerate(row):
            radar_y.append(float(nis))
            print(i*count)

plt.figure()
plt.plot(x, radar_y,  label='NIS Radar')
plt.plot(x,  nis_p,  label='95%')
plt.xlabel('samples')
plt.ylabel('Radar NIS')
plt.title('Radar NIS')
plt.legend()
plt.show()