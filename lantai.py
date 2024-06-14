vertices_lantai = [
    # Lantai atas (menghadap +y) 
    0.0, 0.0, 0.0,    0.0, 0.0,  0.0, 1.0, 0.0, # 0
    6.0, 0.0, 0.0,    1.0, 0.0,  0.0, 1.0, 0.0,# 1
    6.0, 0.0, 6.0,    1.0, 1.0,  0.0, 1.0, 0.0,# 2
    0.0, 0.0, 6.0,    0.0, 1.0,  0.0, 1.0, 0.0,# 3

    # Lantai bawah (menghadap -y)
    0.0, -0.25, 0.0,   0.0, 0.0,  0.0, -1.0, 0.0, # 4
    6.0, -0.25, 0.0,   1.0, 0.0,  0.0, -1.0, 0.0,# 5
    6.0, -0.25, 6.0,   1.0, 1.0,  0.0, -1.0, 0.0,# 6
    0.0, -0.25, 6.0,   0.0, 1.0,  0.0, -1.0, 0.0, # 7

    # Lantai kanan
    6.0, 0.0, 6.0,   0.0, 0.0,   1.0, 0.0, 0.0,          
    6.0, 0.0, 0.0,   1.0, 0.0,   1.0, 0.0, 0.0,
    6.0, -0.25, 6.0, 1.0, 1.0,   1.0, 0.0, 0.0,
    6.0, -0.25, 0.0, 0.0, 1.0,   1.0, 0.0, 0.0,

    #lantai kiri
    0.0, 0.0, 6.0,   0.0, 0.0,   -1.0, 0.0, 0.0,
    0.0, 0.0, 0.0,   1.0, 0.0,   -1.0, 0.0, 0.0,
    0.0, -0.25, 6.0, 1.0, 1.0,   -1.0, 0.0, 0.0,
    0.0, -0.25, 0.0, 0.0, 1.0,   -1.0, 0.0, 0.0,
    
    #lantai depan
    0.0, 0.0, 6.0,   0.0, 0.0,   0.0, 0.0, 1.0,
    6.0, 0.0, 6.0,   1.0, 0.0,   0.0, 0.0, 1.0,
    0.0, -0.25, 6.0, 1.0, 1.0,   0.0, 0.0, 1.0,
    6.0, -0.25, 6.0, 0.0, 1.0,   0.0, 0.0, 1.0,

    #lantai belakang
    0.0, 0.0, 0.0,   0.0, 0.0,   0.0, 0.0, -1.0,
    6.0, 0.0, 0.0,   1.0, 0.0,   0.0, 0.0, -1.0,
    0.0, -0.25, 0.0, 1.0, 1.0,   0.0, 0.0, -1.0,
    6.0, -0.25, 0.0, 0.0, 1.0,   0.0, 0.0, -1.0
    
]
indices_lantai = [
    # Lantai atas
    0, 1, 2, 2, 3, 0,

    # Lantai bawah
    4, 5, 6, 6, 7, 4,
    9, 8, 10, 9, 11, 10,
    13, 12, 14, 13, 15, 14,
    17, 16, 18, 17, 19, 18,
    20, 21, 23, 20, 22, 23


    # # Sisi lantai (menghadap -x dan +x)
    # 0, 1, 5, 5, 4, 0,
    # 1, 2, 6, 6, 5, 1,
    # 2, 3, 7, 7, 6, 2,
    # 3, 0, 4, 4, 7, 3,
]
