import os
import qianfan

# 配置AK/SK
qianfan.get_config().AK = os.environ.get("AK", "")
qianfan.get_config().AK = os.environ.get("SK", "")
model = os.environ.get("model", "ERNIE-Bot")

chat_comp = qianfan.ChatCompletion(model=model)


def erine(message):
    resp = chat_comp.do(messages=[{
        "role": "user",
        "content": message
    }], top_p=0.8, temperature=0.9, penalty_score=1.0)
    return resp["result"]
