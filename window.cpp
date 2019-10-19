// This file contains everything dealing with the window and most things
// dealing with the render process

#include "window.h"
#include "camera.h"

#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#include "shader.h"
#include "model.h"

unsigned int VAO0, VBO0, EBO0; //All should be temporary, but won't be temporary :(
int basicShaderID; 
int WIDTH = 500;
int HEIGHT = 500;
GLFWwindow* window;
extern glm::mat4 view;



void initWindow() {
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3); //Current version is 3.0
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    if (!VIEW_MODE_3D) {
        window = glfwCreateWindow(WIDTH, HEIGHT, "Rendering Engine", NULL, NULL);
    } else {
        window = glfwCreateWindow(2 * WIDTH, HEIGHT, "Rendering Engine", NULL, NULL);
    }
    
    if (window == NULL) {
        std::cout << "Failed to initialize GLFW" << std::endl;
    }
    glfwMakeContextCurrent(window); //Most important instruction that I always forget
    if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress)) {
        std::cout << "Failed to initialize GLAD" << std::endl;
    }

    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED); //Disables the cursor so you dont see it


    glViewport(0, 0, WIDTH, HEIGHT); //Initializes the viewport to this context, split into two during render time for 3D fun!

    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback); //Creates the callback function
    glfwSetCursorPosCallback(window, cam::mouseCallback); //Set mouse callback function
    glEnable(GL_DEPTH_TEST);

    Shader basicShader("src/shaders/basic.vs", "src/shaders/basic.fs");
    basicShaderID = basicShader.ID;


}

//Loops through until escape is pressed and the game is closed
void loop() {
    Shader basicShader("src/shaders/basic.vs", "src/shaders/basic.fs"); //This should not last for a long time hopefully. I hate scoping in C++
    Shader modelShader("src/shaders/testmodel.vs", "src/shaders/testmodel.fs");
    Model testModel("res/geom/monkey.obj");
    Model sphere("res/geom/sphere.obj");
    
    
    while (!glfwWindowShouldClose(window)) {
        glClearColor(.10f, .10f, .10f, 1.0f); //Set background color
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        cam::processInput(window);
        cam::updateCamera();

        //Start of drawing process of the model
        modelShader.use();
        glm::mat4 model = glm::mat4(1.0f);
        model = glm::scale(model,glm::vec3(.5f,.5f,.5f));
        glm::mat4 perspective = glm::mat4(1.0f);
        float fov = 80.0f;
        perspective = glm::perspective(glm::radians(fov), (float) WIDTH / (float) HEIGHT, 0.1f, 100.0f);
        modelShader.setMat4("model", model);  
        modelShader.setMat4("view", view); //extern view
        //perspective = glm::mat4(1.0f);
        perspective = glm::perspective(glm::radians(fov), (float) WIDTH / (float) (HEIGHT), 0.1f, 100.0f);
        modelShader.setMat4("perspective", perspective);
        modelShader.use();
        testModel.Draw(modelShader);

        //This block of code is only here until I'm bored messing around with 3D, it is only temprorary sadly
        if (VIEW_MODE_3D) {
            float amp = .06f;
            glViewport(0, 0, WIDTH/2, HEIGHT); //Left viewport
            modelShader.setMat4("view", cam::left3DViewMat(amp));
            testModel.Draw(modelShader);
            modelShader.setMat4("view", cam::right3DViewMat(amp));
            glViewport(WIDTH / 2, 0, WIDTH/2, HEIGHT);
            testModel.Draw(modelShader);
        }

        //End of drawing process


        //renderObjects(basicShader);

        glfwSwapBuffers(window); //Update Buffers
        glfwPollEvents(); //Watch for events
    }
}

//Binds shaders and renders objects
void renderObjects(Shader s) {
    glBindVertexArray(VAO0);
    s.use();
    //New way of making matrix:
    //glm::mat4 mat = glm::mat4(1.0f)
    glm::mat4 model = glm::mat4(1.0f);
    glm::mat4 perspective = glm::mat4(1.0f);
    //model = glm::rotate(model, (float) glfwGetTime(), glm::vec3(0.0f, 0.0f, 1.0f));
    float fov = 80.0f;
    perspective = glm::perspective(glm::radians(fov), (float) WIDTH / (float) HEIGHT, 0.1f, 100.0f);  

    model = glm::mat4(1.0f); //Temp identity matrices for debugging
    //view = glm::mat4(1.0f);
    //perspective = glm::mat4(1.0f);

    s.setMat4("model", model);
    s.setMat4("view", view);
    s.setMat4("perspective", perspective);

    glm::vec4 v(.5f, .5f, 0.0f, 1.0f);
    v = perspective * view * model * v;
    //std::cout << "(" << v.x << ", " << v.y << ", " << v.z << ", " << v.w << ")" << std::endl;

    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
}

//Where objects are initialized
void initObjects() {
    glGenVertexArrays(1, &VAO0);
    glGenBuffers(1, &VBO0);
    glGenBuffers(1, &EBO0);
    float vertices[] = { .5f, .5f, 0.0f,   -1.0f, -1.0f, //First three are model vertices, last two are texture vertices
                         .5f, -.5f, 0.0f,    -1.0f, 1.0f, //This array should be temporary, even though I know it will not be
                         -.5f, -.5f, 0.0f,    1.0f, -1.0f,
                         -.5f, .5f, 0.0f,     1.0f, 1.0f };
    unsigned int indices[] = {0, 1, 3, 
                              1, 2, 3};

    glUseProgram(basicShaderID);
    glBindVertexArray(VAO0);
    glBindBuffer(GL_ARRAY_BUFFER, VBO0); //Bind the three buffers
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW); //Bind the arrays to the the buffers
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO0);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW); 

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(float), (void*) 0); //(ID, 3 floats, its a float, not normalized, 5 float stride, offset 0)
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(float), (void*) (3 * sizeof(float)));
    glEnableVertexAttribArray(1);

}

//Resize callback function
void framebuffer_size_callback(GLFWwindow* win, int width, int height) {
    glViewport(0, 0, width, height);
    long winl = (long) win; //This line just prevents the warning "win is not used" I don't know if I can safely get rid of win though
    winl += 1;
}