#include <stdio.h>

int main(int argc, char *argv[]) {
  /*
  The general way to define a struct type is:
  struct tag_name {
   type member1;
   type member2;
  };
  Declare the struct with float members x, y,z
  */
  struct point {
    float x;
    float y;
    float z;
  };

  struct point p1; // define a variable with struct point type
  p1.x = 0.0;      // assign values to its members
  p1.y = 0.2;
  p1.z = 0.4;

  struct point *structptr = &p1;
  printf("x: %.2lf\n", structptr->x);
  return 0;
}
