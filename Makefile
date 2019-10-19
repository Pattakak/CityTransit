all:
	gcc -P -g *.cpp graphics/glad.c graphics/*.cpp -o transit -lglfw3 -lGL -lX11 -lXi -lXrandr -lXxf86vm -lXinerama -lXcursor -lrt -lm -lassimp -lpthread -ldl -lstdc++
