from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import io
from diffusers import StableDiffusionPipeline
import torch
import os
app = FastAPI(title="FastAPI + Stable Diffusion 演示", version="1.0")

# 加载Stable Diffusion模型
try:
    # 尝试使用较小的模型以减少下载大小
    model_name = "runwayml/stable-diffusion-v1-5"
    
    # 添加离线加载支持
    if os.path.exists("./stable-diffusion-v1-5"):
        print("使用本地模型...")
        pipe = StableDiffusionPipeline.from_pretrained("./stable-diffusion-v1-5", torch_dtype=torch.float16)
    else:
        print("从Hugging Face Hub下载模型...")
        pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
        # 保存模型到本地供后续使用
        pipe.save_pretrained("./stable-diffusion-v1-5")
        
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    pipe.enable_attention_slicing()
except Exception as e:
    print(f"模型加载失败: {e}")
    print("请手动下载模型并放在项目根目录下的stable-diffusion-v1-5文件夹中")
    print("模型下载地址: https://huggingface.co/runwayml/stable-diffusion-v1-5")
    print("请确保已安装所有依赖并拥有足够的内存")

# 请求体模型
class TextToImageRequest(BaseModel):
    prompt: str
    num_inference_steps: int = 20
    guidance_scale: float = 7.5

# 根路由\@app.get("/")
def read_root():
    return {
        "message": "FastAPI + Stable Diffusion 演示项目", 
        "endpoints": [
            "/", 
            "/text-to-image (POST)"
        ],
        "说明": "这个项目展示了如何通过API调用Stable Diffusion生成图像"
    }

# 文本生成图像API\@app.post("/text-to-image")
def text_to_image(request: TextToImageRequest):
    try:
        # 使用Stable Diffusion生成图像
        image = pipe(
            prompt=request.prompt,
            num_inference_steps=request.num_inference_steps,
            guidance_scale=request.guidance_scale
        ).images[0]

        # 将图像转换为字节流
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return StreamingResponse(img_byte_arr, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"图像生成失败: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)