import os
import qianfan

# 配置AK/SK
os.environ["QIANFAN_AK"] = os.environ.get("AK", "")
os.environ["QIANFAN_SK"] = os.environ.get("SK", "")

chat_comp = qianfan.ChatCompletion(model="ERNIE-Bot")


def erine(message):
    resp = chat_comp.do(messages=[{
        "role": "user",
        "content": message
    }], top_p=0.8, temperature=0.9, penalty_score=1.0)
    return resp["result"]
