PLAYER1_COLOR = "red"
PLAYER2_COLOR = "blue"
FRAME_RATE = 30
POINT_RADIUS = 2
TAIL_LENGTH = 8
COLORS = [str(hex(i))[2:].zfill(2) for i in range(0, 256, 8)]
COLORS_3D = [str(hex(i))[2:].zfill(2) for i in range(128, 256, 4)]
COLORS_3D_P1_AVG = ["#" + str(hex(i))[2:].zfill(2) + "0c" + str(hex(int(2*i/3)-40))[2:].zfill(2) for i in range(128, 256, 4)]
COLORS_3D_P2_AVG = ["#" + "0c" + str(hex(int(2*i/3)-40))[2:].zfill(2) + str(hex(int(2*i/3)-40))[2:].zfill(2) for i in range(192, 256, 2)]

NEW_COLOR = "ff"

LENGTH = 400
BOTTOM_LEFT = (100, 460)