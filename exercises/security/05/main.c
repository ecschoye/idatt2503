#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "replace.h"


int main() {
    char input[100];
    printf("Enter string: ");
    fgets(input, sizeof(input), stdin);
    input[strlen(input) - 1] = '\0';

    char *output = replaceSpecialCharacters(input);
    if (output != NULL) {
        printf("Output: %s\n", output);
    } else {
        printf("Memory allocation error!\n");
    }

    return 0;
}
