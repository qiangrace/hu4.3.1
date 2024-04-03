import requests
import time
import getopt
import sys
import re




def get_first_number(string):
    match = re.search(r'\d+', string)
    if match:
        return match.group()
    else:
        return None


downloadSpeed_good = 300
downloadSpeed_poor = 100

try:
    opts, args = getopt.getopt(sys.argv[1:], "h:g:p:", ["good=", "poor="])
except getopt.GetoptError:
    print('JS.py -g 300kbps -p 100kbps')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('JS.py -g 300kbps -p 100kbps')
        sys.exit()
    elif opt in ("-g", "--good"):
        downloadSpeed_good = int(get_first_number(arg))
    elif opt in ("-p", "--poor"):
        downloadSpeed_poor = int(get_first_number(arg))


if downloadSpeed_poor >= downloadSpeed_good:
    print("请提供正确的命令行参数！")
    sys.exit(3)




# 三个JS文件，分别对应，通话，记录，统计
JSurls = [
    'https://console.air-test.sobot.tech/agent-platform/vendors.95f055b7.async.js',
    'https://console.air-test.sobot.tech/agent-platform/records/umi.js',
    'https://console.air-test.sobot.tech/agent-platform/statistics/umi.js'
]


totaldownloadedbytes = 0
totaltime_seconds = 0
# 根据URL列表并获取每个JS的时长和字节
for url in JSurls:
    # 记录开始时间
    start_time = time.time()

    # 下载JS文件
    response = requests.get(url)
    content = response.content

    # 计算时长和字节数
    #time.time()获取的时间戳是指自1970年1月1日以来的秒数
    end_time = time.time()
    duration = end_time - start_time
    size_in_bytes = len(content)
    size_in_Mbytes = size_in_bytes / 1024 /1024

    totaldownloadedbytes += size_in_bytes
    totaltime_seconds += duration

    # 打印结果
    #print(f'start_time: {start_time}')
    #print(f'end_time: {end_time}')
    #print(f'JS: {url}')
    #print(f'加载时长: {duration} 秒')
    #print(f'字节大小: {size_in_bytes} 字节')
    #print(f'字节大小: {size_in_Mbytes} M字节')
    
    
average_download_speed = totaldownloadedbytes / totaltime_seconds / 1024
average_download_speed = round(average_download_speed, 3)
print("\n")
print(f'平均下载速度: {average_download_speed} kbps')
print("！！！！！！！！！！！！！！")  
if average_download_speed > downloadSpeed_good:
    print("网络状况良好，系统使用体验流畅！")
elif downloadSpeed_good > average_download_speed > downloadSpeed_poor:
    print("网络状况一般，系统页面刷新可能会慢！")    
elif downloadSpeed_poor > average_download_speed:
    print("网络状况差，系统页面刷新会有明显卡顿！") 












    