# Football Analysis System

## Giới thiệu
Football Analysis System là một hệ thống phân tích trận đấu bóng đá sử dụng Computer Vision và Deep Learning. Dự án thực hiện nhận diện và theo dõi chuyển động của cầu thủ, trọng tài, và quả bóng trong video trận đấu, từ đó phân tích các chỉ số như tốc độ, quãng đường di chuyển và kiểm soát bóng của từng đội.

## Các tính năng chính
- **Nhận diện và phân loại**: Nhận diện cầu thủ, trọng tài và quả bóng (Sử dụng YOLO).
- **Phân đội**: Tự động phân loại cầu thủ vào các đội khác nhau dựa trên màu áo (Clustering bằng KMeans).
- **Gán quyền kiểm soát bóng**: Xác định cầu thủ nào đang kiểm soát bóng.
- **Theo dõi đối tượng (Tracking)**: Theo dõi chuyển động của các đối tượng qua các khung hình (ByteTrack).
- **Phân tích tốc độ và khoảng cách**: Tính toán quãng đường và tốc độ của cầu thủ.
- **Biến đổi góc nhìn (View Transformation)**: Chuyển đổi tọa độ từ góc nhìn camera sang tọa độ 2D mặt phẳng sân từ trên xuống.

## Nguồn dữ liệu & Mô hình
- **Mô hình detect cầu thủ, bóng và trọng tài**: Sử dụng mạng YOLO được huấn luyện từ tập dữ liệu (dataset) chuyên về bóng đá thu thập trên [Roboflow Universe](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1) (Football Player Detection Dataset).
- **Tải mô hình (Pretrained Weights) detect các vị trí sân (Pitch Keypoints)**: Bạn có thể tải các file weights của mô hình đã được huấn luyện sẵn trực tiếp từ [Hugging Face](https://huggingface.co/martinjolif/yolo-football-pitch-detection) và đặt vào thư mục `pitch_detector/` của dự án để sử dụng.

## ⚠️ Lưu ý 
- **Đặc điểm về vận tốc và khoảng cách di chuyển của cầu thủ**: Hiện tại, tính toán vận tốc có thể **không chính xác khi camera di chuyển**. Điều này là do sự thay đổi góc quay, dịch chuyển và thu phóng (zoom) của camera ảnh hưởng đến việc tính toán khoảng cách pixel, khiến ước lượng khoảng cách vật lý và vận tốc trên sân không phản ánh đúng thực tế.

