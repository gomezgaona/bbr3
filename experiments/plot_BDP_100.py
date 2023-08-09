import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json



def extract_iperf_summary(CC, BDP, start, end):

    throughput = 0

    for i in range(start, end + 1):
        filename = f"json_files/h{i}_{CC}_{BDP}BDP_out.json"
        f = open(filename)
        data = json.loads(open(filename).read())
        throughput += data['end']['sum_sent']['bits_per_second']/1e9

    return throughput

def plot_timing():
    global plt, np
    BDP = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}
    f_size = 26
    matplotlib.rc('font', **font)

    tput_flow_1 = []
    tput_flow_2 = []
    for bdp in BDP:
        tput_flow_1.append(extract_iperf_summary("bbr", bdp, 1,50))
        tput_flow_2.append(extract_iperf_summary("cubic", bdp, 51, 100))

    print(tput_flow_1)
    print(tput_flow_2)
    
    fairness = [0 for i in range(len(tput_flow_1))] 
    t = range(0,len(tput_flow_1))
        
    for i in range(0, len(tput_flow_1)):
        fairness[i] += 100*(tput_flow_1[i] + tput_flow_2[i])**2 / (2 * (tput_flow_1[i]**2 + tput_flow_2[i]**2))
    print(fairness)

    ##########################Plotting###########################
    font = {'family' : 'normal',
            'weight' : 'normal',
            'size'   : 22}
    f_size = 22
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
    plt[1].semilogx(BDP, tput_flow_1,'#2D72B7', linewidth=2, label='CUBIC',marker ='o')
    plt[1].semilogx(BDP, tput_flow_2,'#95253B', linewidth=2, label='BBRv3',marker ='o')

    #Setting the y-axis labels and the x-axis label
    plt[0].set_ylabel('Fairness [%]', fontsize=f_size)
    plt[1].set_ylabel('Throughput [Gbps]', fontsize=f_size)
    plt[1].set_xlabel('Buffer size [BDP]', fontsize=f_size)

    #Plot legends
    plt[0].legend(loc="upper left", fontsize=f_size)
    plt[1].legend(loc="upper left", ncol=2, fontsize=f_size)


    #Setting the position of the y-axis labels
    plt[0].yaxis.set_label_coords(-0.12, 0.5)
    plt[1].yaxis.set_label_coords(-0.12, 0.5)

    #Setting the x-axis labels font size
    plt[0].tick_params(axis='y', labelsize=f_size)
    plt[1].tick_params(axis='y', labelsize=f_size)
    plt[1].tick_params(axis='x', labelsize=f_size)

    #Setting the y-axis limits
    plt[0].set_ylim([50, 109])#fairness
    plt[1].set_ylim([0, 12.1])#throughput

    fig.savefig("BDP_10G_100hosts.pdf", bbox_inches='tight')

def main():
    plot_timing()

if __name__ == '__main__':
    main()
    

