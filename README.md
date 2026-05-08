# YOLOv8 NEU-DET 钢材表面缺陷检测实验

## 课程信息
- 课程：人工智能导论
- 实验截止日期：2026年5月10日
- 任务：使用YOLOv8对NEU-DET数据集进行目标检测训练

## 实验结果

| 指标 | 数值 |
|------|------|
| mAP50 | 0.820 |
| mAP50-95 | 0.516 |
| Precision | 0.682 |
| Recall | 0.804 |
| 训练时长 | ~15分钟 (30 epochs) |
| 推理速度 | ~2.1ms/张 (476 FPS) |

## 数据集
- NEU-DET（东北大学钢材表面缺陷数据集）
- 6个类别：crazing, inclusion, patches, pitted_surface, rolled-in_scale, scratches
- 1770张训练图片 + 30张验证图片，YOLO格式标注

## 环境配置
- Python 3.9 (Anaconda)
- PyTorch 2.5.1+cu121
- Ultralytics 8.4.47
- GPU: NVIDIA GeForce RTX 4060 Laptop (8GB)
- CUDA Version: 12.7 (PyTorch cu121)
- OS: Windows 11

## 项目结构
```
├── code/
│   ├── objectDetection.py      # 训练脚本
│   └── neu.yaml                # 数据集配置
├── results/                    # 训练输出结果
│   ├── results.csv             # 逐epoch指标
│   ├── results.png             # 训练曲线图
│   ├── confusion_matrix.png    # 混淆矩阵
│   ├── val_batch0_pred.jpg     # 验证集预测结果
│   ├── labels.jpg              # 标签分布
│   └── weights/                # 模型权重
│       ├── best.pt
│       └── last.pt
├── YOLO实验报告.docx            # 实验报告
├── SESSION_MEMORY.md           # 实验过程记录
└── README.md
```
