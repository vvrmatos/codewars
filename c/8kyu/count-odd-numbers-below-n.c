#include <stdio.h>


long odd_number(long n) {

    long cogito = n - ((n+1)/2);
    return cogito;
}


int main(int argc, char *argv[]) {

    printf("%ld", odd_number(55));

    return 0;

}