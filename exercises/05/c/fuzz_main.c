#include <stdint.h>
#include <string.h>
#include <stdlib.h>

extern char *replaceSpecialCharacters(char *input);

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    char *str = (char *)malloc(sizeof(char) * size + 1);
    memcpy(str, data, size);
    str[size] = '\0';

    replaceSpecialCharacters(str);

    free(str);

    return 0;
}