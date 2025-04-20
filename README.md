# system_monitor
Simple System Monitor Tool for Windows/Linux --/系统资源巡检工具

## 🚀 功能特色

- ✅ 实时检测 CPU、内存、磁盘使用率
- ✅ 超过阈值自动提示
- ✅ 所有检测结果记录到日志文件（含时间戳）
- ✅ 支持自定义：循环次数、检测间隔、报警阈值

---

## 📸 使用效果

![image](https://github.com/user-attachments/assets/df77d987-39a7-4418-af76-f0d59dafbd93)


日志输出（`monitor_log.txt`）示例：

[2025-04-20 14:30:01] ✅ CPU 正常：24.5% [2025-04-20 14:30:01] ⚠️ 内存使用率过高：82.3%（阈值：80%） [2025-04-20 14:30:01] ✅ 磁盘正常：47.2%

## ⚙️ 使用方法
### 安装依赖
pip install psutil

运行项目
python monitor.py

修改参数（可选）
你可以在 monitor.py 中修改以下参数：
run_monitor(times=10, interval=5, cpu_th=50, mem_th=60, disk_th=70)

📂 项目结构
system_monitor/
├── monitor.py          # 主程序
├── utils.py            # 监控逻辑模块
└── monitor_log.txt     # 自动生成的日志文件

🧠 技术栈
Python 3.x
psutil
时间戳 / 文件处理 / 日志系统

🧳 适用场景
运维自动巡检脚本
轻量级监控工具
Python 项目实践作品集
Upwork / Freelancer 投标展示项目
