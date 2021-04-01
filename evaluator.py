# 
# MODIFY get_data() AS YOU LIKE.
# DO NOT SEND THIS FILE TO US

import random
random.seed(111)  #remove hash-sign to get randomization seed we will be using at evaluation
#                    (if you fix the seed you get always the same probabilty choice sequence)




def get_data():
	"""Get the initial state of the individuals & the environment"""
	# @TODO: Update this function just for your own testing. We will use our own get_data().
	       #[M, N,   D,   K, LAMBDA, MU,    universal_state]
           
	return [89, 67, 5, 4, 74, 0.47, [[(48, 8), 2, 'notmasked', 'notinfected'], [(28, 60), 2, 'notmasked', 'notinfected'], [(28, 46), 5, 'masked', 'notinfected'], [(20, 28), 7, 'notmasked', 'notinfected'], [(7, 33), 1, 'masked', 'infected'], [(47, 46), 0, 'notmasked', 'infected'], [(38, 75), 3, 'masked', 'notinfected'], [(19, 67), 3, 'notmasked', 'infected'], [(22, 5), 7, 'masked', 'notinfected'], [(15, 28), 6, 'notmasked', 'notinfected'], [(64, 46), 5, 'notmasked', 'notinfected'], [(1, 54), 1, 'notmasked', 'notinfected'], [(54, 5), 4, 'notmasked', 'infected'], [(50, 47), 6, 'masked', 'notinfected'], [(6, 5), 5, 'notmasked', 'infected'], [(51, 40), 3, 'masked', 'infected'], [(53, 11), 6, 'notmasked', 'infected'], [(11, 68), 2, 'masked', 'infected'], [(28, 54), 0, 'masked', 'infected'], [(7, 31), 7, 'notmasked', 'notinfected'], [(31, 19), 0, 'notmasked', 'infected'], [(52, 37), 6, 'notmasked', 'notinfected'], [(12, 82), 3, 'masked', 'notinfected'], [(56, 51), 3, 'masked', 'infected'], [(50, 8), 4, 'masked', 'notinfected'], [(56, 83), 6, 'masked', 'notinfected'], [(14, 83), 1, 'masked', 'notinfected'], [(20, 50), 2, 'notmasked', 'infected'], [(32, 80), 0, 'masked', 'notinfected'], [(24, 15), 2, 'notmasked', 'infected'], [(38, 44), 7, 'masked', 'notinfected'], [(41, 6), 0, 'masked', 'notinfected'], [(13, 88), 4, 'notmasked', 'infected'], [(24, 63), 2, 'masked', 'infected'], [(47, 85), 7, 'notmasked', 'infected'], [(12, 21), 5, 'masked', 'notinfected'], [(30, 30), 0, 'masked', 'notinfected'], [(4, 55), 1, 'masked', 'notinfected'], [(45, 80), 2, 'masked', 'infected'], [(52, 74), 2, 'masked', 'notinfected'], [(64, 57), 0, 'masked', 'infected'], [(45, 33), 3, 'notmasked', 'notinfected'], [(45, 29), 7, 'notmasked', 'infected'], [(53, 22), 7, 'masked', 'infected'], [(58, 38), 5, 'notmasked', 'notinfected'], [(9, 88), 5, 'masked', 'infected'], [(30, 82), 3, 'notmasked', 'notinfected'], [(12, 37), 3, 'masked', 'infected'], [(17, 3), 2, 'masked', 'notinfected'], [(11, 2), 0, 'notmasked', 'infected'], [(53, 19), 3, 'masked', 'notinfected'], [(66, 37), 1, 'masked', 'notinfected'], [(11, 38), 0, 'notmasked', 'infected'], [(2, 72), 4, 'notmasked', 'infected'], [(15, 16), 7, 'masked', 'infected']]]
 






# [50, 100, 5, 80, 30, 0.55, [[(22, 14), 0, 'notmasked', 'notinfected'], [(19, 15), 7, 'notmasked', 'notinfected'], [(17, 16), 7, 'notmasked', 'notinfected'], [(26, 20), 3, 'notmasked', 'infected'], [(22, 21), 5, 'masked', 'infected'], [(25, 21), 3, 'notmasked', 'infected']]] #