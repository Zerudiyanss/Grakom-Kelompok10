vertices_pintu = [
    # Pintu depan (menghadap +z)
    -0.55, 0.0, 0.025,  0.0, 0.0,   0.0, 1.0, 0.5, # 0
    -0.55, 2.1, 0.025,  0.0, 1.0,   0.0, 1.0, 0.5, # 1
     0.55, 2.1, 0.025,  1.0, 1.0,   0.0, 1.0, 0.5, # 2
     0.55, 0.0, 0.025,  1.0, 0.0,   0.0, 1.0, 0.5, # 3

    # Pintu belakang (menghadap -z)
    -0.55, 0.0, -0.025,  0.0, 0.0,  0.0, 0.0, -1.0, # 4
    -0.55, 2.1, -0.025,  0.0, 1.0,  0.0, 0.0, -1.0, # 5
     0.55, 2.1, -0.025,  1.0, 1.0,  0.0, 0.0, -1.0, # 6
     0.55, 0.0, -0.025,  1.0, 0.0,  0.0, 0.0, -1.0, # 7
]
indices_pintu = [
    # Pintu depan
    0, 1, 2,  2, 3, 0,

    # Pintu belakang
    4, 5, 6,  6, 7, 4,

    # Sisi kiri pintu (menghadap -x)
    0, 1, 5,  5, 4, 0,

    # Sisi kanan pintu (menghadap +x)
    3, 2, 6,  6, 7, 3,

    # Sisi atas pintu (menghadap +y)
    1, 2, 6,  6, 5, 1,

    # Sisi bawah pintu (menghadap -y)
    0, 3, 7,  7, 4, 0,
]
