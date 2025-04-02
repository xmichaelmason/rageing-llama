import os
from dotenv import load_dotenv
import requests
import torch
from PIL import Image
from transformers import MllamaForConditionalGeneration, AutoProcessor
import urllib

load_dotenv()

#model = LlamaForCausalLM.from_pretrained("./path/to/local/directory", local_files_only=True)

def is_url_or_path(s):
    try:
        result = urllib.parse.urlparse(s)
        return bool(result.scheme)
    except ValueError:
        return False
    
def load_image(image_path):
    if is_url_or_path(image_path):
        image = Image.open(requests.get(image_path, stream=True).raw)
    else:
        image = Image.open(image_path)
    
    return image

def process_image(image_path, prompt):
        
    model_id = "meta-llama/Llama-3.2-11B-Vision-Instruct"

    model = MllamaForConditionalGeneration.from_pretrained(
        model_id,
        cache_dir=os.path.join(os.getenv("HF_HUB_CACHE")),
        torch_dtype=torch.bfloat16,
        device_map="auto",
        local_files_only=True
    )
    processor = AutoProcessor.from_pretrained(model_id)

    image = load_image(image_path)

    messages = [
        {"role": "user", "content": [
            {"type": "image"},
            {"type": "text", "text": prompt}
        ]}
    ]
    input_text = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(
        image,
        input_text,
        add_special_tokens=False,
        return_tensors="pt"
    ).to(model.device)

    output = model.generate(**inputs, max_new_tokens=512)
    return(processor.decode(output[0]))


if __name__ == "__main__":
    image_path = "images/360_F_13836944_ufHlwFTgpueUKO0x2xxmtvNRDN70sVpc.jpg"
    prompt = "Describe this image in detail"
    result = process_image(image_path, prompt)
    print(result)