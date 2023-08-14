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

    N = 480
    Runs = 10
    tput_flow_1 = np.zeros(N)
    tput_flow_2 = np.zeros(N)
    tput_flow_3 = np.zeros(N)
    tput_flow_4 = np.zeros(N)
    tput_flow_5 = np.zeros(N)
    tput_flow_6 = np.zeros(N)
    
    for i in range(1, Runs + 1):
        tmp1 = extract_iperf_timing(f'json_files/h1_cubic_out_{i}.json')
        tmp2 = extract_iperf_timing(f'json_files/h2_bbr_out_{i}.json')
        tmp3 = extract_iperf_timing(f'json_files/h3_bbr_out_{i}.json')
        tmp4 = extract_iperf_timing(f'json_files/h4_bbr_out_{i}.json')
        tmp5 = extract_iperf_timing(f'json_files/h5_bbr_out_{i}.json')
        tmp6 = extract_iperf_timing(f'json_files/h6_bbr_out_{i}.json')

        start = 0
        for j in range(start, N):
            tput_flow_1[j] += tmp1[j]/Runs

        start += 60
        for j in range(start, N):
            tput_flow_2[j] += tmp2[j - start]/Runs

        start += 60
        for j in range(start, N):
            tput_flow_3[j] += tmp3[j - start]/Runs
        
        start += 60
        for j in range(start, N):
            tput_flow_4[j] += tmp4[j - start]/Runs
        
        start += 60
        for j in range(start, N):
            tput_flow_5[j] += tmp5[j - start]/Runs
        
        start += 60
        for j in range(start, N):
            tput_flow_6[j] += tmp6[j - start]/Runs

    
    fairness = [0 for i in range(len(tput_flow_1))] 
    t = range(0,len(tput_flow_1))
    for i in range(0, 60):
        fairness[i] += 100*(tput_flow_1[i])**2 / (1 * (tput_flow_1[i]**2 )   )
        
    for i in range(60, 120):
        fairness[i] += 100*(tput_flow_1[i]  + tput_flow_2[i] )**2 / (2 * (tput_flow_1[i]**2 + tput_flow_2[i]**2))

    for i in range(120, 180):
        fairness[i] += 100*(tput_flow_1[i]  + tput_flow_2[i] + tput_flow_3[i])**2 / (3 * (tput_flow_1[i]**2 + tput_flow_2[i]**2 + 
                                                                                          tput_flow_3[i]**2))    
    for i in range(180, 240):
        fairness[i] += 100*(tput_flow_1[i]  + tput_flow_2[i] + 
                            tput_flow_3[i] + tput_flow_4[i])**2 / (4 * (tput_flow_1[i]**2 + tput_flow_2[i]**2 + 
                                                                        tput_flow_3[i]**2+ tput_flow_4[i]**2))    
    for i in range(240, 300):
        fairness[i] += 100*(tput_flow_1[i]  + tput_flow_2[i] + 
                            tput_flow_3[i] + tput_flow_4[i] +
                            tput_flow_5[i])**2 / (5 * (tput_flow_1[i]**2 + tput_flow_2[i]**2 + 
                                                       tput_flow_3[i]**2 + tput_flow_4[i]**2 + 
                                                       tput_flow_5[i]**2))       
    for i in range(300, 480):
        fairness[i] += 100*(tput_flow_1[i]  + tput_flow_2[i] 
                          + tput_flow_3[i]  + tput_flow_4[i] 
                          + tput_flow_5[i]  + tput_flow_6[i])**2 / (6 * (tput_flow_1[i]**2 + tput_flow_2[i]**2+
                                                                         tput_flow_3[i]**2 + tput_flow_4[i]**2+
                                                                         tput_flow_5[i]**2 + tput_flow_6[i]**2))
  

    fig, plt = plt.subplots(2, 1, sharex=True,figsize=(10,11))
    fig.subplots_adjust(hspace=0.1)
    # Plot grids
    plt[0].grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
    plt[1].grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
    
    # Colors
    #Gold: #E5B245
    #Blue: #2D72B7 
    #Green: #82AA45
    #Garnet: #95253B
    #Orange: #FFA500
    #Violet: #7F00FF
    #Light blue: #ADD8E6

    t = range(0, len(tput_flow_1) )
    #print(len(tput_flow_2))
    
    #Plotting the metrics as a time's function
    plt[0].plot(t, fairness,'#E5B245', linewidth=2, label='Fairness')
    plt[1].plot(t, tput_flow_1, '#2D72B7', linewidth=2, label='CUBIC flow') 
    plt[1].plot(t, tput_flow_2, '#ADD8E6', linewidth=2, label='BBRv3 flow 1') 
    plt[1].plot(t, tput_flow_3, '#95253B', linewidth=2, label='BBRv3 flow 2') 
    plt[1].plot(t, tput_flow_4, '#FFA500', linewidth=2, label='BBRv3 flow 3') 
    plt[1].plot(t, tput_flow_5, '#82AA45', linewidth=2, label='BBRv3 flow 4') 
    plt[1].plot(t, tput_flow_6, '#7F00FF', linewidth=2, label='BBRv3 flow 5') 
    
    # Setting the y-axis labels and the x-axis label
    plt[0].set_ylabel('Fairness [%]', fontsize=f_size)
    plt[1].set_ylabel('Throughput [Gbps]', fontsize=f_size)
    plt[1].set_xlabel('Time [seconds]', fontsize=f_size)

    # Plot legends
    plt[1].legend(loc="upper right", ncol=2, fontsize=21)

    # Setting the position of the y-axis labels
    plt[1].yaxis.set_label_coords(-0.12, 0.5)
    #plt.xaxis.set_label_coords(-0.06, 0.5)


    # Setting the y-axis limits
    plt[0].set_ylim([50,105])#throughput
    plt[1].set_ylim([0,1.25])#throughput
    plt[1].set_xlim([-1,len(tput_flow_1)+1])#fairness

    # Saving file
    fig.savefig(f"fainess_time.pdf", bbox_inches='tight')

def main():
    plot_timing()

if __name__ == '__main__':
    main()
    

