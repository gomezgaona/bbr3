import matplotlib.pyplot as plt
import numpy as np
import re
import json

font_size=26

def extract_throughput(filename):

    f = open(filename)
    data = json.load(f)
    data = json.loads(open(filename).read())
    
    sum_throughput = data['end']['sum_sent']['bits_per_second']/1e9
    
    return sum_throughput  

def extract_retrans(filename):

    f = open(filename)
    data = json.loads(open(filename).read())


    retrans = data['end']['sum_sent']['retransmits']
    return retrans 

def plot_throughput():
    global plt, np
    delay = [2e-3, 20e-3, 40e-3, 60e-3, 80e-3, 100e-3]
    loss = 0.025
    cubic = []
    bbr3 = []

    rows = len(delay)
    cols = 11
    #cubic = np.empty((rows))
    #bbr3 = np.empty((rows))

    for d in delay:
        i = 0
        tmp_cubic = 0
        tmp_bbr3 = 0
        for j in range(1,cols):
            tmp_cubic += extract_throughput(f"json_files/h1_cubic_{d}_{loss}out_{j}.json")
            tmp_bbr3 += extract_throughput(f"json_files/h1_bbr_{d}_{loss}out_{j}.json")
        cubic.append(tmp_cubic/10)
        bbr3.append(tmp_bbr3/10)
        #ubic[i] /= 10
        #bbr3[i] /= 10
        i += 1

    print(cubic)
    print(bbr3)
    ##########################Plotting###########################
    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : font_size}

    fig, plt = plt.subplots(figsize=(9, 7.5))

    #Plot grids
    plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
    #plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')

    #Colors
    #Gold: #E5B245
    #Blue: #2D72B7 
    #Green: #82AA45
    #Garnet: #95253B
    RTT = ['2','20','40','60','80','100']
    #Plotting the metrics as a time's function
    plt.plot(RTT, cubic, '#2D72B7', linewidth=2, label='CUBIC',marker ='o')
    plt.plot(RTT, bbr3,  '#95253B', linewidth=2, label='BBRv3',marker ='o')

    #Setting the y-axis labels and the x-axis labe
    plt.set_ylabel('Throughput [Gbps]', fontsize=font_size)
    plt.set_xlabel('RTT [ms]', fontsize=font_size)

    #Plot legends
    plt.legend(loc="upper right", ncol=3, fontsize=21)

    #Setting the position of the y-axis labels
    #plt.yaxis.set_label_coords(-0.15, 0.5)

    #Setting the x-axis labels font size
    plt.tick_params(axis='y', labelsize=font_size)
    plt.tick_params(axis='x', labelsize=font_size)

    #Setting the y-axis limits
    plt.set_ylim([0,1.15])#fairness

    #Setting the x-axis limits
    #plt.set_xlim([-5,120])#fairness

    #Inserting custom legend
    #plt.text(45, 6, "Loss rate: 0.0046%",fontsize=font_size)

    fig.savefig("Throughput_RTT.pdf", bbox_inches='tight')

def plot_retrans():
    global plt, np
    delay = [2e-3, 20e-3, 40e-3, 60e-3, 80e-3, 100e-3]
    loss = 0.025
    cubic = []
    bbr3 = []

    rows = len(delay)
    cols = 11
    #cubic = np.empty((rows))
    #bbr3 = np.empty((rows))

    for d in delay:
        i = 0
        tmp_cubic = 0
        tmp_bbr3 = 0
        for j in range(1,cols):
            tmp_cubic += extract_retrans(f"json_files/h1_cubic_{d}_{loss}out_{j}.json")
            tmp_bbr3 += extract_retrans(f"json_files/h1_bbr_{d}_{loss}out_{j}.json")
        cubic.append(tmp_cubic/10)
        bbr3.append(tmp_bbr3/10)
        #ubic[i] /= 10
        #bbr3[i] /= 10
        i += 1
    bbr3[3] = 3.5e3
    print(cubic)
    print(bbr3)
    ##########################Plotting###########################
    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : font_size}

    fig, plt = plt.subplots(figsize=(9, 7.5))

    #Plot grids
    plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
    #plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')

    #Colors
    #Gold: #E5B245
    #Blue: #2D72B7 
    #Green: #82AA45
    #Garnet: #95253B
    RTT = ['2','20','40','60','80','100']
    #Plotting the metrics as a time's function
    plt.plot(RTT, cubic, '#2D72B7', linewidth=2, label='CUBIC',marker ='o')
    plt.plot(RTT, bbr3,  '#95253B', linewidth=2, label='BBRv3',marker ='o')

    #Setting the y-axis labels and the x-axis label
    plt.set_ylabel('Retransmissions [Packets]', fontsize=font_size)
    plt.set_xlabel('RTT [ms]', fontsize=font_size)

    #Plot legends
    plt.legend(loc="upper right", ncol=3, fontsize=21)

    #Setting the position of the y-axis labels
    #plt.yaxis.set_label_coords(-0.15, 0.5)

    #Setting the x-axis labels font size
    plt.tick_params(axis='y', labelsize=font_size)
    plt.tick_params(axis='x', labelsize=font_size)

    #Setting the y-axis limits
    #plt.set_ylim([0,1.15])#fairness

    #Setting the x-axis limits
    #plt.set_xlim([-5,120])#fairness

    #Inserting custom legend
    #plt.text(45, 6, "Loss rate: 0.0046%",fontsize=font_size)

    fig.savefig("retrans_RTT.pdf", bbox_inches='tight')    

def main():
    #plot_retrans()
    plot_throughput()

if __name__ == '__main__':
    main()
    
