import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

def extract_iperf_summary(filename):
    
    f = open(filename)
    data = json.loads(open(filename).read())

    throughput = data['end']['sum_sent']['bits_per_second']/1e9

    return throughput

def plot_timing_flows():
    global plt, np
    
    font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 26}
    f_size = 26
    matplotlib.rc('font', **font)

    tag = ["1_1", "1_2", "1_3", "1_5", "1_10",
           "2_1", "2_2", "2_3", "2_5", "2_10",
           "3_1", "3_2", "3_3", "3_5", "3_10",
           "4_1", "4_2", "4_3", "4_5", "4_10",
           "5_1", "5_2", "5_3", "5_5", "5_10",
           "6_1", "6_2", "6_3", "6_5", "6_10",
           "7_1", "7_2", "7_3", "7_5", "7_10",
           "8_1", "8_2", "8_3", "8_5", "8_10",
           "9_1", "9_2", "9_3", "9_5", "9_10",
           "10_1", "10_2", "10_3", "10_5", "10_10"
           ]
    cubic_flows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bbr3_flows = [1, 2, 3, 5, 10]
    Runs = 10
    
    cubic1 = []
    cubic2 = []
    f1 = [0 for i in range(len(cubic_flows))] 
    f2 = [0 for i in range(len(cubic_flows))] 
    f3 = [0 for i in range(len(cubic_flows))] 
    f4 = [0 for i in range(len(cubic_flows))] 
    f5 = [0 for i in range(len(cubic_flows))] 

    for i in range(0, len(cubic_flows)): 
        f1[i]  = cubic_flows[i] + bbr3_flows[0]
        f2[i]  = cubic_flows[i] + bbr3_flows[1]
        f3[i]  = cubic_flows[i] + bbr3_flows[2]
        f4[i]  = cubic_flows[i] + bbr3_flows[3]
        f5[i]  = cubic_flows[i] + bbr3_flows[4]
    fair_share_ideal_1=100*np.divide(cubic_flows, f1)
    fair_share_ideal_2=100*np.divide(cubic_flows, f2)
    fair_share_ideal_3=100*np.divide(cubic_flows, f3)
    fair_share_ideal_4=100*np.divide(cubic_flows, f4)
    fair_share_ideal_5=100*np.divide(cubic_flows, f5)
       
    share_1 = []
    tag = "1_1" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "2_1"  
    for i in range(1, Runs + 1):
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 3
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "3_1"    
    for i in range(1, Runs + 1):
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "4_1"    
    for i in range(1, Runs + 1):     
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
   
    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        
    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "5_1"    
    for i in range(1, Runs + 1):   
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "6_1"    
    for i in range(1, Runs + 1):        
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "7_1"    
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        
    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "8_1"    
    for i in range(1, Runs + 1):          
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        
    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "9_1"    
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    cubic_tmp = 0
    bbr3_tmp = 0
    tag = "10_1"    
    for i in range(1, Runs + 1):       
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 10
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_1.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    
        ######################################### 2 BBRv3 flows################################
           
    share_2 = []
    tag = "1_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):  
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 3
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
   
    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "2_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 3
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "3_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):    
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "4_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):     
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        

    tag = "5_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):    
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        


    tag = "6_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        


    tag = "7_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):       
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        

    tag = "8_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):     
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "9_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):       
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "10_2" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):           
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 10
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_2.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


        ######################################### 3 BBRv3 flows################################
        
    share_3 = []
    tag = "1_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):       
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 3
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "2_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 3
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "3_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):          
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "4_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        

    tag = "5_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):       
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        

    tag = "6_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "7_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        

    tag = "8_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):   
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "9_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):       
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "10_3" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):        
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 10
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_3.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

 
        ######################################### 5 BBRv3 flows################################
        
    share_4 = []
    tag = "1_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):          
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 3
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "2_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):     
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 3
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "3_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):        
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "4_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):       
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
    
    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        

    tag = "5_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):        
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
    
    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "6_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):           
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "7_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):        
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        

    tag = "8_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):       
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "9_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 14
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "10_5" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):     
        flow = 1
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 10
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 14
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 15
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_4.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


        ######################################### 10 BBRv3 flows################################
    share_5 = []
    tag = "1_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 3
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    
    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "2_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):         
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 3
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 4
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 

   
    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "3_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):        
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 5
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

  
    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "4_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 6
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 10
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 14
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
 
    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "5_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):    
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 7
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 14
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 15
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "6_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):        
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 8
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 12
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 14
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 15
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 16
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))

    tag = "7_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):   
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 8
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 9
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 13
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 14
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 15
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 16
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 17
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        

    tag = "8_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):     
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 10
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  


    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))
        


    tag = "9_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):     
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 10
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 11
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 14
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 15
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 16
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')
        flow = 17
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 18
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 19
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    tag = "10_10" 
    cubic_tmp = 0
    bbr3_tmp = 0
    for i in range(1, Runs + 1):      
        flow = 1
        cubic_tmp = extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')  
        flow = 2
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 3
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 4
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 5
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 6
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 7
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 8
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 9
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json')
        flow = 10
        cubic_tmp += extract_iperf_summary(f'json_files/h{flow}_cubic_{tag}_{i}.json') 
        flow = 11
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 12
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 13
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 14
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 15
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json') 
        flow = 16
        bbr3_tmp = extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 17
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 18
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 19
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  
        flow = 20
        bbr3_tmp += extract_iperf_summary(f'json_files/h{flow}_bbr_{tag}_{i}.json')  

    cubic_tmp = cubic_tmp/10
    bbr3_tmp = bbr3_tmp/10
    share_5.append(100*cubic_tmp / (cubic_tmp + bbr3_tmp))


    
    ##########################Plotting###########################
    
    fig, plt = plt.subplots(1, 1, sharex=True,figsize=(13,8))
    fig.subplots_adjust(hspace=0.1)

    #Plot grids
    plt.grid(True, which="both", lw=0.3, linestyle=(0,(1,10)), color='black')

    #plt[1].xscale("log")

    #Colors
    #Gold: #E5B245
    #Blue: #2D72B7 
    #Green: #82AA45
    #Garnet: #95253B

    #Plotting the metrics as a time's function
    plt.plot(cubic_flows, fair_share_ideal_1,'#2D72B7',linestyle='--', linewidth=2)
    plt.plot(cubic_flows, share_1,'#2D72B7', linewidth=2, label='1')
    
    plt.plot(cubic_flows, fair_share_ideal_2,'#EE7621',linestyle='--', linewidth=2)
    plt.plot(cubic_flows, share_2,'#EE7621', linewidth=2, label='2')
    plt.plot(cubic_flows, fair_share_ideal_3,'#458B00',linestyle='--', linewidth=2)
    plt.plot(cubic_flows, share_3,'#458B00', linewidth=2, label='3')
    plt.plot(cubic_flows, fair_share_ideal_4,'#808A87',linestyle='--', linewidth=2)
    plt.plot(cubic_flows, share_4,'#808A87', linewidth=2, label='5')
    plt.plot(cubic_flows, fair_share_ideal_5,'#FFB90F',linestyle='--', linewidth=2)
    plt.plot(cubic_flows, share_5,'#FFB90F', linewidth=2, label='10')
   

    #Setting the y-axis labels and the x-axis label
    plt.set_ylabel('Total share of CUBIC flows [%]', fontsize=f_size)
    plt.set_xlabel('Number of CUBIC flows', fontsize=f_size)

    #Plot legends
    plt.legend(title="# BBRv3 flows",loc="upper right", ncol=5, fontsize=f_size)


    #Setting the position of the y-axis labels
    #plt[0].yaxis.set_label_coords(-0.12, 0.5)
    #plt[1].yaxis.set_label_coords(-0.12, 0.5)

    #Setting the x-axis labels font size
    custom_x_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    plt.set_xticks(cubic_flows)
    plt.set_xticklabels(custom_x_labels)

    #Setting the y-axis limits
    plt.set_ylim([0, 119])#fairness
    plt.set_xlim([0.75, 10.25])#throughput
   
    fig.savefig("total-share.pdf", bbox_inches='tight')
   

def main():
    plot_timing_flows()
    #plot_timing_100_flows()

if __name__ == '__main__':
    main()
    

