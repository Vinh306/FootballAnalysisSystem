import numpy as np
import cv2


class ViewTransformer:
    def __init__(self):
        pass

    def calculate_homography(self, pixel_points, real_points):
        """
        Tính ma trận biến đổi (Homography) cho 1 frame cụ thể.
        Yêu cầu truyền vào mảng các điểm Pixel và mảng các điểm Thực tế tương ứng.
        """
        pixel_points = np.array(pixel_points, dtype=np.float32)
        real_points = np.array(real_points, dtype=np.float32)
        
        # Thuật toán Homography cần tối thiểu 4 điểm để tính toán
        if len(pixel_points) >= 4:
            # Sử dụng cv2.RANSAC để loại bỏ bớt các điểm nhiễu (outliers) do AI nhận diện lệch
            matrix, _ = cv2.findHomography(pixel_points, real_points, cv2.RANSAC, 5.0)
            return matrix
        return None

    def transform_point(self, point, matrix):
        """
        Biến đổi 1 điểm tọa độ từ Pixel sang Mét dựa trên ma trận.
        """
        if matrix is None:
            return None
            
        reshaped_point = point.reshape(-1, 1, 2).astype(np.float32)
        transform_point = cv2.perspectiveTransform(reshaped_point, matrix)
        return transform_point.reshape(-1, 2)

    def add_transformed_position_to_tracks(self, tracks, homography_matrices):
        """
        Cập nhật lại tọa độ thực tế cho toàn bộ cầu thủ và bóng trong tất cả các frame.
        homography_matrices: Danh sách các ma trận, mỗi frame có 1 ma trận tương ứng.
        """
        for object, object_tracks in tracks.items():
            for frame_num, track in enumerate(object_tracks):
                
                # Lấy ma trận của frame thứ frame_num
                matrix = homography_matrices[frame_num]
                
                for track_id, track_info in track.items():
                    # Sử dụng tọa độ gốc (hoặc đã adjust nếu có)
                    position = track_info.get('position_adjusted', track_info['position'])
                    position = np.array(position)
                    
                    # Biến đổi tọa độ bằng ma trận của CHÍNH frame đó
                    position_transformed = self.transform_point(position, matrix)
                    
                    if position_transformed is not None:
                        position_transformed = position_transformed.squeeze().tolist()
                        
                    tracks[object][frame_num][track_id]['position_transformed'] = position_transformed
