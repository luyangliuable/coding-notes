#include <stdio.h>

// Write your code below
struct Table {
  int length;
  int width;
  int height;
  char color[20];
};

int main(void) {
  int table1Length = 24;
  int table1Width = 24;
  int table1Height = 20;
  char table1Color[20] = "Dark Brown";

  int table2Length = 42;
  int table2Width = 18;
  int table2Height = 32;
  char table2Color[20] = "Matte Black";

  // Write your code below
  struct Table table1 = {24, 24, 20, "Dark Brown"};

  struct Table table2 = {42, 18, 32, "Matte Black"};
}
