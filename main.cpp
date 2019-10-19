#include <iostream>
#include <vector>
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#include "graphics/window.h"



/*
* Restarting from scratch on OpenGL, this time I'm trying to render a model from Blender
* Started 2018-11-05
*/

//Main function hidden away in sadness
int main() {
    initWindow();
    initObjects();
    loop();
    return 0;
}