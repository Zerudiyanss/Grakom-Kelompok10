import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
from TextureLoader import load_texture
from shader import shader_function 
import pyrr
from PIL import Image
from camera import Camera
left, right, forward, backward, up, down = False, False, False, False, False, False


# instance buat kamera
cam = Camera()
WIDTH, HEIGHT = 1280, 720
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True

# Keyboard callback funciton ESC
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

     if key == glfw.KEY_Z and action == glfw.PRESS:
          up = True

     if key == glfw.KEY_X and action == glfw.PRESS:
          down = True
          
     if key in [glfw.KEY_W, glfw.KEY_S, glfw.KEY_D, glfw.KEY_A, glfw.KEY_Z, glfw.KEY_X] and action == glfw.RELEASE:
          left, right, forward, backward, up, down = False, False, False, False, False, False

# keyboard movement
def do_movement():
     if left:
          cam.process_keyboard("LEFT", 0.005)
     if right:
          cam.process_keyboard("RIGHT", 0.005)
     if forward:
          cam.process_keyboard("FORWARD", 0.005)
     if backward:
          cam.process_keyboard("BACKWARD", 0.005)
     if up:
          cam.process_keyboard("UP", 0.005)
     if down:
          cam.process_keyboard("DOWN", 0.005)

# CALL BACK FOR THE MOUSE look callback?
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
    raise Exception("glfw can not be initialized woy!")

# For creating da windows
# UPDATED FOR SUPPORTING DA CAMERA
window = glfw.create_window(WIDTH, HEIGHT, "Kamar Tidur", None, None)

# checking whether the window has created or no
if not window:
        glfw.terminate()
        raise Exception("glfw tidak bisa dibuat!")

# For setting da windows position
glfw.set_window_pos(window, 150, 100)

# For calling the rezise capability
glfw.set_window_size_callback(window, window_resize)

# For calling the mouse callback
glfw.set_cursor_pos_callback(window, mouse_look_clb)
# glfw.set_cursor_enter_callback(window, mouse_enter_clb)
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
glfw.set_key_callback(window, key_input_clb)

# For make the context current
glfw.make_context_current(window)


from ret_obj2 import vertices_keset, indices_keset
from jendela import vertices_jendela, indices_jendela

vertices_lemari = [
     
     # BODY

     # Face depan

    1.2, 0.2, -1.0, 0.0, 0.0,
    2.4, 0.2, -1.0, 1.0, 0.0,
    2.4, 0.8, -1.0, 1.0, 1.0,
    1.2, 0.8, -1.0, 0.0, 1.0,

    # Face belakang

    1.2, 0.2, -1.6,  0.0, 0.0,
    2.4, 0.2, -1.6, 1.0, 0.0,
    2.4, 0.8, -1.6,  1.0, 1.0,
    1.2, 0.8, -1.6,  0.0, 1.0,	

    # Kanan

    2.4, 0.2, -1.0,  0.0, 0.0,
    2.4, 0.2, -1.6,  1.0, 0.0,
    2.4, 0.8, -1.6,  1.0, 1.0,
    2.4, 0.8, -1.0, 0.0, 1.0,

    # Kiri

    1.2, 0.2, -1.0,  0.0, 0.0,
    1.2, 0.2, -1.6,  1.0, 0.0,
    1.2, 0.8, -1.6,  1.0, 1.0,
    1.2, 0.8, -1.0, 0.0, 1.0,

    # Atas

    1.2, 0.8, -1.0,  0.0, 0.0,
    2.4, 0.8, -1.0,  1.0, 0.0,
    2.4, 0.8, -1.6,  1.0, 1.0,
    1.2, 0.8, -1.6,  0.0, 1.0,

    # Bawah

    1.2, 0.2, -1.0, 0.0, 0.0,
    2.4, 0.2, -1.0, 1.0, 0.0,
    2.4, 0.2, -1.6, 1.0, 1.0,
    1.2, 0.2, -1.6, 0.0, 1.0

   
]            

vertices_pintulemari = [
     
      # PINTU

    # Face depan

    1.3, 0.3, -1.05, 0.0, 0.0,
    1.7, 0.3, -1.05, 1.0, 0.0,
    1.7, 0.7, -1.05, 1.0, 1.0,
    1.3, 0.7, -1.05, 0.0, 1.0,

    # Face belakang

    1.3, 0.3, -1.0, 0.0, 0.0,
    1.7, 0.3, -1.0, 1.0, 0.0,
    1.7, 0.7, -1.0, 1.0, 1.0,
    1.3, 0.7, -1.0, 0.0, 1.0,	

    # Kanan

    1.7, 0.3, -1.05, 0.0, 0.0,
    1.7, 0.3, -1.0, 1.0, 0.0,
    1.7, 0.7, -1.0, 1.0, 1.0,
    1.7, 0.7, -1.05, 0.0, 1.0,

    # Kiri

    1.3, 0.3, -1.05, 0.0, 0.0,
    1.3, 0.3, -1.0, 1.0, 0.0,
    1.3, 0.7, -1.0, 1.0, 1.0,
    1.3, 0.7, -1.05, 0.0, 1.0,

    # Atas

    1.3, 0.7, -1.05, 0.0, 0.0,
    1.7, 0.7, -1.05, 1.0, 0.0,
    1.7, 0.7, -1.0, 1.0, 1.0,
    1.3, 0.7, -1.0, 0.0, 1.0,

    # Bawah

    1.3, 0.3, -1.05, 0.0, 0.0,
    1.7, 0.3, -1.05, 1.0, 0.0,
    1.7, 0.3, -1.0, 1.0, 1.0,
    1.3, 0.3, -1.0, 0.0, 1.0
]

vertices_pintulemari2 = [
     
      # PINTU

    # Face depan

    1.3, 0.3, -1.05, 0.0, 0.0,
    1.7, 0.3, -1.05, 1.0, 0.0,
    1.7, 0.7, -1.05, 1.0, 1.0,
    1.3, 0.7, -1.05, 0.0, 1.0,

    # Face belakang

    1.3, 0.3, -1.0, 0.0, 0.0,
    1.7, 0.3, -1.0, 1.0, 0.0,
    1.7, 0.7, -1.0, 1.0, 1.0,
    1.3, 0.7, -1.0, 0.0, 1.0,	

    # Kanan

    1.7, 0.3, -1.05, 0.0, 0.0,
    1.7, 0.3, -1.0, 1.0, 0.0,
    1.7, 0.7, -1.0, 1.0, 1.0,
    1.7, 0.7, -1.05, 0.0, 1.0,

    # Kiri

    1.3, 0.3, -1.05, 0.0, 0.0,
    1.3, 0.3, -1.0, 1.0, 0.0,
    1.3, 0.7, -1.0, 1.0, 1.0,
    1.3, 0.7, -1.05, 0.0, 1.0,

    # Atas

    1.3, 0.7, -1.05, 0.0, 0.0,
    1.7, 0.7, -1.05, 1.0, 0.0,
    1.7, 0.7, -1.0, 1.0, 1.0,
    1.3, 0.7, -1.0, 0.0, 1.0,

    # Bawah

    1.3, 0.3, -1.05, 0.0, 0.0,
    1.7, 0.3, -1.05, 1.0, 0.0,
    1.7, 0.3, -1.0, 1.0, 1.0,
    1.3, 0.3, -1.0, 0.0, 1.0
]

indices_lemari = [ 0,  1,  2,  2,  3,  0,
                 4,  5,  6,  6,  7,  4,
                 8,  9, 10, 10, 11,  8,
                12, 13, 14, 14, 15, 12,
                16, 17, 18, 18, 19, 16,
                20, 21, 22, 22, 23, 20

                # 24, 25, 26, 26, 27, 24,
                # 28, 29, 30, 30, 31, 28,
                # 32, 33, 34, 34, 35, 32,
                # 36, 37, 38, 38, 39, 36,
                # 40, 41, 42, 42, 43, 40,
                # 44, 45, 46, 46, 47, 44
                
                ]

indices_pintulemari = [
                 0,  1,  2,  2,  3,  0,
                 4,  5,  6,  6,  7,  4,
                 8,  9, 10, 10, 11,  8,
                12, 13, 14, 14, 15, 12,
                16, 17, 18, 18, 19, 16,
                20, 21, 22, 22, 23, 20
]

indices_pintulemari2 = [
                 0,  1,  2,  2,  3,  0,
                 4,  5,  6,  6,  7,  4,
                 8,  9, 10, 10, 11,  8,
                12, 13, 14, 14, 15, 12,
                16, 17, 18, 18, 19, 16,
                20, 21, 22, 22, 23, 20
]



#Deklarasi tipe data here

vertices_lemari = np.array(vertices_lemari, dtype=np.float32)
indices_lemari = np.array(indices_lemari, dtype=np.uint32)

vertices_pintulemari = np.array(vertices_pintulemari, dtype=np.float32)
indices_pintulemari = np.array(indices_pintulemari, dtype=np.uint32)

vertices_pintulemari2 = np.array(vertices_pintulemari2, dtype=np.float32)
indices_pintulemari2 = np.array(indices_pintulemari2, dtype=np.uint32)

vertices_keset = np.array(vertices_keset, dtype=np.float32)
indices_keset = np.array(indices_keset, dtype=np.uint32)

vertices_jendela = np.array(vertices_jendela, dtype=np.float32)
indices_jendela = np.array(indices_jendela, dtype=np.uint32)


shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragmen_src, GL_FRAGMENT_SHADER))
 
# Cube VAO, VBO, EBO here
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
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_lemari.itemsize * 5, ctypes.c_void_p(0))

#for color / TEXTURE coordinate, depending on the value, check pipeline!!
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_lemari.itemsize * 5, ctypes.c_void_p(12))


# Cube VAO, VBO, EBO here
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
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_pintulemari.itemsize * 5, ctypes.c_void_p(0))

#for color / TEXTURE coordinate, depending on the value, check pipeline!!
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_pintulemari.itemsize * 5, ctypes.c_void_p(12))


# Cube VAO, VBO, EBO here
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
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_pintulemari2.itemsize * 5, ctypes.c_void_p(0))

#for color / TEXTURE coordinate, depending on the value, check pipeline!!
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_pintulemari2.itemsize * 5, ctypes.c_void_p(12))


#VAO KESET
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
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_keset.itemsize * 5, ctypes.c_void_p(0))

#for color / TEXTURE coordinate, depending on the value, check pipeline!!
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_keset.itemsize * 5, ctypes.c_void_p(12))


#VAO jendela
jendela_VAO = glGenVertexArrays(1)
glBindVertexArray(jendela_VAO)

# vertex buffer object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices_jendela.nbytes, vertices_jendela, GL_STATIC_DRAW)

#element buffer object
EBO = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_jendela.nbytes, indices_jendela, GL_STATIC_DRAW)

#for vertex POSITION coordinate
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices_jendela.itemsize * 5, ctypes.c_void_p(0))

#for color / TEXTURE coordinate, depending on the value, check pipeline!!
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices_jendela.itemsize * 5, ctypes.c_void_p(12))


# ~~ END HERE ~~

# The value here define how many texture we want to create
texture = glGenTextures(15)

#Texture here

lemari_texture = load_texture("TEXTURE/wood.jpg", texture[0])
pintulemari_texture = load_texture("TEXTURE/steelhammer1.jpg", texture[1])
keset = load_texture("TEXTURE/metal.jpg", texture[2])
jendela = load_texture("TEXTURE/metal.jpg", texture[3])

#using the shader
glUseProgram(shader)

#window color
glClearColor(0, 0.1, 0.1, 1)

#for free rotation
glEnable(GL_DEPTH_TEST)

#this is for transparancy
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

#for projection matrix ~~~~ starts here ~~~~~

#4 argument( FOV, Aspect ratio window, Near Clipping pane, far clipping pane)
#copied for eazier window management
# ALSO UPDATED FOR SUPPORTING DA CAMERA?
projection = pyrr.matrix44.create_perspective_projection_matrix(45, WIDTH/HEIGHT, 0.1, 100)

#Translasi here

lemari = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 3, -2]))
pintulemari = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.06, 3, -1.95]))
pintulemari2 = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.55, 3, -1.95]))
keset = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.2, 3, 1]))
jendela = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.2, 4, 1]))

# rotation_matrix = pyrr.matrix44.create_from_x_rotation(np.radians(180))
# new_keset = pyrr.matrix44.multiply(keset, rotation_matrix)
# keset = keset @ rotation_matrix

#~~~~ end here ~~~~~

#rotation for the cube // switched to model because the shader file said
model_loc = glGetUniformLocation(shader, "model")

proj_loc= glGetUniformLocation(shader, "projection")

#adding shader for view matrix
view_loc= glGetUniformLocation(shader, "view")

#for switcher inside the fragment
switcher_loc = glGetUniformLocation(shader, "switcher")

#this one too moved into resize for better window management
glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

# The main application loop
while not glfw.window_should_close(window):
      glfw.poll_events()
      do_movement()

      view = cam.get_view_matrix()
      glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

      glUniform1i(switcher_loc, 0)

      #Declaring the wall
      glBindVertexArray(lemari_VAO)
      glBindTexture(GL_TEXTURE_2D, texture[0])
      glUniformMatrix4fv(model_loc, 1, GL_FALSE, lemari)
      glDrawElements(GL_TRIANGLES, len(indices_lemari), GL_UNSIGNED_INT, None)

      #Declaring the pintulemari
      glBindVertexArray(pintulemari_VAO)
      glBindTexture(GL_TEXTURE_2D, texture[1])
      glUniformMatrix4fv(model_loc, 1, GL_FALSE, pintulemari)
      glDrawElements(GL_TRIANGLES, len(indices_pintulemari), GL_UNSIGNED_INT, None)

      #Declaring the pintulemari
      glBindVertexArray(pintulemari2_VAO)
      glBindTexture(GL_TEXTURE_2D, texture[1])
      glUniformMatrix4fv(model_loc, 1, GL_FALSE, pintulemari2)
      glDrawElements(GL_TRIANGLES, len(indices_pintulemari2), GL_UNSIGNED_INT, None)

      #Declaring the pintulemari
      glBindVertexArray(keset_VAO)
      glBindTexture(GL_TEXTURE_2D, texture[2])
      glUniformMatrix4fv(model_loc, 1, GL_FALSE, keset)
      glDrawElements(GL_TRIANGLES, len(indices_keset), GL_UNSIGNED_INT, None)

      #Declaring the pintulemari
      glBindVertexArray(jendela_VAO)
      glBindTexture(GL_TEXTURE_2D, texture[2])
      glUniformMatrix4fv(model_loc, 1, GL_FALSE, jendela)
      glDrawElements(GL_TRIANGLES, len(indices_jendela), GL_UNSIGNED_INT, None)
      
      
     
      glfw.swap_buffers(window)

# For terminating glfw
glfw.terminate()