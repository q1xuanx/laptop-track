import psutil as ps
import plotext as plt 
import time

cpu_history = []
cpu_freq = []
mem_track = []

label_cpu = ["user", "system", "idle", "interrupt", "dpc"]
label_freq = ["current", "min", "max"]
label_mem = ["free", "used", "percent"]

def track():  

    while(True):
        cpu_times = ps.cpu_times()
        cpu_history.append(round(cpu_times.user / 3600, 2))
        cpu_history.append(round(cpu_times.system / 3600, 2))
        cpu_history.append(round(cpu_times.idle / 3600, 2))
        cpu_history.append(round(cpu_times.interrupt / 3600, 2))
        cpu_history.append(round(cpu_times.dpc / 3600, 2))
        
        load = ps.cpu_freq()

        cpu_freq.append(load.current)
        cpu_freq.append(load.min)
        cpu_freq.append(load.max)

        mem = ps.virtual_memory()
        mem_track.append(mem.free)
        mem_track.append(mem.used)
        mem_track.append(mem.percent)
        
        cpu_count = ps.cpu_count()


        plt.clt()
        
        plt.simple_bar(label_cpu, cpu_history, width=100, title="CPU Used")
        plt.show()

        plt.simple_bar(label_freq, cpu_freq, width=100, title="CPU Frequency")
        plt.show()

        plt.simple_bar(label_mem, mem_track, width=100, title="Mem used")
        plt.show()
        time.sleep(3)



def main(): 
    track()
          
if __name__ == "__main__": 
    main()