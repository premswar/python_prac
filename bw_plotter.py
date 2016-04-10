import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerLine2D
peakbw =[]
peakbw_time =[]
avgbw =[]
avgbw_time =[]
peakbw_a =[]
peakbw_time_a =[]
avgbw_a =[]
avgbw_time_a =[]
keep_phrases = ["openflow.flow_tracker:Network peak link throughput",
                "openflow.flow_tracker:Network avg link throughput"]
peak = ["peak"]
avg  = ["avg"]
with open("pox_1.log") as f:
    f = f.readlines()
first_time = 1
for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            #important.append(line)
            p1,p2 = line.split('Time:',1);
            p2 = p2.strip()
            words = p1.strip().split();
            if words[1] ==  "peak" :
                peakbw_time.append(float(p2))
                if first_time == 1:
                    start_time = peakbw_time[0]
                    first_time = 0
                peakbw_time[-1] = peakbw_time[-1]-start_time
                peakbw.append(words[-1])
            #print(words[0])
            #print(words[1])
            #print(words[2])
            #print(words[3])
            #print(words[4])
            #print(words[5])
            if words[1] ==  "avg" :
                #words = p1.strip().split();
                avgbw_time.append(float(p2))
                avgbw_time[-1] = avgbw_time[-1]-start_time
                avgbw.append(words[-1])
            break

with open("pox_avra_1.log") as a:
    a = a.readlines()
first_time = 1
for line in a:
    for phrase in keep_phrases:
        if phrase in line:
            #important.append(line)
            p1,p2 = line.split('Time:',1);
            p2 = p2.strip()
            words = p1.strip().split();
            if words[1] ==  "peak" :
                peakbw_time_a.append(float(p2))
                if first_time == 1:
                    start_time_a = peakbw_time_a[0]
                    first_time = 0
                peakbw_time_a[-1] = peakbw_time_a[-1]- start_time_a
                peakbw_a.append(words[-1])
            #print(words[0])
            #print(words[1])
            #print(words[2])
            #print(words[3])
            #print(words[4])
            #print(words[5])
            if words[1] ==  "avg" :
                #words = p1.strip().split();
                avgbw_time_a.append(float(p2))
                avgbw_time_a[-1] = avgbw_time_a[-1]-start_time_a
                avgbw_a.append(words[-1])
            break
#print(peakbw)
#print(peakbw_a)
#print(peakbw_time_a)
#print(avgbw)
#print(avgbw_a)
plt.figure(1)
plt.subplot(211)
line1 = plt.plot(peakbw_time, peakbw, 'r-',label="Peak BW")
line2 = plt.plot(peakbw_time_a, peakbw_a, 'b-',label="Peak BW_AVRA")
#line2 = plt.plot(avgbw_time, avgbw, 'b-',label="Avg BW")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.grid(color='r', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Bandwidth (Mbps)')
plt.subplot(212)
#ine3 = plt.plot(peakbw_time_a, peakbw_a, 'r-',label="Peak BW_a")
line3 = plt.plot(avgbw_time, avgbw, 'r-',label="Avg BW")
line4 = plt.plot(avgbw_time_a, avgbw_a, 'b-',label="Avg BW_AVRA")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.grid(color='r', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Bandwidth (Mbps)')
#plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
# Create a legend for the first line.
plt.show()
#print(important)
