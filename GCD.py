#Two files have been modified
#include <stdio.h>

int main() {
	printf("hello git");
}


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(91, 35))
