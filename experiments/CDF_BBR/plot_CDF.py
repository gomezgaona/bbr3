import matplotlib.pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}    
f_size = 26
matplotlib.rc('font', **font)

def extract_throughput(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())/1e9  # Convert line to float (or int if applicable)
                numbers.append(number)
            except ValueError:
                # Line does not contain a valid number
                pass
    return numbers

data = extract_throughput("out.dat")

#duration = len(data)
#t = range(0, duration)

data_x = np.sort(data)
cdf = np.arange(1, len(data_x) + 1) / float(len(data_x))

##########################Plotting###########################

fig, plt = plt.subplots(1, 1, sharex=True,figsize=(10.5,6.75))
fig.subplots_adjust(hspace=0.1)

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
plt.plot(data_x, cdf,     '#82AA45', linewidth=2, label='BBR')  #label='Fairness', marker ='o'

#Setting the y-axis labels and the x-axis label
plt.set_ylabel('CDF', fontsize=f_size)
plt.set_xlabel('Estimated Bandwidth [Gbps]', fontsize=f_size)

#Plot legends
#plt.legend(loc="lower right", fontsize=f_size)
plt.legend(loc="upper left", ncol=2, fontsize=21)

#Setting the position of the y-axis labels
plt.yaxis.set_label_coords(-0.15, 0.5)
plt.yaxis.set_label_coords(-0.15, 0.5)

#Setting the x-axis labels font size
#plt.tick_params(axis='y', labelsize=f_size)
#plt.tick_params(axis='y', labelsize=f_size)
#plt.tick_params(axis='x', labelsize=f_size)

#Setting the y-axis limits
plt.set_ylim([0,1])#throughput
plt.set_xlim([8,20])#fairness

fig.savefig(f"estimated_bandwidth.pdf", bbox_inches='tight')

