from utlis import check_cpu,check_memory,check_disk
import time


def run_monitor(times=5,interval=5,cpu_th=80,mem_th=80,disk_th=85):
    print(f"系统监控启动，总控检测{times}次，每{interval}s 检测一次")
    for i in range(times):
        print(f"\n第{i+1}次巡检：")
        check_cpu(cpu_th)
        check_memory(mem_th)
        check_disk(disk_th)
        time.sleep(interval)
if __name__ =="__main__":
    run_monitor(times=10, interval=5,cpu_th=80,mem_th=80,disk_th=80)
