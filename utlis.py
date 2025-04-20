import psutil
from datetime import datetime
 
def log_msg(msg):
    now =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{now},{msg}"
    print(log)
    with open ("monitor_log.txt","a" ,encoding="utf-8") as f:
        f.write(log + "\n")

def check_cpu(threshold=80):
    usage=psutil.cpu_percent(interval=1)
    if usage > threshold:
       log_msg(f"cpu使用率过高：{usage}%(阈值：{threshold}%)")
    else:
        log_msg(f"cpu正常：{usage}%") 

def check_memory(threshold=80):
    usage = psutil.virtual_memory().percent
    if usage > threshold:
        log_msg(f"内存使用率过高：{usage}%(阈值：{threshold}%)")
    else:
        log_msg(f"内存使用正常：{usage}%")

def check_disk(threshold=90):
    usage =psutil.disk_usage("/").percent
    if usage > threshold:
        log_msg(f"磁盘使用率过高：{usage}%(阈值：{threshold})")
    else:
        log_msg(f"磁盘使用正常：{usage}%")  
          