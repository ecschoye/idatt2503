#include <assert.h>
#include <string.h>
#include <stdlib.h>

extern char *replaceSpecialCharacters(char *input);

int main() {
    char *result;

    result = replaceSpecialCharacters("hello");
    assert(strcmp(result, "hello") == 0);
    free(result);

    result = replaceSpecialCharacters("hello&world");
    assert(strcmp(result, "hello&amp;world") == 0);
    free(result);

    result = replaceSpecialCharacters("hello<world");
    assert(strcmp(result, "hello&lt;world") == 0);
    free(result);

    result = replaceSpecialCharacters("hello>world");
    assert(strcmp(result, "hello&gt;world") == 0);
    free(result);

    result = replaceSpecialCharacters("hello&world<>");
    assert(strcmp(result, "hello&amp;world&lt;&gt;") == 0);
    free(result);

    // Negative Cases
    result = replaceSpecialCharacters("hello&");
    assert(strcmp(result, "hello&gt;") != 0); // Should not equal "hello&gt;"
    free(result);

    result = replaceSpecialCharacters("hello<");
    assert(strcmp(result, "hello&gt;") != 0); // Should not equal "hello&gt;"
    free(result);

    result = replaceSpecialCharacters("hello>");
    assert(strcmp(result, "hello&lt;") != 0); // Should not equal "hello&lt;"
    free(result);

    return 0;
}