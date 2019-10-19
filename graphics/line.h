#ifndef LINE_H
#define LINE_H

//#define LINE_WIDTH (double) .01

#include "window.h"
#include <math.h>
#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

//All these coordinates are set in World space, so they may be transformed when zooming and panning

// Returns theta in [0, 2pi] such that theta points to (x,y)
double getTanAngle(double y, double x);

class Rectangle {
    public:
        //Defined in a counter clockwise directoin
        Rectangle(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4);
        unsigned int getVAO();
        
    private:
        unsigned int VAO, VBO, EBO;

};

class Line {
    public:
        Line();
        Line(double x1, double y1, double x2, double y2);
        unsigned int getVAO();
        double x1, y1;
        double x2, y2;
    private:
        //Rectangle rect;
        unsigned int VAO;
};

#endif