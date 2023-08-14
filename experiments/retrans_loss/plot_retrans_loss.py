import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

def extract_retrans(filename):
    
    f = open(filename)
    data = json.loads(open(filename).read())

    #throughput = data['end']['sum_sent']['bits_per_second']/1e9
    retrans = data['end']['sum_sent']['retransmits']
    return retrans 
    #return throughput
def extract_throughput(filename):
    
    f = open(filename)
    data = json.loads(open(filename).read())

    throughput = data['end']['sum_sent']['bits_per_second']/1e9
    
    return throughput


def plot_retrans():
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}
    global plt, np
    f_size = 26
    matplotlib.rc('font', **font)
    fig, plt = plt.subplots(1, 1, sharex=True,figsize=(10.5,6.75))
    fig.subplots_adjust(hspace=0.1)

    loss = [0.001, 0.01, 0.1, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]# 
    #delay = [10e-3, 20e-3, 30e-3, 40e-3, 50e-3, 60e-3, 70e-3, 80e-3, 90e-3, 100e-3]
    delay = [20e-3]

    rows = len(loss)
    cols = len(delay)
    results = np.zeros((rows, cols))
    t = range(0, len(loss))
    i = 0
    
    for l in loss:
        j = 0
        for d in delay:
            results[i][j] = extract_retrans(f'json_files/h1_bbr_{d}_{l}out.json')
            j += 1
        i += 1
    #print(results)
    results_trans = results.transpose()
    ##########################Plotting###########################
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
    plt.loglog(loss, results_trans[0], '#E5B245', linewidth=2, marker ='o')  #label='Fairness', label='loss= 0.001%',
    #plt.plot(t, cubic, '#2D72B7', linewidth=2, label='CUBIC')  #label='Fairness', marker ='o'
    #plt.plot(t, bbr3,  '#95253B', linewidth=2, label='BBRv3')  #label='Fairness', marker ='o'
    
    #Setting the y-axis labels and the x-axis label
    plt.set_ylabel('Retansmissions [Packets]', fontsize=f_size)
    plt.set_xlabel('Loss rate [%]', fontsize=f_size)

    #Plot legends
    #plt.legend(loc="lower right", fontsize=f_size)
    #plt.legend(loc="upper right", ncol=1, fontsize=21)

    #Setting the position of the y-axis labels
    #plt.yaxis.set_label_coords(-0.11, 0.5)
    #plt.yaxis.set_label_coords(-0.09, 0.5)

   # custom_x_labels = ['0.001', '0.01', '0.1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20']
    #
    #plt.set_xticks(loss)
    #plt.set_xticklabels(custom_x_labels)
    #Setting the x-axis labels font size
    #plt.tick_params(axis='y', labelsize=f_size)
    #plt.tick_params(axis='y', labelsize=f_size)
    #plt.tick_params(axis='x', labelsize=f_size)

    #Setting the y-axis limits
    plt.set_ylim([50, 1.5e5])#throughput
    #plt.set_xlim([0,duration])#fairness


    fig.savefig("retrans_delay_loss.pdf", bbox_inches='tight')

def plot_throughput():
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}
    global plt, np
    f_size = 26
    matplotlib.rc('font', **font)
    fig, plt = plt.subplots(1, 1, sharex=True,figsize=(10.5,6.75))
    fig.subplots_adjust(hspace=0.1)

    loss = [0.001, 0.01, 0.1, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]# 
    #delay = [10e-3, 20e-3, 30e-3, 40e-3, 50e-3, 60e-3, 70e-3, 80e-3, 90e-3, 100e-3]
    delay = [20e-3]

    rows = len(loss)
    cols = len(delay)
    results = np.zeros((rows, cols))
    t = range(0, len(loss))
    i = 0
    
    for l in loss:
        j = 0
        for d in delay:
            results[i][j] = extract_throughput(f'json_files/h1_bbr_{d}_{l}out.json')
            j += 1
        i += 1
    #print(results)
    results_trans = results.transpose()
    ##########################Plotting###########################
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
    plt.semilogx(loss, results_trans[0], '#E5B245', linewidth=2, marker ='o')  #label='Fairness', label='loss= 0.001%',
    #plt.plot(t, cubic, '#2D72B7', linewidth=2, label='CUBIC')  #label='Fairness', marker ='o'
    #plt.plot(t, bbr3,  '#95253B', linewidth=2, label='BBRv3')  #label='Fairness', marker ='o'
    
    #Setting the y-axis labels and the x-axis label
    plt.set_ylabel('Throughput [Gbps]', fontsize=f_size)
    plt.set_xlabel('Loss rate [%]', fontsize=f_size)

    #Plot legends
    #plt.legend(loc="lower right", fontsize=f_size)
    #plt.legend(loc="upper right", ncol=1, fontsize=21)

    #Setting the position of the y-axis labels
    #plt.yaxis.set_label_coords(-0.11, 0.5)
    #plt.yaxis.set_label_coords(-0.09, 0.5)

   # custom_x_labels = ['0.001', '0.01', '0.1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20']
    #
    #plt.set_xticks(loss)
    #plt.set_xticklabels(custom_x_labels)
    #Setting the x-axis labels font size
    #plt.tick_params(axis='y', labelsize=f_size)
    #plt.tick_params(axis='y', labelsize=f_size)
    #plt.tick_params(axis='x', labelsize=f_size)

    #Setting the y-axis limits
    plt.set_ylim([-0.05, 1.1])#throughput
    #plt.set_xlim([0,duration])#fairness


    fig.savefig("throughput_delay_loss.pdf", bbox_inches='tight')

def main():
    #plot_retrans()
    plot_throughput()
if __name__ == '__main__':
    main()
    

