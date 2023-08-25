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
duration=360*2
cc = 'bbr2'
N_Run = 1

cubic = extract_throughput(f"50ms/cubic_{N_Run}_q_occupancy.dat")
bbr = extract_throughput(f"50ms/bbr_{N_Run}_q_occupancy.dat")
bbr2 = extract_throughput(f"50ms/bbr2_{N_Run}_q_occupancy.dat")
t = range(0, duration)
##########################Plotting###########################

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}    
f_size = 26
matplotlib.rc('font', **font)

fig, plt = plt.subplots(1, 1, sharex=True,figsize=(10.5,6.75))
fig.subplots_adjust(hspace=0.1)

step = 40*2
BDP = 10e9*50e-3/8/1e6
q = BDP*np.ones(step)
q1 = 2*BDP*np.ones(step)
q2 = 3*BDP*np.ones(step)
q3 = 4*BDP*np.ones(step)
q4 = 4*BDP*np.ones(step)
q5 = 3*BDP*np.ones(step)
q6 = 2*BDP*np.ones(step)
q7 = BDP*np.ones(2*step)
q = np.append(q, q1) 
q = np.append(q, q2)
q = np.append(q, q3) 
q = np.append(q, q4) 
q = np.append(q, q5)
q = np.append(q, q6)
q = np.append(q, q7)

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
plt.plot(t, q,     '#82AA45', linewidth=2, label='Buffer Size')  #label='Fairness', marker ='o'
plt.plot(t, cubic, '#E5B245', linewidth=2, label='CUBIC')  #label='Fairness', marker ='o'
plt.plot(t, bbr,   '#95253B', linewidth=2, label='BBRv1')  #label='Fairness', marker ='o'
plt.plot(t, bbr2,  '#13b5d1', linewidth=2, label='BBRv2')  #label='Fairness', marker ='o'

#Setting the y-axis labels and the x-axis label
plt.set_ylabel('Buffer Size [MBytes]', fontsize=f_size)
plt.set_xlabel('Time [seconds]', fontsize=f_size)

#Plot legends
#plt.legend(loc="lower right", fontsize=f_size)
plt.legend(loc="upper right", ncol=2, fontsize=21)

#Setting the position of the y-axis labels
plt.yaxis.set_label_coords(-0.15, 0.5)
plt.yaxis.set_label_coords(-0.15, 0.5)

#Setting the x-axis labels font size
#plt.tick_params(axis='y', labelsize=f_size)
#plt.tick_params(axis='y', labelsize=f_size)
#plt.tick_params(axis='x', labelsize=f_size)

#Setting the y-axis limits
plt.set_ylim([0,350])#throughput
plt.set_xlim([0,duration])#fairness

fig.savefig(f"q_occupancy.pdf", bbox_inches='tight')