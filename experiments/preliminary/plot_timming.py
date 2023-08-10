import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json



def extract_iperf_timing(filename):
    
    f = open(filename)
    data = json.loads(open(filename).read())

    duration = data['start']['test_start']['duration']
    throughput = []

    for i in range(0,duration):
        throughput.append(data['intervals'][i]['sum']['bits_per_second']/1e9)

    return throughput

def plot_timing():
    global plt, np

    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}
    f_size = 26
    matplotlib.rc('font', **font)

    tput_flow_1 = extract_iperf_timing('json_files/h1_cubic_out.json')
    tput_flow_2 = extract_iperf_timing('json_files/h2_bbr_out.json')
    
    fig, plt = plt.subplots(1, 1, sharex=True,figsize=(10.5,6.75))
    fig.subplots_adjust(hspace=0.1)

    # Plot grids
    plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
    plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')

    # Colors
    #Gold: #E5B245
    #Blue: #2D72B7 
    #Green: #82AA45
    #Garnet: #95253B
    #Orange: #FFA500

    t = range(0, len(tput_flow_1) )
    print(len(tput_flow_2))

    # Plotting the metrics as a time's function
    plt.plot(t, tput_flow_1, '#82AA45', linewidth=2, label='CUBIC')  #label='Fairness', marker ='o'
    plt.plot(t, tput_flow_2, '#E5B245', linewidth=2, label='BBRv3')  #label='Fairness', marker ='o'
    

    # Setting the y-axis labels and the x-axis label
    plt.set_ylabel('Throughput [Gbps]', fontsize=f_size)
    plt.set_xlabel('Time [seconds]', fontsize=f_size)

    # Plot legends
    plt.legend(loc="upper right", ncol=2, fontsize=21)

    # Setting the position of the y-axis labels
    plt.yaxis.set_label_coords(-0.12, 0.5)
    #plt.xaxis.set_label_coords(-0.06, 0.5)

    # Setting the x-axis labels font size

    # Setting the y-axis limits
    plt.set_ylim([0,1.25])#throughput
    plt.set_xlim([-1,len(tput_flow_1)+1])#fairness

    # Saving file
    fig.savefig(f"tput_time.pdf", bbox_inches='tight')

def main():
    plot_timing()

if __name__ == '__main__':
    main()
    

