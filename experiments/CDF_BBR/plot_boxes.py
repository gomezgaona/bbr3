import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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


font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}
f_size = 26
matplotlib.rc('font', **font)

cc="bbr"
# Generate some random data
data_1 = extract_throughput(f"results/{cc}_10_sw.dat")
data_2 = extract_throughput(f"results/{cc}_20_sw.dat")
data_3 = extract_throughput(f"results/{cc}_30_sw.dat")
data_4 = extract_throughput(f"results/{cc}_40_sw.dat")
data_5 = extract_throughput(f"results/{cc}_50_sw.dat")
data_6 = extract_throughput(f"results/{cc}_60_sw.dat")
data_7 = extract_throughput(f"results/{cc}_70_sw.dat")
data_8 = extract_throughput(f"results/{cc}_80_sw.dat")
data_9 = extract_throughput(f"results/{cc}_90_sw.dat")
data_10 = extract_throughput(f"results/{cc}_100_sw.dat")
#data_11 = extract_throughput(f"results/{cc}_110.dat")
#data_12 = extract_throughput(f"results/{cc}_120.dat")

data = [data_1, data_2, data_3, data_4,
        data_5, data_6, data_7, data_8,
        data_9, data_10]#, data_11, data_12]

# Create a figure and axes
fig, ax = plt.subplots(1, 1, sharex=True,figsize=(10,8))

# Create a boxplot
ax.boxplot(data, showfliers=False,medianprops = dict(color = "black", linewidth = 1.0))

# Customize the plot
ax.set_xticklabels(['10', '20', '30', '40',
                    '50', '60', '70', '80',
                    '90', '100'])#, '110', '120',])
ax.set_xlabel('Propagataion delay [ms]')
ax.set_ylabel('Throughput [Gbps]')
#ax.set_title('R')
#ax.set_ylim(0.9,1.05, 0.005)
ax.set_yticks(np.arange(0.9, 1.05, 0.05))
# Show the plot
plt.show()
fig.savefig(f"{cc}_boxplot_sw.pdf", bbox_inches='tight')