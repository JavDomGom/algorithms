#include <stdio.h>
#include <stdlib.h>
#include <check.h>
#include <unistd.h>
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

START_TEST (test_set_Gx_mod_p)
{
	unsigned long int p = 1999;         // Public prime number.
	unsigned long int secret_a = 47;    // Private.
	
	mpz_t G, G_pow_a, Ga_mod_p;
	mpz_init (G);           // Public.
	mpz_init (G_pow_a);     // Public.
	mpz_init (Ga_mod_p);

	/* Set generator G as unsigned long int. */
	mpz_set_ui(G, 33);

	/* 1. A calculates "G^secret_a mod p" to send to B. */
	set_Gx_mod_p (secret_a, p, G, G_pow_a, Ga_mod_p);

	ck_assert_uint_eq (mpz_get_ui (Ga_mod_p), 1343);

	/* Free memory. */
	mpz_clear (Ga_mod_p);
	mpz_clear (G_pow_a);
	mpz_clear (G);
} END_TEST

START_TEST (test_set_Gxy_mod_p)
{
	unsigned long int p = 1999;         // Public prime number.
	unsigned long int secret_a = 47;    // Private.
	unsigned long int secret_b = 117;   // Private.
	
	mpz_t G, G_pow_a, Ga_mod_p, Ga_pow_b, Gab_mod_p;
	mpz_init (G);           // Public.
	mpz_init (G_pow_a);     // Public.
	mpz_init (Ga_mod_p);
	mpz_init (Ga_pow_b);
	mpz_init (Gab_mod_p);

	/* Set generator G as unsigned long int. */
    mpz_set_ui(G, 33);

	/* 1. A calculates "G^secret_a mod p" to send to B. */
	set_Gx_mod_p (secret_a, p, G, G_pow_a, Ga_mod_p);

	/* 3. B receives "G^a mod p" and calculates "(G^a)^b mod p". */
	set_Gxy_mod_p (Ga_mod_p, secret_b, p, Ga_pow_b, Gab_mod_p);

	ck_assert_uint_eq (mpz_get_ui (Gab_mod_p), 1506);

	/* Free memory. */
	mpz_clear (Gab_mod_p);
	mpz_clear (Ga_pow_b);
	mpz_clear (Ga_mod_p);
	mpz_clear (G_pow_a);
	mpz_clear (G);
} END_TEST

START_TEST (test_set_shared_K)
{
	unsigned long int p = 1999;         // Public prime number.
	unsigned long int secret_a = 47;    // Private.
	unsigned long int secret_b = 117;   // Private.
	
	mpz_t G, G_pow_ab, shared_K;
	mpz_init (G);           // Public.
	mpz_init (G_pow_ab);
    mpz_init (shared_K);

	/* Set generator G as unsigned long int. */
	mpz_set_ui(G, 33);

	/* 5. Shared Key between A and B is "G^(a * b) mod p". */
	set_shared_K (G, secret_a, secret_b, p, G_pow_ab, shared_K);

	ck_assert_uint_eq (mpz_get_ui (shared_K), 1506);

	/* Free memory. */
	mpz_clear (shared_K);
	mpz_clear (G_pow_ab);
	mpz_clear (G);
} END_TEST

Suite *DiffieHellman_algorithm_suite (void)
{
	Suite *s;
	TCase *tc_core;

	s = suite_create ("DiffieHellman algorithm tests");
	tc_core = tcase_create ("test core");

	tcase_add_test (tc_core, test_set_Gx_mod_p);
	tcase_add_test (tc_core, test_set_Gxy_mod_p);
	tcase_add_test (tc_core, test_set_shared_K);
	

	suite_add_tcase (s, tc_core);

	return s;
}

int main (void)
{
	int no_failed = 0;
	SRunner *sr;

	sr = srunner_create (DiffieHellman_algorithm_suite ());

	/* If the log name is set to "-" either via srunner_set_log(),
	the log data will be printed to stdout instead of to a file. */
	srunner_set_log (sr, "-");

	srunner_run_all (sr, CK_NORMAL);

	no_failed = srunner_ntests_failed (sr);

	srunner_free (sr);
	
	return (no_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}