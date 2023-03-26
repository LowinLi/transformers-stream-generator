# transformers-stream-generator

### Description
This is a text generation method which returns a generator, streaming out each token in real-time during inference, based on Huggingface/Transformers. 

### Web Demo
+ original
![](./pic/original.gif)
+ stream
![](./pic/stream.gif)

### Installation
```bash
pip install transformers-stream-generator
```

### Usage
+ just add two lines of code before your original code
```python
from transformers_stream_generator import init_stream_support
init_stream_support()
```

### Example
+ run python script [example](./example/run.py) by gpt2
+ run web [example](./example/run_web.py)  by gpt2 and test in client [example](./example/test_client.py)