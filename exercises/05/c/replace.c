#include <string.h>
#include <stdlib.h>
#include "replace.h"

char* replaceSpecialCharacters(char *input) {
    size_t len = strlen(input);
    size_t newLen = len;
    for (size_t i = 0; i < len; ++i) {
        if (input[i] == '&') newLen += 4;
        else if (input[i] == '<' || input[i] == '>') newLen += 3;
    }

    char *output = malloc(newLen + 1);
    if (output == NULL) return NULL;

    size_t j = 0;
    for (size_t i = 0; i < len; ++i) {
        if (input[i] == '&') {
            strcpy(output + j, "&amp;");
            j += 5;
        } else if (input[i] == '<') {
            strcpy(output + j, "&lt;");
            j += 4;
        } else if (input[i] == '>') {
            strcpy(output + j, "&gt;");
            j += 4;
        } else {
            output[j++] = input[i];
        }
    }
    output[newLen] = '\0';
    return output;
}