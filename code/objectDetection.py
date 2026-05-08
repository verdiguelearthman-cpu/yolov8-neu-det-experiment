from ultralytics import YOLO

#model = YOLO('yolov8.yaml')

# 加载预训练YOLO模型（推荐用于训练）
model = YOLO('yolov8n.pt')

# 使用neu.yaml数据集训练模型30个周期
results = model.train(data='./neu.yaml', epochs=30, workers=0)

# 评估模型在验证集上的性能
results = model.val()

# 使用模型对图片进行目标检测
#results = model('https://ultralytics.com/images/bus.jpg')
