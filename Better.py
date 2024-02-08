#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char charSet[] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
const int charSetLength = sizeof(charSet) - 1;

void nextGuess(char *guess, int *length) {
    int i;
    for (i = 0; i < *length; i++) {
        char *currentCharPtr = strchr(charSet, guess[i]); // Pointer to the current character in the character set.

        int index = currentCharPtr - charSet; // Calculate the index of the current character.
        if (index < charSetLength - 1) {
            guess[i] = charSet[index + 1];
            return;
        } else {
            guess[i] = charSet[0];
        }
    }

    if (*length < 5) {
        guess[*length] = charSet[0];
        (*length)++;
        guess[*length] = '\0';
    } else {
        *length = -1; // If all combinations have been tried, end the loop.
    }
}

int bruteForce(char *password) {
    int length = 1;
    char *guess = (char *)malloc(6);
    guess[0] = charSet[0];
    guess[1] = '\0';

    while (length != -1) {
        if (strcmp(guess, password) == 0) {
            printf("Password found: %s\n", guess);
            free(guess);
            return 1;
        }
        nextGuess(guess, &length);
    }
    free(guess);
    return 0;
}

int main() {
    char password[6];
    printf("Enter the password: ");
    scanf("%5s", password);

    if (!bruteForce(password)) {
        printf("Password not found.\n");
    }

    return 0;
}
