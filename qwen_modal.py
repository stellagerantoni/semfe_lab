import modal

app = modal.App("qwen-image")

image = (
    modal.Image.debian_slim()
    .pip_install(
        "torch",
        "diffusers",
        "transformers",
        "accelerate",
        "safetensors",
        "pillow"
    )
)

@app.function(
    gpu="H200",
    image=image,
    timeout=600
)
def run_qwen(prompt: str = "", rank: int = 128, steps: int = 8):
    import math
    import torch
    from diffusers import QwenImagePipeline

    print(f"Running on GPU: {torch.cuda.get_device_name(0)}")


    pipe = QwenImagePipeline.from_pretrained(
        "Qwen/Qwen-Image",
        torch_dtype=torch.float16
    ).to("cuda")

    pipe.enable_model_cpu_offload()  # 🔥 huge memory saver
    pipe.enable_attention_slicing()

    if prompt == "":
        prompt = "A futuristic bookstore, ultra detailed, cinematic"

    image = pipe(
        prompt=prompt,
        width=512,  # ⬅️ reduce from 1024
        height=512,
        num_inference_steps=8
    ).images[0]

    image.save("/tmp/output.png")

    return "/tmp/output.png"


@app.local_entrypoint()
def main():
    path = run_qwen.remote()
    print("Saved at:", path)