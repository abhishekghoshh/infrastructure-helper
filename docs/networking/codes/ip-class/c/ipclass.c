#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Returns the class of the IP address as a string (A, B, C, D, E)
const char* getIPClassString(const int ip[4]) {
    int octet0 = ip[0];
    if (octet0 <= 127)
        return "A";
    else if (octet0 <= 191)
        return "B";
    else if (octet0 <= 223)
        return "C";
    else if (octet0 <= 239)
        return "D";
    else
        return "E";
}

// Validates that all IP parts are in the range 0-255
int validateIPParts(const int* parts) {
    if (!parts)
        return 0; // Check for NULL pointer
    for (int i = 0; i < 4; i++) {
        if (parts[i] < 0 || parts[i] > 255)
            return 0;
    }
    return 1;
}

// Parses the IP string into an array of 4 integers. Returns pointer to array or NULL if invalid.
int* constructParts(const char* ip) {
    int n = strlen(ip);
    if (n < 7 || n > 15) {
        return NULL;
    }
    int* parts = (int*)malloc(4 * sizeof(int));
    if (!parts) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < 4; i++) {
        parts[i] = 0;
    }
    int partI = 0;
    int num = 0;
    for (int i = 0; i <= n; i++) {
        if (ip[i] == '.' || ip[i] == '\0') {
            if (partI > 3) {
                free(parts);
                return NULL;
            }
            partI++;
            num = 0;
        } else if (ip[i] >= '0' && ip[i] <= '9') {
            num = ip[i] - '0';
            parts[partI] = parts[partI] * 10 + num;
        } else if (ip[i] != '\0' && partI != 3) {
            free(parts);
            return NULL;
        }
    }
    return parts;
}

// Returns the class of the IP as a string, or NULL if invalid
char* IPClass(const char* ip) {
    int* parts = constructParts(ip);
    if (!validateIPParts(parts)) {
        free(parts);
        return NULL;
    }
    const char* ipClass = getIPClassString(parts);
    free(parts);
    return (char*)ipClass;
}

int main() {
    char ip[20];
    printf("Enter your IP\n");
    scanf("%19s", ip);

    // Get the class of the IP address
    const char* ipClass = IPClass(ip);
    if (!ipClass) {
        printf("Please enter a valid IP\n");
        return 0;
    }
    printf("IP in the class of %s\n", ipClass);
    return 0;
}
