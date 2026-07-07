# Kích thước sân chuẩn FIFA: Dài 105m, Rộng 68m
# Quy ước hệ tọa độ: 
# Gốc tọa độ (0, 0) ở góc trên bên trái sân.
# Trục X chạy dọc theo chiều dài sân (0 đến 105)
# Trục Y chạy dọc theo chiều rộng sân (0 đến 68)

PITCH_KEYPOINTS_REAL = {
    # --- ĐƯỜNG BIÊN NGANG TRÁI (X = 0) ---
    0: (0, 0),         # 01: Góc trên trái
    1: (0, 13.84),     # 02: Giao điểm vòng 16m50 trên
    2: (0, 24.84),     # 03: Giao điểm vòng 5m50 trên
    3: (0, 43.16),     # 04: Giao điểm vòng 5m50 dưới
    4: (0, 54.16),     # 05: Giao điểm vòng 16m50 dưới
    5: (0, 68),        # 06: Góc dưới trái

    # --- KHU VỰC 16m50 TRÁI ---
    6: (5.5, 24.84),   # 07: Góc trên vòng 5m50
    7: (5.5, 43.16),   # 08: Góc dưới vòng 5m50
    8: (11, 34),       # 09: Chấm phạt đền trái
    9: (16.5, 13.84),  # 10: Góc trên vòng 16m50
    10: (16.5, 26.69), # 11: Giao điểm vòng cung 16m50 (trên)
    11: (16.5, 41.31), # 12: Giao điểm vòng cung 16m50 (dưới)
    12: (16.5, 54.16), # 13: Góc dưới vòng 16m50

    # --- KHU VỰC GIỮA SÂN ---
    13: (43.35, 34),   # 14: Rìa trái vòng tròn trung tâm
    14: (52.5, 0),     # 15: Giao điểm đường giữa sân (biên dọc trên)
    15: (52.5, 24.85), # 16: Giao điểm vòng tròn trung tâm (trên)
    16: (52.5, 43.15), # 17: Giao điểm vòng tròn trung tâm (dưới)
    17: (52.5, 68),    # 18: Giao điểm đường giữa sân (biên dọc dưới)
    18: (61.65, 34),   # 19: Rìa phải vòng tròn trung tâm

    # --- KHU VỰC 16m50 PHẢI ---
    19: (88.5, 13.84), # 20: Góc trên vòng 16m50 phải
    20: (88.5, 26.69), # 21: Giao điểm vòng cung 16m50 phải (trên)
    21: (88.5, 41.31), # 22: Giao điểm vòng cung 16m50 phải (dưới)
    22: (88.5, 54.16), # 23: Góc dưới vòng 16m50 phải
    23: (94, 34),      # 24: Chấm phạt đền phải
    24: (99.5, 24.84), # 25: Góc trên vòng 5m50 phải
    25: (99.5, 43.16), # 26: Góc dưới vòng 5m50 phải

    # --- ĐƯỜNG BIÊN NGANG PHẢI (X = 105) ---
    26: (105, 0),      # 27: Góc trên phải
    27: (105, 13.84),  # 28: Giao điểm vòng 16m50 phải trên
    28: (105, 24.84),  # 29: Giao điểm vòng 5m50 phải trên
    29: (105, 43.16),  # 30: Giao điểm vòng 5m50 phải dưới
    30: (105, 54.16),  # 31: Giao điểm vòng 16m50 phải dưới
    31: (105, 68),     # 32: Góc dưới phải
}
