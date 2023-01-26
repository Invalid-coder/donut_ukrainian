# donut_ukrainian

## Step 1

Go to "/content/donut/config" folder, add a new file called "train_ubiai.yaml" and copy the following config rows in it:

resume_from_checkpoint_path: null # only used for resume_from_checkpoint option in PL
result_path: "/content/drive/MyDrive/Invoice dataset/UBIAI_dataset/processed_dataset/result"
pretrained_model_name_or_path: "naver-clova-ix/donut-base" # loading a pre-trained model (from moldehub or path)
dataset_name_or_paths: ["/content/drive/MyDrive/Invoice dataset/UBIAI_dataset/processed_dataset"] # loading datasets (from moldehub or path)
sort_json_key: False # cord dataset is preprocessed, and publicly available at https://huggingface.co/datasets/naver-clova-ix/cord-v2
train_batch_sizes: [1]
val_batch_sizes: [1]
input_size: [1280, 960] # when the input resolution differs from the pre-training setting, some weights will be newly initialized (but the model training would be okay)
max_length: 768
align_long_axis: False
num_nodes: 1
seed: 2022
lr: 3e-5
warmup_steps: 300 # 800/8*30/10, 10%
num_training_samples_per_epoch: 800
max_epochs: 50
max_steps: -1
num_workers: 8
val_check_interval: 1.0
check_val_every_n_epoch: 3
gradient_clip_val: 1.0
verbose: True

## Step 2

pip install -r requirements.txt

## Step 3

train the model
!cd donut && python train.py --config config/train_ubiai.yaml

## Step 4

Test fine-tuned donut model

python test_donut.py --model_path model_here --image_path image_here --jsonl_path jsonl_here --image_index 7

- model_path - path to the directory of fine-tuned donut model
- image_path - path to the test image
- jsonl_path - path to the jsonl file
- image_index - index of test image in jsonl file
