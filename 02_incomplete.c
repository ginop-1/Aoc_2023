#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  int id;
  int red;    // max 12
  int green;  // max 13
  int blue;   // max 14
} gameSet;

bool is_set_valid(gameSet set) {
  if (set.red > 12 || set.green > 13 || set.blue > 14) {
    return false;
  }
  return true;
}

gameSet get_set(char* set_str, int offset, int id) {
  gameSet game;
  game.id = id;
  char* bkp_str = malloc(strlen(set_str) * sizeof(char));
  strcpy(bkp_str, set_str);
  char* sliced = strtok(bkp_str + offset, ",");
  while (sliced != NULL) {
    int num;
    char color[6];
    sscanf(sliced, " %d %s", &num, color);
    if (strcmp("red", color) == 0) {
      game.red = num;
    } else if (strcmp("green", color) == 0) {
      game.green = num;
    } else {
      game.blue = num;
    }
    sliced = strtok(NULL, ",");
  }
  free(bkp_str);
  return game;
}

int process_game(char* line, int id) {
  char* modified_line = malloc(strlen(line) * sizeof(char));
  strcpy(modified_line, line);
  int n_sets = 0;
  int offset;
  while (true) {
    char* set_str = strtok(NULL, ";");
    if (set_str == NULL) {
      break;
    }
    // set_str = strtok(line + strlen(modified_line) + 1, ";");
    // skip Game {5} + n(depends on digits) + :(first part)
    if (n_sets == 0) {
      offset = 5 + id / 10 + 1 + 1;
    } else {
      offset = 0;  // just a space
    }
    n_sets++;
    char* bkp_str = malloc(strlen(set_str) * sizeof(char));
    strcpy(bkp_str, set_str);
    gameSet game = get_set(bkp_str, offset, id);
    if (!is_set_valid(game)) {
      return 0;
    }
    free(bkp_str);
  }
  return id;
}

int main() {
  FILE* f = fopen("input2.txt", "r");
  int result = 0;
  char line[300];
  for (size_t i = 0;; i++) {
    line[0] = -1;
    fgets(line, 300, f);
    if (line[0] == -1) {
      break;
    }
    result += process_game(line, i + 1);
  }
  fclose(f);
  return 0;
}