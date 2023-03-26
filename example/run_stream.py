from transformers_stream_generator import init_stream_support
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

init_stream_support()
model = AutoModelForCausalLM.from_pretrained(
    "gpt2"
)

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = model.eval()
prompt_text = "hello? How can I help you?\n"
input_ids = tokenizer(
    prompt_text, return_tensors="pt", add_special_tokens=False
).input_ids

with torch.no_grad():
    result = model.generate(
        input_ids,
        max_new_tokens=20,
        do_sample=True,
        top_k=30,
        top_p=0.85,
        temperature=0.35,
        repetition_penalty=1.2,
        early_stopping=True,
        seed=0,
    )
    print("the original generate output:\n###\n")
    print(tokenizer.decode(result[0], skip_special_tokens=True))
    print("###\n")
    generator = model.generate(
        input_ids,
        max_new_tokens=20,
        do_sample=True,
        top_k=30,
        top_p=0.85,
        temperature=0.35,
        repetition_penalty=1.2,
        early_stopping=True,
        seed=0,
        do_stream=True,
    )
    stream_result = ""
    print("real-time stream chunk  generate output:\n###\n")
    for index, x in enumerate(generator):
        chunk = tokenizer.decode(x, skip_special_tokens=True)
        stream_result += chunk
        print(f"chunk index: {index}: {chunk}")
    print("###\n")
    print("the stream cumulate generate output:\n###\n")
    print(stream_result)
    print("###\n")