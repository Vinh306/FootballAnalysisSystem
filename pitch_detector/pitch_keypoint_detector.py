from ultralytics import YOLO
import numpy as np
from utils import PITCH_KEYPOINTS_REAL

class PitchKeypointDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        # Lưu bản đồ thực tế vào class để tiện dùng tính toán sau này
        self.pitch_template = PITCH_KEYPOINTS_REAL

    def detect_keypoints(self, frame):
        # Chạy model trên frame
        results = self.model.predict(frame, conf=0.5, verbose=False)
        
        keypoints_pixel = {}
        if len(results) > 0 and results[0].keypoints is not None:
            # Lấy tọa độ (x, y) của các keypoints
            kpts = results[0].keypoints.xy[0].cpu().numpy() 
            
            # Lưu vào dictionary: {id_điểm: [x, y]}
            for idx, pt in enumerate(kpts):
                if pt[0] > 0 and pt[1] > 0: # Chỉ lấy các điểm detect được
                    keypoints_pixel[idx] = [pt[0], pt[1]]
                    
        return keypoints_pixel

    def get_keypoints_for_video(self, frames, read_from_stub=False, stub_path=None):
        import os
        import pickle
        
        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path, 'rb') as f:
                keypoints_per_frame = pickle.load(f)
            return keypoints_per_frame

        keypoints_per_frame = []
        for frame in frames:
            keypoints = self.detect_keypoints(frame)
            keypoints_per_frame.append(keypoints)

        if stub_path is not None:
            os.makedirs(os.path.dirname(stub_path), exist_ok=True)
            with open(stub_path, 'wb') as f:
                pickle.dump(keypoints_per_frame, f)

        return keypoints_per_frame
