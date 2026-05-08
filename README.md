# YOLOv8 NEU-DET 钢材表面缺陷检测实验

## 课程信息
- 课程：人工智能导论
- 实验截止日期：2026年5月10日
- 任务：使用YOLOv8对NEU-DET数据集进行目标检测训练

## 数据集
- NEU-DET（东北大学钢材表面缺陷数据集）
- 6个类别：crazing, inclusion, patches, pitted_surface, rolled-in_scale, scratches
- 训练集 + 验证集，YOLO格式标注

## 环境配置
- Python 3.9 (Anaconda)
- PyTorch 2.5.1+cu121
- Ultralytics 8.4.47
- GPU: NVIDIA GeForce RTX 4060 Laptop (8GB)
- CUDA Version: 12.7
- OS: Windows 11

## 项目路径（本地）
```
D:\YOLO各版本\YOLO-V8\YOLOV8\YOLOV8\ObjectDetection\
├── objectDetection.py      # 训练脚本
├── neu.yaml                # 数据集配置
├── NEU-DET/                # 数据集
│   ├── train/images/
│   ├── train/labels/
│   ├── valid/images/
│   └── valid/labels/
└── runs/detect/train/      # 训练输出结果
```
