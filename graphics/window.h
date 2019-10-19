#ifndef WINDOW_H
#define WINDOW_H

// Constant for 3 dimentional or not, 0 means not 3D
#define VIEW_MODE_3D 0


#include "shader.h"
#include <glad/glad.h>
#include <GLFW/glfw3.h>

void initWindow();
void loop();
void renderObjects(Shader s);
void initObjects();
void framebuffer_size_callback(GLFWwindow* win, int width, int height);


#endif