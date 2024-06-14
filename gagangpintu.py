vertices_gagang = [
    # Gagang pintu depan 
    0.0, 1.05, -0.08,  0.5, 0.5,  0.0, 0.0, 1.0,  # 0
    0.08, 1.05, -0.08,  1.0, 0.5,  0.0, 0.0, 1.0,  # 1
    0.04, 1.08, -0.08,  0.75, 1.0,  0.0, 0.0, 1.0,  # 2
    -0.04, 1.08, -0.08,  0.25, 1.0,  0.0, 0.0, 1.0,  # 3
    -0.08, 1.05, -0.08,  0.0, 0.5,  0.0, 0.0, 1.0,  # 4
    -0.04, 1.0, -0.08,  0.25, 0.0,  0.0, 0.0, 1.0,  # 5
    0.04, 1.0, -0.08,  0.75, 0.0,  0.0, 0.0, 1.0,  # 6

    # Gagang pintu belakang 
    0.0, 1.05, 0.0,  0.5, 0.5,  0.0, 0.0, -1.0,  # 7
    0.08, 1.05, 0.0,  1.0, 0.5,  0.0, 0.0, -1.0,  # 8
    0.04, 1.08, 0.0,  0.75, 1.0,  0.0, 0.0, -1.0,  # 9
    -0.04, 1.08, 0.0,  0.25, 1.0,  0.0, 0.0, -1.0,  # 10
    -0.08, 1.05, 0.0,  0.0, 0.5,  0.0, 0.0, -1.0,  # 11
    -0.04, 1.0, 0.0,  0.25, 0.0,  0.0, 0.0, -1.0,  # 12
    0.04, 1.0, 0.0,  0.75, 0.0,  0.0, 0.0, -1.0,  # 13
]

indices_gagang = [
    # Sisi depan
    0, 1, 2,
    0, 2, 3,
    0, 3, 4,
    0, 4, 5,
    0, 5, 6,
    0, 6, 1,

    # Sisi belakang
    7, 8, 9,
    7, 9, 10,
    7, 10, 11,
    7, 11, 12,
    7, 12, 13,
    7, 13, 8,

    # Menghubungkan sisi depan dan belakang
    1, 8, 9, 1, 9, 2,
    2, 9, 10, 2, 10, 3,
    3, 10, 11, 3, 11, 4,
    4, 11, 12, 4, 12, 5,
    5, 12, 13, 5, 13, 6,
    6, 13, 8, 6, 8, 1,
]
