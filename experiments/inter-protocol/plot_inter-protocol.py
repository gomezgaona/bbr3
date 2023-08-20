import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

def extract_iperf_summary(filename):
    
    f = open(filename)
    data = json.loads(open(filename).read())

    throughput = data['end']['sum_sent']['bits_per_second']/1e9

    return throughput

def plot_timing_2_flows():
    global plt, np
    BDP = [ 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}
    f_size = 26
    matplotlib.rc('font', **font)
    Runs = 10

    cubic = []
    bbr3 = []
    for bdp in BDP:
        tmp_cubic = 0
        tmp_bbr3 = 0
        for i in range(1, Runs + 1):
            tmp_cubic += extract_iperf_summary(f'2_flows/h1_cubic_{bdp}BDP_out_{i}.json')
            tmp_bbr3 += extract_iperf_summary(f'2_flows/h2_bbr_{bdp}BDP_out_{i}.json')
        cubic.append(tmp_cubic/10)
        bbr3.append(tmp_bbr3/10)

    print(cubic)
    print(bbr3)
 
    fairness = [0 for i in range(len(cubic))] 

    for i in range(0, len(cubic)):
        fairness[i] += 100*(cubic[i] + bbr3[i])**2 / (2 * (cubic[i]**2 + bbr3[i]**2))
    print(fairness)

    ##########################Plotting###########################
    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : 26}
    f_size = 26
    fig, plt = plt.subplots(2, 1, sharex=True,figsize=(10,8))
    fig.subplots_adjust(hspace=0.1)

    #Plot grids
    plt[0].grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
    plt[1].grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')

    #plt[1].xscale("log")

    #Colors
    #Gold: #E5B245
    #Blue: #2D72B7 
    #Green: #82AA45
    #Garnet: #95253B

    #Plotting the metrics as a time's function
    plt[0].semilogx(BDP, fairness,'#E5B245', linewidth=2, label='Fairness',marker ='o')
    plt[1].semilogx(BDP,cubic,'#2D72B7', linewidth=2, label='CUBIC',marker ='o')
    plt[1].semilogx(BDP, bbr3,'#95253B', linewidth=2, label='BBRv3',marker ='o')

    #Setting the y-axis labels and the x-axis label
    plt[0].set_ylabel('Fairness [%]', fontsize=f_size)
    plt[1].set_ylabel('Throughput [Gbps]', fontsize=f_size)
    plt[1].set_xlabel('Buffer size [BDP]', fontsize=f_size)

    #Plot legends
    plt[0].legend(loc="lower right", fontsize=f_size)
    plt[1].legend(loc="upper right", ncol=2, fontsize=f_size)


    #Setting the position of the y-axis labels
    plt[0].yaxis.set_label_coords(-0.12, 0.5)
    plt[1].yaxis.set_label_coords(-0.12, 0.5)

    #Setting the x-axis labels font size
    plt[0].tick_params(axis='y', labelsize=f_size)
    plt[1].tick_params(axis='y', labelsize=f_size)
    plt[1].tick_params(axis='x', labelsize=f_size)

    #Setting the y-axis limits
    plt[0].set_ylim([50, 105])#fairness
    plt[1].set_ylim([0, 1.2])#throughput

    fig.savefig("inter-protocol_2_flows.pdf", bbox_inches='tight')


def plot_timing_100_flows():
    global plt, np
    BDP = [ 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}
    f_size = 26
    matplotlib.rc('font', **font)
    Runs = 10
    Flows = 100

    cubic = []
    bbr3 = []
    for bdp in BDP:
        tmp_cubic = 0
        tmp_bbr3 = 0
        for i in range(1, Runs + 1):
            for flows in range(1, Flows + 1):
                if flows <= Flows/2:
                    tmp_cubic += extract_iperf_summary(f'100_flows_loss/h{flows}_cubic_{bdp}BDP_out_{i}.json')
                else:
                    tmp_bbr3 += extract_iperf_summary(f'100_flows_loss/h{flows}_bbr_{bdp}BDP_out_{i}.json')
        cubic.append(tmp_cubic/10)
        bbr3.append(tmp_bbr3/10)

    print(cubic)
    print(bbr3)
 
    fairness = [0 for i in range(len(cubic))] 

    for i in range(0, len(cubic)):
        fairness[i] += 100*(cubic[i] + bbr3[i])**2 / (2 * (cubic[i]**2 + bbr3[i]**2))
    print(fairness)

    ##########################Plotting###########################
    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : 26}
    f_size = 26
    fig, plt = plt.subplots(2, 1, sharex=True,figsize=(10,8))
    fig.subplots_adjust(hspace=0.1)

    #Plot grids
    plt[0].grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
    plt[1].grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')

    #plt[1].xscale("log")

    #Colors
    #Gold: #E5B245
    #Blue: #2D72B7 
    #Green: #82AA45
    #Garnet: #95253B

    #Plotting the metrics as a time's function
    plt[0].semilogx(BDP, fairness,'#E5B245', linewidth=2, label='Fairness',marker ='o')
    plt[1].semilogx(BDP,cubic,'#2D72B7', linewidth=2, label='CUBIC',marker ='o')
    plt[1].semilogx(BDP, bbr3,'#95253B', linewidth=2, label='BBRv3',marker ='o')

    #Setting the y-axis labels and the x-axis label
    plt[0].set_ylabel('Fairness [%]', fontsize=f_size)
    plt[1].set_ylabel('Throughput [Gbps]', fontsize=f_size)
    plt[1].set_xlabel('Buffer size [BDP]', fontsize=f_size)

    #Plot legends
    plt[0].legend(loc="lower right", fontsize=f_size)
    plt[1].legend(loc="upper right", ncol=2, fontsize=f_size)


    #Setting the position of the y-axis labels
    plt[0].yaxis.set_label_coords(-0.12, 0.5)
    plt[1].yaxis.set_label_coords(-0.12, 0.5)

    #Setting the x-axis labels font size
    plt[0].tick_params(axis='y', labelsize=f_size)
    plt[1].tick_params(axis='y', labelsize=f_size)
    plt[1].tick_params(axis='x', labelsize=f_size)

    #Setting the y-axis limits
    plt[0].set_ylim([50, 105])#fairness
    plt[1].set_ylim([0, 1.2])#throughput

    fig.savefig("inter-protocol_100_flows_loss.pdf", bbox_inches='tight')

def main():
    #plot_timing_2_flows()
    plot_timing_100_flows()

if __name__ == '__main__':
    main()
    

