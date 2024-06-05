from huggingface_hub import snapshot_download
 
from huggingface_hub import login
 
#目前需要输入access token确认登陆
huggingface_hub.login("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")
 
#自行选择模型，自行修改下面参数（第一步的相对地址）

#自行选择模型，自行修改下面参数（第一步的相对地址）
model_addr = 'microsoft/phi-2'
 
#提取模型库名和模型名称
model_repo = model_addr.split('/')[0]
model_name = model_addr.split('/')[1]
 
# 下载模型
snapshot_download(
repo_id=f"{model_addr}",
 
#去除tensorflow的模型，只下载pytorch模型
ignore_patterns=["*.h5", "*.ot", "*.msgpack"],
 
#模型存储地址
local_dir=f"md/",
)
