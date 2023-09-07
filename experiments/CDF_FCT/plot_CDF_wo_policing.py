import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def calculate_CDF(filename):
    p4bs = []
    i=0
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            i+=1
            if (i < 10):
                continue
            p4bs.append(abs(float(row[6]) - float(row[5])))

    p4bs = np.sort(p4bs)
    freq_1 = np.zeros(len(p4bs))
    freq_1[0] = 1/len(p4bs)
    for i in range(1,len(p4bs)):
        freq_1[i] = freq_1[i-1] + 1/len(p4bs)
    freqs_len = []
    freqs_len.append(len(freq_1))
    freqs = []
    freqs.append(freq_1)
    #freqs.append(freq_2)
    freq = np.argmin(freqs_len)
    freq = freqs[freq]
    
    standard_deviation = np.std(p4bs)
    stdev_1 = "{:.2f}".format(standard_deviation)
    print("Standard Deviation:", stdev_1)
    mean_value = np.mean(p4bs)
    mean_1 = "{:.2f}".format(mean_value)
    print("Mean Value:", mean_1)
    return freq, p4bs, mean_1, stdev_1

def main():
    freq1, cubic, mean_1, stdev_1 = calculate_CDF("cubic_01BDP.csv")
    freq2, bbr, mean_2, stdev_2 = calculate_CDF("bbr_01BDP.csv")

    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 30}
    f_size = 30
    matplotlib.rc('font', **font)

    #Red: #95253B
    #Blue: #2D72B7
    fig = plt.figure()
    plt.figure(figsize=(9.8, 9))
    plt.plot(cubic[0:len(freq1)], freq1, c='#2D72B7', label=f'CUBIC\n \u03BC = {mean_1}\n \u03C3 = {stdev_1}')
    plt.plot(bbr[0:len(freq2)], freq2, c='#95253B', label=f'BBRv3\n \u03BC = {mean_2}\n \u03C3 = {stdev_2}')
    #plt.plot(stanford[0:len(freq)], freq, c='#77ac30', label='Without a large flow')
    plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')
    plt.legend(loc='lower right')
    plt.xlabel('Flow completion time [s]')
    plt.ylabel('CDF')    
    plt.xlim(-0.1,5)
    #plt.title('N = 1000')

    #plt.legend()
    plt.savefig('FCT_01BDP.pdf')
    plt.show()


if __name__ == '__main__':
    main()