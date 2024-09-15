import socket
import time

# 定义目标主机和端口
target_host = "127.0.0.1"
target_port = 9997

def send_and_receive():
    try:
        # 创建UDP套接字
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 发送数据到目标地址
        client.sendto(b"AAABBBCCC", (target_host, target_port))

        # 接收最多4096字节的数据
        data, addr = client.recvfrom(4096)

        # 打印接收到的数据
        print(data.decode())

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭套接字
        client.close()

# 尝试重试机制
max_retries = 3
retry_delay = 2  # 重试间隔时间（秒）
send_delay = 5  # 每次发送后的延迟时间（秒）

# 主循环
for i in range(max_retries):
    try:
        send_and_receive()
        break  # 成功后退出循环
    except Exception as e:
        if i == max_retries - 1:
            print("所有尝试均失败")
        else:
            print(f"尝试 {i + 1} 失败，等待 {retry_delay} 秒后重试...")
            time.sleep(retry_delay)

    # 在每次发送后加入延迟
    time.sleep(send_delay)
