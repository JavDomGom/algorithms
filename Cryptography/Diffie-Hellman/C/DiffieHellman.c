#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

void set_Gx_mod_p (unsigned long int secret_x, unsigned long int p, mpz_t G, mpz_t G_pow_x, mpz_t Gx_mod_p)
{
    mpz_pow_ui (G_pow_x, G, secret_x);  // Set G_pow_x = G^secret_x.
    mpz_mod_ui (Gx_mod_p, G_pow_x, p);  // Set Gx_mod_p = G_pow_x % p.
}

void set_Gxy_mod_p (mpz_t Gy_mod_p, unsigned long int secret_x, unsigned long int p, mpz_t Gx_pow_y, mpz_t Gxy_mod_p)
{
    mpz_pow_ui (Gx_pow_y, Gy_mod_p, secret_x);  // Set Gx_pow_y = Gy_mod_p^secret_x.
    mpz_mod_ui (Gxy_mod_p, Gx_pow_y, p);        // Set Gxy_mod_p = Gx_pow_y % p.
}

void set_shared_K (mpz_t G, unsigned long int secret_x, unsigned long int secret_y, unsigned long int p, mpz_t G_pow_xy, mpz_t shared_K)
{
    mpz_pow_ui (G_pow_xy, G, (secret_x * secret_y));    // Set G_pow_xy = G^(secret_x * secret_y)
    mpz_mod_ui (shared_K, G_pow_xy, p);                 // Set shared_K = G_pow_xy % p.
}

int main (int argc, char *argv[])
{
    unsigned long int p = 1999;         // Public prime number.
    unsigned long int secret_a = 47;    // Private.
    unsigned long int secret_b = 117;   // Private.

    /* Sets these as GMP Integers. */
    mpz_t G, G_pow_a, G_pow_b, Ga_mod_p, Gb_mod_p, Ga_pow_b, Gb_pow_a, Gab_mod_p, Gba_mod_p, G_pow_ab, shared_K;

    /* Initializes variables. */
    mpz_init (G);           // Public.
    mpz_init (G_pow_a);     // Public.
    mpz_init (G_pow_b);     // Public.
    mpz_init (Ga_mod_p);
    mpz_init (Gb_mod_p);
    mpz_init (Ga_pow_b);
    mpz_init (Gb_pow_a);
    mpz_init (Gab_mod_p);
    mpz_init (Gba_mod_p);
    mpz_init (G_pow_ab);
    mpz_init (shared_K);

    /* Set generator G as unsigned long int. */
    mpz_set_ui(G, 33);
    
    /* 1. A calculates "G^secret_a mod p" to send to B. */
    set_Gx_mod_p (secret_a, p, G, G_pow_a, Ga_mod_p);

    /* 2. B calculates "G^secret_b mod p" to send to A. */
    set_Gx_mod_p (secret_b, p, G, G_pow_b, Gb_mod_p);
    
    /* 3. B receives "G^a mod p" and calculates "(G^a)^b mod p". */
    set_Gxy_mod_p (Ga_mod_p, secret_b, p, Ga_pow_b, Gab_mod_p);

    /* 4. A receives "G^b mod p" and calculates "(G^b)^a mod p". */
    set_Gxy_mod_p (Gb_mod_p, secret_a, p, Gb_pow_a, Gba_mod_p);

    /* 5. Shared Key between A and B is "G^(a * b) mod p". */
    set_shared_K (G, secret_a, secret_b, p, G_pow_ab, shared_K);

    gmp_printf ("Gab_mod_p:\t%Zd\n", Gab_mod_p);
    gmp_printf ("Gba_mod_p:\t%Zd\n", Gba_mod_p);
    gmp_printf ("shared_K:\t%Zd\n", shared_K);

    /* Free memory. */
    mpz_clear (shared_K);
    mpz_clear (G_pow_ab);
    mpz_clear (Gba_mod_p);
    mpz_clear (Gab_mod_p);
    mpz_clear (Gb_pow_a);
    mpz_clear (Ga_pow_b);
    mpz_clear (Gb_mod_p);
    mpz_clear (Ga_mod_p);
    mpz_clear (G_pow_b);
    mpz_clear (G_pow_a);
    mpz_clear (G);

    exit (EXIT_SUCCESS);
}