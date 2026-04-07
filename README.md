# Multi-Process Generation Notebooks

This project contains a set of **Jupyter Notebooks** that demonstrate three simple generation processes. 

---

## 📁 Project Structure

```
.
├── text_to_image.ipynb  
├── image_text_to_image.ipynb   
├── mask.ipynb   
├── diffusion-xl.ipynb  
├── requirements.txt  
└── README.md         
```

---

## ⚙️ Requirements

Make sure you have Python **3.10+** installed.

Install dependencies with:

```bash
pip install -r requirements.txt
```

Or directly inside a notebook by running the first code block.

---

## 🚀 How to Run

1. Open Jupyter Notebook or VS Code
2. Select the correct Python environment (kernel)
3. Open any of the notebooks
4. Run the cells step-by-step from top to bottom

---

## The Generation Processes

### text_to_image

A basic text to image generation process using the diffusers 1.5 model. This is a model that most pcs will easily load and run. 

### image_text_to_image

An image and text to image generation process the same diffusers 1.5 model only a differect pipeline. 

### mask

An alternative approach to generation, using masks to guide the generation. Feel free to use masks on many more advanced models and get better results.

### diffusion-xl

A powerfull model that might not run on most pcs, but feel free to run it on a cloud cerver if that is tha cse. 


---

## Notes

* Each notebook is **independent** and can be run separately
* Make sure all required libraries are installed before running


---

## License

This project is for educational purposes. Feel free to use and modify it.

---
---
