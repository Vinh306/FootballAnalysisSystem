from ultralytics import YOLO

# Khởi tạo mô hình (đảm bảo đường dẫn này đúng với nơi bạn lưu file .pt)
model = YOLO("pitch_detector/yolo-football-pitch-detection.pt")

results = model.predict(source="input_video/video.mp4", save=True)

print("Đã xử lý xong! Video kết quả được lưu trong thư mục: runs/detect/predict")