from ultralytics import YOLO

model = YOLO("train_YOLO/runs/detect/train/weights/best.pt")

result = model.predict(source="input_video/test (24).mp4", save=True)

print(result[0])
print("------------------------------")
for box in result[0].boxes:
    print(box)