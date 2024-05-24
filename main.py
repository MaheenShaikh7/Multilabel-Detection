from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO('yolov8n.yaml')


def train():
  # Train the model using the 'coco128.yaml' dataset for 3 epochs
  results = model.train(data='config.yaml', epochs=1, workers=1,batch=12)


if __name__=='__main__':
  train()
