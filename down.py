# from huggingface_hub import snapshot_download
 
# from huggingface_hub import login
 
#目前需要输入access token确认登陆
#huggingface_hub.login("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")
 
#自行选择模型，自行修改下面参数（第一步的相对地址）

#自行选择模型，自行修改下面参数（第一步的相对地址）
#model_addr = 'microsoft/phi-2'
 
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.set_default_device("cpu")

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

model.save_pretrained("./md")
tokenizer.save_pretrained("./md")
