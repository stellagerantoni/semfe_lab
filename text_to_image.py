import os
import torch
from PIL import Image
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained(
	"runwayml/stable-diffusion-v1-5",
	use_auth_token=True
).to("mps")
print("pipeline loaded")

prompt = ("a cinematic portrait of a young woman standing in a rainy neon-lit street in Tokyo "
		  "at night, wet pavement reflecting colorful lights, shallow depth of field, "
		  "35mm photography, ultra detailed, soft lighting, bokeh, high contrast, "
		  "realistic skin texture, masterpiece, best quality")

image = pipe(prompt)[0][0]
import pdb; pdb.set_trace()

image.save("astronaut_rides_horse.png")