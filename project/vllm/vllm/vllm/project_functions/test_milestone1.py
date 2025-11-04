import os
os.environ["VLLM_ATTENTION_BACKEND"] = "NO_ATTENTION"
import sys
import torch
print("torch ok:", torch.__version__)
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from vllm.engine.arg_utils import EngineArgs
from vllm.engine.llm_engine import LLMEngine
from vllm.sampling_params import SamplingParams
from vllm.project_functions.simulator import Simulator

# 1. 建立 LLMEngine（保持原本設定即可）
engine_args = EngineArgs(
    model="facebook/opt-125m",
    trust_remote_code=True,
    device="cpu",          # 明確指定使用 CPU
    disable_async_output_proc=True,  # mac/CPU 不支援 async，關掉避免 NotImplementedError
    worker_cls="vllm.worker.cpu_worker.CPUWorker",
)
engine = LLMEngine.from_engine_args(engine_args)

# 2. 啟用 dummy 模式
engine.enable_dummy_inference(Simulator())
 
# 3. 送一個 request，prompt 用你在 Simulator 裡定義過的字串
sampling_params = SamplingParams(max_tokens=32)
request_id = "req-1"
engine.add_request(request_id, prompt="你好", params=sampling_params)

# 4. 正常呼叫 step()，看回傳是不是 Simulator.generate 的結果
while True:
    outputs = engine.step()
    for output in outputs:
        print(f"request={output.request_id}, text={output.outputs[0].text!r}")
        if output.finished:
            break
    if not engine.has_unfinished_requests():
        break

engine.disable_dummy_inference()
