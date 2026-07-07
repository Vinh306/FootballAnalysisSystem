import urllib.request

url = "https://huggingface.co/martinjolif/yolo-football-pitch-detection/resolve/main/yolo-football-pitch-detection.pt"
save_path = "pitch_detector/yolo-football-pitch-detection.pt" 

print("Đang tải mô hình...")
urllib.request.urlretrieve(url, save_path)
print(f"Tải xong! Đã lưu tại: {save_path}")

