from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers_stream_generator import init_stream_support
import torch
import random
from typing import Dict


init_stream_support()
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = model.eval()


class CompletionsRequest(BaseModel):
    prompt: str = Field(title="input prompt")
    parameters: Dict = Field(title="runtime parameters")


app = FastAPI(
    title="Stream Restful Demo",
    redoc_url=None,
    docs=None,
)


@app.post(
    "/inference_stream",
)
def inference_stream(request: CompletionsRequest):
    with torch.no_grad():
        input_ids = tokenizer(request.prompt, return_tensors="pt").input_ids
        pars = request.parameters
        generator = model.generate(
            input_ids,
            max_new_tokens=pars.get("max_tokens") or 200,
            do_sample=True,
            do_stream=True,
            top_k=pars.get("top_k") or 30,
            top_p=pars.get("top_p") or 0.85,
            temperature=pars.get("temperature") or 0.35,
            repetition_penalty=pars.get("repetition_penalty") or 1.2,
            early_stopping=True,
            seed=0,
        )

        def _decode_generator(generator):
            words = ""
            last_tokens = []
            last_decoded_tokens = []
            for x in generator:
                tokens = x.cpu().numpy().tolist()
                tokens = last_tokens + tokens
                word = tokenizer.decode(tokens, skip_special_tokens=True)
                if "�" in word:
                    last_tokens = tokens
                else:
                    if " " in tokenizer.decode(
                        last_decoded_tokens + tokens, skip_special_tokens=True
                    ):
                        word = " " + word
                    last_tokens = []
                    last_decoded_tokens = tokens
                    yield json.dumps(
                        {
                            "code": 200,
                            "message": "success",
                            "data": [
                                {
                                    "delta": {"content": word},
                                    "logprobs": None,
                                    "index": 0,
                                    "finish_reason": None,
                                }
                            ],
                        },
                        ensure_ascii=False,
                    )
                    words += word
            log.info(uid + "$$ " + words)

    return StreamingResponse(_decode_generator(generator))



@app.post(
    "/inference",
)
def inference(request: CompletionsRequest):
    with torch.no_grad():
        input_ids = tokenizer(request.prompt, return_tensors="pt").input_ids
        pars = request.parameters
        result = model.generate(
            input_ids,
            max_new_tokens=pars.get("max_tokens") or 200,
            do_sample=True,
            top_k=pars.get("top_k") or 30,
            top_p=pars.get("top_p") or 0.85,
            temperature=pars.get("temperature") or 0.35,
            repetition_penalty=pars.get("repetition_penalty") or 1.2,
            early_stopping=True,
            seed=0,
        )
        words = tokenizer.decode(result[0], skip_special_tokens=True)
        print(words)

    return {"result": words}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
