import matplotlib.pyplot as plt
import numpy as np
import re
import json
import matplotlib

def extract_throughput(filename):
    f = open(filename)
    data = f.readlines()
    f.close()
    
    for i in range(0, len(data)):
        data[i]= float(data[i])/1e6
        
    return data

####################Main############################
duration = 480
cc = 'bbr2'
N_Run = 1

cubic = extract_throughput(f"cubic.dat")
bbr3 = extract_throughput(f"bbr.dat")
t = range(0, duration)
##########################Plotting###########################

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}    
f_size = 26
matplotlib.rc('font', **font)

fig, plt = plt.subplots(1, 1, sharex=True,figsize=(10.5,6.75))
fig.subplots_adjust(hspace=0.1)

step = 60
BDP = [0.1, 0.2, 0.5, 0.5, 0.2, 0.1]
q = BDP[0]*np.ones(step)
q1 = BDP[1]*np.ones(step)
q2 = BDP[2]*np.ones(step)
q3 = BDP[3]*np.ones(step)
q4 = BDP[4]*np.ones(step)
q5 = BDP[5]*np.ones(step)
q = np.append(q, q1) 
q = np.append(q, q2)
q = np.append(q, q3) 
q = np.append(q, q4) 
q = np.append(q, q5)
q = np.append(q, q5)
q = np.append(q, q5)

#Plot grids
plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')

#Colors
#Gold: #E5B245
#Blue: #2D72B7 
#Green: #82AA45
#Garnet: #95253B
#Orange: #FFA500

#Plotting the metrics as a time's function
plt.plot(t, q,     '#E5B245', linewidth=2, label='Buffer Size')  #label='Fairness', marker ='o'
plt.plot(t, cubic, '#2D72B7', linewidth=2, label='CUBIC')  #label='Fairness', marker ='o'
plt.plot(t, bbr3,  '#95253B', linewidth=2, label='BBRv3')  #label='Fairness', marker ='o'

custom_y_labels = ['0.5', '1', '10', '10', '1', '0.5']

plt.set_yticks(BDP)
plt.set_yticklabels(custom_y_labels)

#Setting the y-axis labels and the x-axis label
plt.set_ylabel('Buffer Size [BDP]', fontsize=f_size)
plt.set_xlabel('Time [seconds]', fontsize=f_size)

#Plot legends
#plt.legend(loc="lower right", fontsize=f_size)
plt.legend(loc="upper right", ncol=1, fontsize=21)

#Setting the position of the y-axis labels
#plt.yaxis.set_label_coords(-0.11, 0.5)
plt.yaxis.set_label_coords(-0.09, 0.5)

#Setting the x-axis labels font size
#plt.tick_params(axis='y', labelsize=f_size)
#plt.tick_params(axis='y', labelsize=f_size)
#plt.tick_params(axis='x', labelsize=f_size)

#Setting the y-axis limits
#plt.set_ylim([0,3])#throughput
#plt.set_xlim([0,duration])#fairness

fig.savefig(f"q_occupancy.pdf", bbox_inches='tight')