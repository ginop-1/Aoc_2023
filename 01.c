#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  char* key;
  int value;
} str_int_map;

str_int_map numbers_map[9] = {{"one", 1},   {"two", 2},   {"three", 3},
                              {"four", 4},  {"five", 5},  {"six", 6},
                              {"seven", 7}, {"eight", 8}, {"nine", 9}};

int is_number(char input) {
  // return -1 if nan
  int num = input - 48;      // convert 'n' to n (char to int)
  if (num < 0 || num > 9) {  // not a number
    return -1;
  }
  return num;
}

void process_int(char* line, int* first, int* last) {
  int local_first = 10e6;
  int local_last = -1;
  for (size_t i = 0; line[i] != '\n'; i++) {
    int num = is_number(line[i]);
    if (num != -1) {
      if (local_first == 10e6) {
        local_first = i;
      }
      local_last = i;
    }
  }
  *first = local_first;
  *last = local_last;
}

void process_str(char* line, int* first, int* last) {
  char buffer;
  int first_occurency[9];
  int last_occurency[9];
  for (size_t i = 0; i < 9; i++) {
    first_occurency[i] = -1;
    last_occurency[i] = -1;
  }
  for (size_t i = 0; i < 9; i++) {
    int position = -1;
    const char* tmp = line;
    while (tmp = strstr(tmp, numbers_map[i].key)) {
      if (first_occurency[i] == -1) {
        first_occurency[i] = tmp - line;
      }
      last_occurency[i] = tmp - line;
      tmp++;
    }
  }
  // return the number
  int min_index = 10e5;
  int max_index = -1;
  for (int i = 0; i < 9; i++) {
    if (first_occurency[i] != -1 && first_occurency[i] < min_index) {
      min_index = first_occurency[i];
    }
    if (last_occurency[i] != -1 && last_occurency[i] > max_index) {
      max_index = last_occurency[i];
    }
  }
  *first = min_index;
  *last = max_index;
}

int strnum_to_int(char* str, int start_pos) {
  for (size_t i = 0; i < 9; i++) {
    int position = -1;
    const char* tmp = str;
    while (tmp = strstr(tmp, numbers_map[i].key)) {
      position = tmp - str;
      if (position == start_pos) {
        return numbers_map[i].value;
      }
      tmp++;
    }
  }
}

int main() {
  FILE* f = fopen("input.txt", "r");
  int res = 0;
  int first_int_ix, last_int_ix;
  int first_str_ix, last_str_ix;
  int first, last;
  while (true) {
    char line[200];
    fgets(line, 200, f);
    if (line[0] == -1) {
      break;
    }
    process_int(line, &first_int_ix, &last_int_ix);
    process_str(line, &first_str_ix, &last_str_ix);
    if (first_int_ix < first_str_ix) {
      first = is_number(line[first_int_ix]) * 10;
    } else {
      first = strnum_to_int(line, first_str_ix) * 10;
    }
    if (last_int_ix > last_str_ix) {
      last = is_number(line[last_int_ix]);
    } else {
      last = strnum_to_int(line, last_str_ix);
    }
    res += first + last;
    line[0] = -1;
  }
  fclose(f);
  printf("%d", res);
  return 0;
}