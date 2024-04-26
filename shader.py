def shader_function():
    vertex_shader = """
    #version 330 core
    layout (location = 0) in vec3 aPos;
    layout (location = 1) in vec2 aTexCoord;

    out vec2 TexCoord;

    uniform mat4 model;
    uniform mat4 view;
    uniform mat4 projection;

    void main()
    {
        gl_Position = projection * view * model * vec4(aPos, 1.0);
        TexCoord = aTexCoord;
    }
    """

    fragment_shader = """
    #version 330 core
    out vec4 FragColor;
    in vec2 TexCoord;

    uniform sampler2D texture1;

    uniform int switcher;

    void main()
    {
        if (switcher == 0)
            FragColor = texture(texture1, TexCoord);
        else
            FragColor = vec4(0.5f, 0.2f, 0.8f, 1.0f);
    }
    """

    return vertex_shader, fragment_shader
