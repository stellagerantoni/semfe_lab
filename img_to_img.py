import torch
from PIL import Image
import requests
from io import BytesIO
from diffusers import StableDiffusionImg2ImgPipeline

# Load pipeline
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("mps")

print("pipeline loaded")

# Load image from URL
url = "https://www.eloquii.com/fleximages/57024/2731_57024_mc_2713_00.jpg"
response = requests.get(url)

init_image = Image.open(BytesIO(response.content)).convert("RGB")
init_image = init_image.resize((512, 512))

# Prompt
prompt = "change hes dress color, without changing the human at all. The human must be "

# Run img2img
image = pipe(
    prompt=prompt,
    image=init_image,
    strength=0.75,
    guidance_scale=7.5
).images[0]

image.save("output.png")