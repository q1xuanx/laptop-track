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
        cpu_history = [
            round(cpu_times.user / 3600, 2),
            round(cpu_times.system / 3600, 2),
            round(cpu_times.idle / 3600, 2),
            round(cpu_times.interrupt / 3600, 2),
            round(cpu_times.dpc / 3600, 2),
        ]

        # CPU frequency
        load = ps.cpu_freq()
        cpu_freq = [
            round(load.current, 2),
            round(load.min, 2),
            round(load.max, 2),
        ]

        # RAM usage
        mem = ps.virtual_memory()
        mem_track = [
            round(mem.free / 1e9, 2),
            round(mem.used / 1e9, 2),
            round(mem.percent, 2),
        ]
        
        plt.clt()
        
        plt.simple_bar(label_cpu, cpu_history, width=100, title="CPU Used")
        plt.show()

        plt.simple_bar(label_freq, cpu_freq, width=100, title="CPU Frequency")
        plt.show()

        plt.simple_bar(label_mem, mem_track, width=100, title="Mem used")
        plt.show()

        time.sleep(1)

        cpu_history.clear()
        cpu_freq.clear()
        mem_track.clear()



def main(): 
    track()
          
if __name__ == "__main__": 
    main()