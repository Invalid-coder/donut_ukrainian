import json
import torch
import shutil
import argparse
from PIL import Image
from donut import DonutModel


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test fine-tuned donut')
    parser.add_argument("--model_path", help="Path to the model directory")
    parser.add_argument("--image_path", help="Path to the test image")
    parser.add_argument("--jsonl_path", help="Path to the test jsonl")
    parser.add_argument("--image_index", help="Image index in the jsonl list")
    args = parser.parse_args()
    model_path = args.model_path
    image_path = args.image_path
    jsonl_path = args.jsonl_path
    image_index = args.image_index
    my_model = DonutModel.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")
    my_model = DonutModel.from_pretrained(model_path).half().to(torch.device("cuda")).eval()
    image = Image.open(image_path).convert("RGB")
    img = image.resize((round(image.size[0]/3), round(image.size[1]/3)))
    img.show() 

    donut_result = my_model.inference(image=image, prompt="<s_ubiai-donut>")

    print("\nFine-tuned DonUT annotation results:\n")
    print(donut_result)
    # Compare annotation results (printed just above) of the DonUT model that we have fine tuned on our data, with the ground truth
    print("Ground truth:\n")

    with open(jsonl_path) as f:
        data = [json.loads(line) for line in f]
        print(json.dumps(data[int(image_index)], indent=4, ensure_ascii=False))