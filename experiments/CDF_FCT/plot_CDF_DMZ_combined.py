import csv
import numpy as np
p4bs = []
i=0
with open("large_flows_w_policing_test11_100Gbytes.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        i+=1
        if (i < 10):
            continue
        p4bs.append(abs(float(row[6]) - float(row[5])))

 

p4bs = np.sort(p4bs)
freq_1 = np.zeros(len(p4bs))
freq_1[0] = 1/len(p4bs)
for i in range(1,len(p4bs)):
    freq_1[i] = freq_1[i-1] + 1/len(p4bs)

 


stanford = []
i=0
with open("large_flows_wo_policing_test12_100Gbytes.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        i+=1
        if (i < 10):
            continue
        stanford.append(abs(float(row[6]) - float(row[5])))

 

stanford= np.sort(stanford)
freq_2 = np.zeros(len(stanford))
freq_2[0] = 1/len(stanford)
for i in range(1,len(stanford)):
    freq_2[i] = freq_2[i-1] + 1/len(stanford)

 


 


 

freqs_len = []
freqs_len.append(len(freq_1))
freqs_len.append(len(freq_2))


 

freqs = []
freqs.append(freq_1)
freqs.append(freq_2)


 

freq = np.argmin(freqs_len)
freq = freqs[freq]

import matplotlib
import matplotlib.pyplot as plt
font = {'family' : 'normal',
     'weight' : 'normal',
     'size'   : 30}
f_size = 30
matplotlib.rc('font', **font)

# With policing
standard_deviation = np.std(p4bs)
stdev_1 = "{:.2f}".format(standard_deviation)
print("Standard Deviation:", stdev_1)
mean_value = np.mean(p4bs)
mean_1 = "{:.2f}".format(mean_value)
print("Mean Value:", mean_1)

# Without policing
standard_deviation = np.std(stanford)
stdev_2 = "{:.2f}".format(standard_deviation)
print("Standard Deviation:", stdev_2)
mean_value = np.mean(stanford)
mean_2 = "{:.2f}".format(mean_value)
print("Mean Value:", mean_2)

#Red: #A2142F
#Green: #77ac30
fig = plt.figure()
plt.figure(figsize=(10, 8))
plt.plot(p4bs[0:len(freq)], freq, c='#77ac30', label=f'w/ policing\n \u03BC = {mean_1}\n \u03C3 = {stdev_1}')
plt.plot(stanford[0:len(freq)], freq, c='#A2142F', label=f'wo/ policing\n \u03BC = {mean_2}\n \u03C3 = {stdev_2}')
plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
plt.legend(loc='lower right')
plt.xlabel('Flow completion time [s]')
plt.ylabel('CDF')    
plt.xlim(-0.1,1.5)
#plt.title('N = 1000')

#plt.legend()
plt.savefig('FCT_combined.pdf', format='pdf')
plt.show()
