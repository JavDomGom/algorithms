#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

void printSecret (unsigned long int a, unsigned long int p, mpz_t G)
{
    mpz_t result, mod; // Sets these as GMP Integers.

    /* Initializes G, result and mod variables. */
    mpz_init(result);
    mpz_init(mod);

    mpz_pow_ui(result, G, a); // Set result = G^a.
    mpz_mod_ui(mod, result, p); // Set mod = result % p

    gmp_printf("%Zd\n", mod);

    /* Free memory. */
    mpz_clear(result);
    mpz_clear(mod);
}


int main (int argc, char *argv[])
{
    unsigned long int a = 47;
    unsigned long int b = 117;
    unsigned long int p = 1999;

    mpz_t G;
    mpz_init(G);
    mpz_set_ui(G, 33); // Set unsigned long int to G.
    
    printSecret (a, p, G);
    printSecret (b, p, G);

    mpz_clear(G);

    exit (EXIT_SUCCESS);
}