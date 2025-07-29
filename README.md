# test1# FastAPI + Stable Diffusion 演示项目

这是一个结合FastAPI和Stable Diffusion的简单演示项目，用于面试展示。通过这个API可以生成文本描述的图像。

## 功能特点
- FastAPI后端服务
- Stable Diffusion图像生成
- 简单的API接口设计
- 交互式API文档

## 安装与运行

### 前置要求
- Python 3.8+ 
- 至少8GB内存（推荐16GB+）
- （可选）NVIDIA GPU与CUDA（可大幅提高生成速度）

### 1. 克隆项目
```bash
git clone <你的GitHub仓库链接>
cd <项目文件夹>
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 启动服务
```bash
python main.py
```

### 4. 使用API
打开浏览器访问: http://localhost:8000/docs

在交互式文档中找到 `/text-to-image` 端点，点击"Try it out"，输入提示词（例如："a beautiful sunset over the mountains"），然后点击"Execute"。

## API端点说明
- GET `/`: 项目介绍和端点列表
- POST `/text-to-image`: 文本生成图像API
  - 请求体: {"prompt": "你的文本描述", "num_inference_steps": 20, "guidance_scale": 7.5}
  - 返回: 生成的PNG图像
## 实例展示
a beautiful sunset over the mountains
<img width="793" height="758" alt="image" src="https://github.com/user-attachments/assets/e8a55ee8-fad5-49ac-b8f6-4d7fb88f1ff0" />


## 注意事项
- 首次运行时会自动下载Stable Diffusion模型（约4GB），需要联网
- 图像生成可能需要几秒到几分钟，取决于硬件配置
- 没有GPU时会使用CPU运行，速度较慢

## 网络要求
- 首次运行需要联网下载Stable Diffusion模型(约4GB)
- 如果遇到网络连接问题，可以手动下载模型并放在项目根目录

## 常见问题解决
### 模型下载失败
1. 检查网络连接
2. 手动下载模型并放在项目根目录: https://huggingface.co/runwayml/stable-diffusion-v1-5
3. 确保文件夹名称为: stable-diffusion-v1-5

### 模块安装问题
如果提示缺少模块，请运行:
```bash
pip install -r requirements.txt --no-cache-dir --index-url https://pypi.org/simple/
```
