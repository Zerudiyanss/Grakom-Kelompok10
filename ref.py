import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
from TextureLoader import load_texture
from shader import shader_function 
import pyrr
from camera import Camera
left, right, forward, backward, up, down = False, False, False, False, False, False


# instance buat kamera
cam = Camera()
WIDTH, HEIGHT = 1280, 720
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True

# Keyboard callback function ESC
def key_input_clb(window, key, scancode, action, mode):
     global left, right, forward, backward, up, down
     if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
          glfw.set_window_should_close(window, True)

     if key == glfw.KEY_W and action == glfw.PRESS:
          forward = True

     if key == glfw.KEY_S and action == glfw.PRESS:
          backward = True

     if key == glfw.KEY_A and action == glfw.PRESS:
          left = True
          
     if key == glfw.KEY_D and action == glfw.PRESS:
          right = True
          
     if key in [glfw.KEY_W, glfw.KEY_S, glfw.KEY_D, glfw.KEY_A] and action == glfw.RELEASE:
          left, right, forward, backward = False, False, False, False
          

# keyboard movement
movement_speed = 0.05
def do_movement():
     if left:
          cam.process_keyboard("LEFT", movement_speed)
     if right:
          cam.process_keyboard("RIGHT", movement_speed)
     if forward:
          cam.process_keyboard("FORWARD", movement_speed)
     if backward:
          cam.process_keyboard("BACKWARD", movement_speed)


# CALL BACK FOR THE MOUSE 
def mouse_look_clb(window, xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos

    lastX = xpos
    lastY = ypos
    
    cam.process_mouse_movement(xoffset, yoffset)


# define isi dari fungsi file shader
vertex_src, fragmen_src = shader_function()

#Here for resize file window
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

# initializing the glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")
#creating windows
window = glfw.create_window(WIDTH, HEIGHT, "Kamar Tidur", None, None)
# For checking the window
if not window:
        glfw.terminate()
        raise Exception("glfw gak bisa dibuat weh!")
# For setting windows position
glfw.set_window_pos(window, 400, 100)

# For calling the rezise capability
glfw.set_window_size_callback(window, window_resize)
# For calling the mouse callback
glfw.set_cursor_pos_callback(window, mouse_look_clb)
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
glfw.set_key_callback(window, key_input_clb)

# For make the context current
glfw.make_context_current(window)

#import vertices and indices
from lemari import vertices_lemari, indices_lemari
from pintulemari import vertices_pintulemari, indices_pintulemari
from pintulemari2 import vertices_pintulemari2, indices_pintulemari2
from keset import vertices_keset, indices_keset
from tembok import vertices_tembok, indices_tembok
from pintu import vertices_pintu, indices_pintu
from jendela import vertices_jendela, indices_jendela
from lantai import vertices_lantai, indices_lantai
from kusen import vertices_kusen, indices_kusen
from kaca import vertices_kaca, indices_kaca
from kasur import vertices_kasur, indices_kasur
from selimut import vertices_selimut, indices_selimut
from bantal import vertices_bantal, indices_bantal
from bantal1 import vertices_bantal1, indices_bantal1
from selimut1 import vertices_selimut1, indices_selimut1
from gagangpintu import vertices_gagang, indices_gagang
from gaganglemari import vertices_gaganglemari, indices_gaganglemari
from gaganglemari2 import vertices_gaganglemari2, indices_gaganglemari2


#Deklarasi tipe data here
vertices_lemari = np.array(vertices_lemari, dtype=np.float32)
indices_lemari = np.array(indices_lemari, dtype=np.uint32)

vertices_pintulemari = np.array(vertices_pintulemari, dtype=np.float32)
indices_pintulemari = np.array(indices_pintulemari, dtype=np.uint32)

vertices_pintulemari2 = np.array(vertices_pintulemari2, dtype=np.float32)
indices_pintulemari2 = np.array(indices_pintulemari2, dtype=np.uint32)

vertices_keset = np.array(vertices_keset, dtype=np.float32)
indices_keset = np.array(indices_keset, dtype=np.uint32)

vertices_tembok = np.array(vertices_tembok, dtype=np.float32)
indices_tembok = np.array(indices_tembok, dtype=np.uint32)

vertices_pintu = np.array(vertices_pintu, dtype=np.float32)
indices_pintu = np.array(indices_pintu, dtype=np.uint32)

vertices_jendela = np.array(vertices_jendela, dtype=np.float32)
indices_jendela = np.array(indices_jendela, dtype=np.uint32)

vertices_lantai = np.array(vertices_lantai, dtype=np.float32)
indices_lantai = np.array(indices_lantai, dtype=np.uint32)

vertices_kusen = np.array(vertices_kusen, dtype=np.float32)
indices_kusen = np.array(indices_kusen, dtype=np.uint32)

vertices_kaca = np.array(vertices_kaca, dtype=np.float32)
indices_kaca = np.array(indices_kaca, dtype=np.uint32)

vertices_kasur = np.array(vertices_kasur, dtype=np.float32)
indices_kasur = np.array(indices_kasur, dtype=np.uint32)

vertices_selimut = np.array(vertices_selimut, dtype=np.float32)
indices_selimut = np.array(indices_selimut, dtype=np.uint32)

vertices_bantal = np.array(vertices_bantal, dtype=np.float32)
indices_bantal = np.array(indices_bantal, dtype=np.uint32)

vertices_bantal1 = np.array(vertices_bantal, dtype=np.float32)
indices_bantal1 = np.array(indices_bantal, dtype=np.uint32)

vertices_selimut1 = np.array(vertices_selimut1, dtype=np.float32)
indices_selimut1 = np.array(indices_selimut1, dtype=np.uint32)

vertices_gagang = np.array(vertices_gagang, dtype=np.float32)
indices_gagang = np.array(indices_gagang, dtype=np.uint32)

vertices_gaganglemari = np.array(vertices_gaganglemari, dtype=np.float32)
indices_gaganglemari = np.array(indices_gaganglemari, dtype=np.uint32)

vertices_gaganglemari2 = np.array(vertices_gaganglemari2, dtype=np.float32)
indices_gaganglemari2 = np.array(indices_gaganglemari2, dtype=np.uint32)


shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragmen_src, GL_FRAGMENT_SHADER))
 

#VAO, VBO, EBO, POST, TEXTURE, NORMALS
#LEMARI
lemari_VAO = glGenVertexArrays(1)
glBindVertexArray(lemari_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_lemari.nbytes, vertices_lemari, GL_STATIC_DRAW)
#element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_lemari.nbytes, indices_lemari, GL_STATIC_DRAW)
#for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_lemari.itemsize * 8, ctypes.c_void_p(0))
#for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_lemari.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_lemari.itemsize, ctypes.c_void_p(20))


# PINTULEMARI
pintulemari_VAO = glGenVertexArrays(1)
glBindVertexArray(pintulemari_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_pintulemari.nbytes, vertices_pintulemari, GL_STATIC_DRAW)
#element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_pintulemari.nbytes, indices_pintulemari, GL_STATIC_DRAW)
#for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_pintulemari.itemsize * 8, ctypes.c_void_p(0))
#for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_pintulemari.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_pintulemari.itemsize, ctypes.c_void_p(20))


# PINTULEMARI2
pintulemari2_VAO = glGenVertexArrays(1)
glBindVertexArray(pintulemari2_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_pintulemari2.nbytes, vertices_pintulemari2, GL_STATIC_DRAW)
#element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_pintulemari2.nbytes, indices_pintulemari2, GL_STATIC_DRAW)
#for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_pintulemari2.itemsize * 8, ctypes.c_void_p(0))
#for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_pintulemari2.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_pintulemari2.itemsize, ctypes.c_void_p(20))


#KESET
keset_VAO = glGenVertexArrays(1)
glBindVertexArray(keset_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_keset.nbytes, vertices_keset, GL_STATIC_DRAW)
#element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_keset.nbytes, indices_keset, GL_STATIC_DRAW)
#for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_keset.itemsize * 8, ctypes.c_void_p(0))
#for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_keset.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_keset.itemsize, ctypes.c_void_p(20))


# TEMBOK
tembok_VAO = glGenVertexArrays(1)
glBindVertexArray(tembok_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_tembok.nbytes, vertices_tembok, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_tembok.nbytes, indices_tembok, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_tembok.itemsize * 8, ctypes.c_void_p(0))
# for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_tembok.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_tembok.itemsize, ctypes.c_void_p(20))


# PINTU
pintu_VAO = glGenVertexArrays(1)
glBindVertexArray(pintu_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_pintu.nbytes, vertices_pintu, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_pintu.nbytes, indices_pintu, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_pintu.itemsize * 8, ctypes.c_void_p(0))
# for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_pintu.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_pintu.itemsize, ctypes.c_void_p(20))


# GAGANG PINTU 
gagang_VAO = glGenVertexArrays(1)
glBindVertexArray(gagang_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_gagang.nbytes, vertices_gagang, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_gagang.nbytes, indices_gagang, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_gagang.itemsize * 8, ctypes.c_void_p(0))
# for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_gagang.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_gagang.itemsize, ctypes.c_void_p(20))


# GAGANG LEMARI
gaganglemari_VAO = glGenVertexArrays(1)
glBindVertexArray(gaganglemari_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_gaganglemari.nbytes, vertices_gaganglemari, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_gaganglemari.nbytes, indices_gaganglemari, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_gaganglemari.itemsize * 8, ctypes.c_void_p(0))
# for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_gaganglemari.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_gaganglemari.itemsize, ctypes.c_void_p(20))


# GAGANG LEMARI 2
gaganglemari2_VAO = glGenVertexArrays(1)
glBindVertexArray(gaganglemari2_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_gaganglemari2.nbytes, vertices_gaganglemari2, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_gaganglemari2.nbytes, indices_gaganglemari2, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_gaganglemari2.itemsize * 8, ctypes.c_void_p(0))
# for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_gaganglemari2.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_gaganglemari2.itemsize, ctypes.c_void_p(20))


#JENDELA
jendela_VAO = glGenVertexArrays(1)
glBindVertexArray(jendela_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_jendela.nbytes, vertices_jendela, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_jendela.nbytes, indices_jendela, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_jendela.itemsize * 8, ctypes.c_void_p(0))
# for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_jendela.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_jendela.itemsize, ctypes.c_void_p(20))


#LANTAI
lantai_VAO = glGenVertexArrays(1)
glBindVertexArray(lantai_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_lantai.nbytes, vertices_lantai, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_lantai.nbytes, indices_lantai, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_lantai.itemsize * 8, ctypes.c_void_p(0))
# for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_lantai.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_lantai.itemsize, ctypes.c_void_p(20))


# KUSEN
kusen_VAO = glGenVertexArrays(1)
glBindVertexArray(kusen_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_kusen.nbytes, vertices_kusen, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_kusen.nbytes, indices_kusen, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_kusen.itemsize * 5, ctypes.c_void_p(0))
# for color / TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_kusen.itemsize * 5, ctypes.c_void_p(12))


# KACA JENDELA
kaca_VAO = glGenVertexArrays(1)
glBindVertexArray(kaca_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_kaca.nbytes, vertices_kaca, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_kaca.nbytes, indices_kaca, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_kaca.itemsize * 8, ctypes.c_void_p(0))
# for TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_kaca.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_kaca.itemsize, ctypes.c_void_p(20))


#KASUR
kasur_VAO = glGenVertexArrays(1)
glBindVertexArray(kasur_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_kasur.nbytes, vertices_kasur, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_kasur.nbytes, indices_kasur, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_kasur.itemsize * 8, ctypes.c_void_p(0))
# for TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_kasur.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_kasur.itemsize, ctypes.c_void_p(20))


#SELIMUT
selimut_VAO = glGenVertexArrays(1)
glBindVertexArray(selimut_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_selimut.nbytes, vertices_selimut, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_selimut.nbytes, indices_selimut, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_selimut.itemsize * 8, ctypes.c_void_p(0))
# for TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_selimut.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_selimut.itemsize, ctypes.c_void_p(20))


#SELIMUT 1
selimut1_VAO = glGenVertexArrays(1)
glBindVertexArray(selimut1_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_selimut1.nbytes, vertices_selimut1, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_selimut1.nbytes, indices_selimut1, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_selimut1.itemsize * 8, ctypes.c_void_p(0))
# for TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_selimut1.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_selimut1.itemsize, ctypes.c_void_p(20))


# Bantal
bantal_VAO = glGenVertexArrays(1)
glBindVertexArray(bantal_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_bantal.nbytes, vertices_bantal, GL_STATIC_DRAW)
# element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_bantal.nbytes, indices_bantal, GL_STATIC_DRAW)
# for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_bantal.itemsize * 8, ctypes.c_void_p(0))
# for color TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_bantal.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_bantal.itemsize, ctypes.c_void_p(20))


#BANTAL1
bantal1_VAO = glGenVertexArrays(1)
glBindVertexArray(bantal1_VAO)
# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_bantal1.nbytes, vertices_bantal1, GL_STATIC_DRAW)
#element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_bantal1.nbytes, indices_bantal1, GL_STATIC_DRAW)
#for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_bantal1.itemsize * 8, ctypes.c_void_p(0))
#for TEXTURE coordinate
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_bantal1.itemsize * 8, ctypes.c_void_p(12))
#Normals
glEnableVertexAttribArray(2)
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices_bantal1.itemsize, ctypes.c_void_p(20))

# ~~ END HERE ~~

# The value here define how many texture we want to create
texture = glGenTextures(14)

#Texture here
lemari_texture = load_texture("TEXTURE/lemari3.jpg", texture[0])
pintulemari_texture = load_texture("TEXTURE/pintulemari3.jpg", texture[1])
keset = load_texture("TEXTURE/keset2.jpg", texture[2])
wall_texture = load_texture("TEXTURE/dinding.jpg", texture[3])
pintu_texture = load_texture("TEXTURE/pintu.jpg", texture[4])
jendela_texture = load_texture("TEXTURE/jendela.jpg", texture[5])
lantai_texture = load_texture("TEXTURE/floor2.jpg", texture[6])
kaca_texture = load_texture("TEXTURE/kaca.jpg", texture[8])
kasur_texture = load_texture("TEXTURE/kaca.jpg", texture[9])
bantal_texture = load_texture("TEXTURE/bantal1.jpg", texture[10])
selimut_texture = load_texture("TEXTURE/keset2.jpg", texture[11])
selimut1_texture = load_texture("TEXTURE/kaca.jpg", texture[12])


#using the shader
glUseProgram(shader)

#window color
glClearColor(0.1, 0.1, 0.1, 1)

#for free rotation
glEnable(GL_DEPTH_TEST)

#this is for transparancy
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

#for projection matrix
projection = pyrr.matrix44.create_perspective_projection_matrix(45, WIDTH/HEIGHT, 0.1, 100)

#Translasi here
lemari = pyrr.matrix44.create_from_translation(pyrr.Vector3([4.3, -0.22, 2]))
pintulemari = pyrr.matrix44.create_from_translation(pyrr.Vector3([4.9, -0.2, 1.42]))
pintulemari2 = pyrr.matrix44.create_from_translation(pyrr.Vector3([4.3, -0.2, 1.42]))
keset = pyrr.matrix44.create_from_translation(pyrr.Vector3([1, -0.2, 7.5]))
tembok = pyrr.matrix44.create_from_translation(pyrr.Vector3([-1.0, -0.01, 1]))
pintu = pyrr.matrix44.create_from_translation(pyrr.Vector3([2.5, -0.02, 7.01]))
jendela = pyrr.matrix44.create_from_translation(pyrr.Vector3([3, 0.8, 1.09]))
lantai = pyrr.matrix44.create_from_translation(pyrr.Vector3([-1.0, -0.01, 1]))
kusen = pyrr.matrix44.create_from_translation(pyrr.Vector3([2.5, -0.02, 7]))
kaca = pyrr.matrix44.create_from_translation(pyrr.Vector3([3, 0.8, 1.09]))
kasur = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.7, -0.49, 3.5]))
selimut = pyrr.matrix44.create_from_translation(pyrr.Vector3([2.059, -0.1, 3.5]))
bantal = pyrr.matrix44.create_from_translation(pyrr.Vector3([-0.6, 0.4, 4]))
bantal1 = pyrr.matrix44.create_from_translation(pyrr.Vector3([-0.6, 0.4, 3]))
selimut1 = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.012, -0.1, 3.5]))
gagang = pyrr.matrix44.create_from_translation(pyrr.Vector3([2.1, -0.02, 7.05]))
gaganglemari = pyrr.matrix44.create_from_translation(pyrr.Vector3([6.3, -0.5, 0.42]))
gaganglemari2 = pyrr.matrix44.create_from_translation(pyrr.Vector3([5.9, -0.5, 0.42]))


# ROTASI UNTUK JENDELA
rotation_matrix = pyrr.matrix44.create_from_y_rotation(np.radians(90))
new_jendela = pyrr.matrix44.multiply(jendela, rotation_matrix)
jendela = jendela @ rotation_matrix

#ROTASI KACA
rotation_matrix = pyrr.matrix44.create_from_y_rotation(np.radians(90))
new_kaca = pyrr.matrix44.multiply(kaca, rotation_matrix)
kaca = kaca @ rotation_matrix

# ROTASI UNTUK LEMARI
rotation_matrix = pyrr.matrix44.create_from_y_rotation(np.radians(90))
new_lemari = pyrr.matrix44.multiply(lemari, rotation_matrix)
lemari = lemari @ rotation_matrix

# ROTASI UNTUK PINTU LEMARI
rotation_matrix = pyrr.matrix44.create_from_y_rotation(np.radians(90))
new_pintulemari = pyrr.matrix44.multiply(pintulemari, rotation_matrix)
pintulemari = pintulemari @ rotation_matrix

# ROTASI UNTUK PINTU LEMARI
rotation_matrix = pyrr.matrix44.create_from_y_rotation(np.radians(90))
new_pintulemari2 = pyrr.matrix44.multiply(pintulemari2, rotation_matrix)
pintulemari2 = pintulemari2 @ rotation_matrix

# ROTASI GAGANG LEMARI
rotation_matrix = pyrr.matrix44.create_from_y_rotation(np.radians(90))
new_gaganglemari = pyrr.matrix44.multiply(gaganglemari, rotation_matrix)
gaganglemari = gaganglemari @ rotation_matrix

# GAGANG LEMARI 2
rotation_matrix = pyrr.matrix44.create_from_y_rotation(np.radians(90))
new_gaganglemari2 = pyrr.matrix44.multiply(gaganglemari2, rotation_matrix)
gaganglemari2 = gaganglemari2 @ rotation_matrix

#ROTASI KASUR
rotation_matrix = pyrr.matrix44.create_from_z_rotation(np.radians(180))
new_kasur = pyrr.matrix44.multiply(kasur, rotation_matrix)
kasur = kasur @ rotation_matrix


model_loc = glGetUniformLocation(shader, "model")
proj_loc= glGetUniformLocation(shader, "projection")
#adding shader for view matrix
view_loc= glGetUniformLocation(shader, "view")
#for switcher inside the fragment
switcher_loc = glGetUniformLocation(shader, "switcher")

# Lighting properties
lightPos = pyrr.Vector3([5.0, 5.0, 5.0])
viewPos = pyrr.Vector3([1.2, 1.2, 1.2])

#this one too moved into resize for better window management
glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


# Main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    do_movement()

    view = cam.get_view_matrix()
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glUniform1i(switcher_loc, 0)


     #lighting
    glUniformMatrix4fv(glGetUniformLocation(shader, "view"), 1, GL_FALSE, view)
    glUniform3fv(glGetUniformLocation(shader, "lightPos"), 1, lightPos)
    glUniform3fv(glGetUniformLocation(shader, "viewPos"), 1, viewPos)
    glUniform3f(glGetUniformLocation(shader, "lightColor"), 1.0, 1.0, 1.0)
   
    # Render lemari
    glBindVertexArray(lemari_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, lemari)
    glDrawElements(GL_TRIANGLES, len(indices_lemari), GL_UNSIGNED_INT, None)

    #Render GAGANG PINTU
    glBindVertexArray(gagang_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[13])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, gagang)
    glDrawElements(GL_TRIANGLES, len(indices_gagang), GL_UNSIGNED_INT, None)
    # GAGANG LEMARI
    glBindVertexArray(gaganglemari_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[13])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, gaganglemari)
    glDrawElements(GL_TRIANGLES, len(indices_gaganglemari), GL_UNSIGNED_INT, None)
    # GAGANG LEMARI 2
    glBindVertexArray(gaganglemari2_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[13])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, gaganglemari2)
    glDrawElements(GL_TRIANGLES, len(indices_gaganglemari2), GL_UNSIGNED_INT, None)

    # Render pintu lemari
    glBindVertexArray(pintulemari_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, pintulemari)
    glDrawElements(GL_TRIANGLES, len(indices_pintulemari), GL_UNSIGNED_INT, None)

    # Render pintu lemari kedua
    glBindVertexArray(pintulemari2_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, pintulemari2)
    glDrawElements(GL_TRIANGLES, len(indices_pintulemari2), GL_UNSIGNED_INT, None)

    glBindVertexArray(keset_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, keset)
    glDrawElements(GL_TRIANGLES, len(indices_keset), GL_UNSIGNED_INT, None)

    # Render tembok
    glBindVertexArray(tembok_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[3])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, tembok)
    glDrawElements(GL_TRIANGLES, len(indices_tembok), GL_UNSIGNED_INT, None)

    # Render pintu
    glBindVertexArray(pintu_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[4])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, pintu)
    glDrawElements(GL_TRIANGLES, len(indices_pintu), GL_UNSIGNED_INT, None)

     # Render jendela
    glBindVertexArray(jendela_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[5])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, jendela)
    glDrawElements(GL_TRIANGLES, len(indices_jendela), GL_UNSIGNED_INT, None)

    # Render lantai
    glBindVertexArray(lantai_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[6])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, lantai)
    glDrawElements(GL_TRIANGLES, len(indices_lantai), GL_UNSIGNED_INT, None)

    #KUSEN PINTU
    glBindVertexArray(kusen_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[7])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, kusen)
    glDrawElements(GL_TRIANGLES, len(indices_kusen), GL_UNSIGNED_INT, None)

    # KACA JENDELA
    glBindVertexArray(kaca_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[8])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, kaca)
    glDrawElements(GL_TRIANGLES, len(indices_kaca), GL_UNSIGNED_INT, None)
 
    # KASUR
    glBindVertexArray(kasur_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[9])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, kasur)
    glDrawElements(GL_TRIANGLES, len(indices_kasur), GL_UNSIGNED_INT, None)

    # SELIMUT
    glBindVertexArray(selimut_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[11])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, selimut)
    glDrawElements(GL_TRIANGLES, len(indices_selimut), GL_UNSIGNED_INT, None)
    #SELIMUT 1
    glBindVertexArray(selimut1_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[12])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, selimut1)
    glDrawElements(GL_TRIANGLES, len(indices_selimut1), GL_UNSIGNED_INT, None)
    
    # BANTAL
    glBindVertexArray(bantal_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[10])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, bantal)
    glDrawElements(GL_TRIANGLES, len(indices_bantal), GL_UNSIGNED_INT, None)
    # BANTAL 
    glBindVertexArray(bantal1_VAO)
    glBindTexture(GL_TEXTURE_2D, texture[10])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, bantal1)
    glDrawElements(GL_TRIANGLES, len(indices_bantal1), GL_UNSIGNED_INT, None)


    glfw.swap_buffers(window)

# For terminating glfw
glfw.terminate()
