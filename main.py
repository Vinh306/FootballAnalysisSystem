from speed_and_distance_estimator import speed_and_distance_estimator
from utils.video_utils import read_video, save_video
from trackers import Tracker
from team_assigner import Team
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from view_transformer import ViewTransformer
from speed_and_distance_estimator.speed_and_distance_estimator import SpeedAndDistanceEstimator
from pitch_detector.pitch_keypoint_detector import PitchKeypointDetector
import numpy as np

def main():
    video_path = "input_video/video2.mp4"
    output_path = "runs/output_annotations2.mp4"

    frames = read_video(video_path)
    
    tracker = Tracker("train_YOLO\\runs\\detect\\train\\weights\\best.pt")

    tracks = tracker.get_tracked_objects(frames, read_from_stub=True, stub_path="stubs/tracks_stubs2.pkl")

    # get positions for each track
    tracker.add_position_to_tracks(tracks)

    # Estimate camera movement
    camera_movement_estimator = CameraMovementEstimator(frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(frames, read_from_stub=True, stub_path="stubs/camera_movement_stubs2.pkl")
    camera_movement_estimator.add_adjust_position_to_tracks(tracks, camera_movement_per_frame)

    # ------------------ PHẦN MỚI: PHÁT HIỆN SÂN VÀ TÍNH MA TRẬN ------------------
    # Khởi tạo mô hình nhận diện sân (đảm bảo đường dẫn đúng)
    pitch_detector = PitchKeypointDetector("pitch_detector/yolo-football-pitch-detection.pt")
    
    # Lấy tọa độ pixel của tất cả các frame (dùng stub để chạy nhanh từ lần 2)
    keypoints_per_frame = pitch_detector.get_keypoints_for_video(
        frames, 
        read_from_stub=True, 
        stub_path="stubs/pitch_keypoints_stubs2.pkl"
    )
    
    # Tính toán ma trận biến đổi (Homography) cho từng frame
    view_transformer = ViewTransformer()
    homography_matrices = []
    
    for frame_idx, keypoints in enumerate(keypoints_per_frame):
        pixel_pts = []
        real_pts = []
        
        # Duyệt qua các điểm mà AI tìm thấy trong frame này
        for idx, pt in keypoints.items():
            # Nếu ID điểm có trong "bản đồ thực tế" của chúng ta
            if idx in pitch_detector.pitch_template:
                pixel_pts.append(pt)
                real_pts.append(pitch_detector.pitch_template[idx])
                
        # Gọi view_transformer tính ma trận và lưu vào mảng
        matrix = view_transformer.calculate_homography(pixel_pts, real_pts)
        homography_matrices.append(matrix)
        
    # Áp dụng mảng ma trận này để biến đổi tọa độ cho tất cả các track
    view_transformer.add_transformed_position_to_tracks(tracks, homography_matrices)
    # -----------------------------------------------------------------------------

    # Interpolate ball positions
    tracks['ball'] = tracker.interpolate_ball_positions(tracks['ball'])

    # Estimate speed and distance
    speed_and_distance_estimator = SpeedAndDistanceEstimator()
    speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

    # assign team colors
    team_assigner = Team()
    team_assigner.assign_team_color(frames[0], tracks['player'][0])

    for frame_num, player_track in enumerate(tracks['player']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(frames[frame_num], track['bbox'], player_id)

            tracks['player'][frame_num][player_id]['team'] = team
            tracks['player'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    # assign ball to players
    player_ball_assigner = PlayerBallAssigner()
    team_ball_control = []
    for frame_num, player_track in enumerate(tracks['player']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_ball_assigner.assign_ball_to_players(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['player'][frame_num][assigned_player]['has_ball'] = True
        # Tỷ lệ kiểm soát bóng
        #     team_ball_control.append(tracks['player'][frame_num][assigned_player]['team'])
        # else:
        #     team_ball_control.append(team_ball_control[-1])

    team_ball_control = np.array(team_ball_control)

    # draw annotations
    output_frames = tracker.draw_annotations(frames, tracks, team_ball_control)

    # draw camera movement 
    output_frames = camera_movement_estimator.draw_camera_movement(output_frames, camera_movement_per_frame)

    # draw speed and distance
    speed_and_distance_estimator.draw_speed_and_distance(output_frames, tracks)

    save_video(output_frames, output_path)

if __name__ == "__main__":
    main()