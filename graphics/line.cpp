#include "line.h"
#include "window.h"


double getTanAngle(double y, double x) {
    if (x == 0 && y == 0) return 0;
    if (x == 0 && y > 0) return 0;
    if (x == 0 && y < 0) return M_PI;
    if (y > 0) return atan(y/x);
    if (y < 0) return M_PI / 2 + atan(y/x);
    return 0;
}


Rectangle::Rectangle(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4) {
    float vertices[] = {x1, y1, 0.0f, 
                                x2, y2, 0.0f,
                                x3, y3, 0.0f,
                                x4, y4, 0.0f};
    unsigned int indices[] = {0, 1, 3, 
                                      1, 2, 3}; 
    
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);
            
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO); //Bind the three buffers
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW); //Bind the arrays to the the buffers
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW); 

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*) 0); //(ID, 3 floats, its a float, not normalized, 5 float stride, offset 0)
    glEnableVertexAttribArray(0);
}
unsigned int Rectangle::getVAO() {
            return VAO;
        }




Line::Line(double x1, double y1, double x2, double y2) {
            this->x1 = x1;
            this->y1 = y1;
            this->x2 = x2;
            this->y2 = y2;


            double theta = getTanAngle((y2-y1), (x2-x1));
            double xShift = .01 * cos(theta);
            double yShift = .01 * sin(theta);
            Rectangle rect = Rectangle(x1 + xShift, y1 + yShift, x1 - xShift, y1 - yShift, x2 - xShift, y2 - yShift, x2 + xShift, y2 + yShift);

            VAO = rect.getVAO();
        }
Line::Line() {
            Line(0, 0, 0, 0);
        }
unsigned int Line::getVAO() {
            return VAO;
        }