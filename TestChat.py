import qianfan
# 这个是用来测试是否能够正常的发送接收消息的

# 创建一个任务对象
qianfan.get_config().AK = "ak"
qianfan.get_config().SK = "sk"

# 创建一个任务对象
chat_comp = qianfan.ChatCompletion()

# 指定特定模型发送消息
resp = chat_comp.do(model="ERNIE-Bot", messages=[{
    "role": "user",
    "content": "你干啥呢"
}])

print(resp["result"])