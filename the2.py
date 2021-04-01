import math
import random
from evaluator import *    
random.seed(111)

DATA = get_data()

def random_move(moves, MU): 

	new_move_list = []
	for i in range(len(moves)):
		if moves[i] == 0:
			move_num = [0,1,2,3,4,5,6,7]
			new_num_list = random.choices(move_num, weights = [(MU)/2.0, (MU)/8.0, (1-MU-(MU*MU))/2.0, 2.0*((MU*MU))/5.0, (MU*MU)/5.0, 2.0*(MU*MU)/5.0, (1-MU-(MU)*(MU))/2.0, (MU)/8.0], k = 1)
			new_move_list.append(new_num_list[0])
		elif moves[i] == 1:
			move_num = [1,2,3,4,5,6,7,0]
			new_num_list = random.choices(move_num, weights = [(MU)/2.0, (MU)/8.0, (1-MU-(MU*MU))/2.0, 2.0*((MU*MU))/5.0, (MU*MU)/5.0, 2.0*(MU*MU)/5.0, (1-MU-(MU)*(MU))/2.0, (MU)/8.0], k = 1)
			new_move_list.append(new_num_list[0])
		elif moves[i] == 2:
			move_num = [2,3,4,5,6,7,0,1]
			new_num_list = random.choices(move_num, weights = [(MU)/2.0, (MU)/8.0, (1-MU-(MU*MU))/2.0, 2.0*((MU*MU))/5.0, (MU*MU)/5.0, 2.0*(MU*MU)/5.0, (1-MU-(MU)*(MU))/2.0, (MU)/8.0], k = 1)
			new_move_list.append(new_num_list[0])
		elif moves[i] == 3:
			move_num = [3,4,5,6,7,0,1,2]
			new_num_list = random.choices(move_num, weights = [(MU)/2.0, (MU)/8.0, (1-MU-(MU*MU))/2.0, 2.0*((MU*MU))/5.0, (MU*MU)/5.0, 2.0*(MU*MU)/5.0, (1-MU-(MU)*(MU))/2.0, (MU)/8.0], k = 1)
			new_move_list.append(new_num_list[0])
		elif moves[i] == 4:
			move_num = [4,5,6,7,0,1,2,3]
			new_num_list = random.choices(move_num, weights = [(MU)/2.0, (MU)/8.0, (1-MU-(MU*MU))/2.0, 2.0*((MU*MU))/5.0, (MU*MU)/5.0, 2.0*(MU*MU)/5.0, (1-MU-(MU)*(MU))/2.0, (MU)/8.0], k = 1)
			new_move_list.append(new_num_list[0])
		elif moves[i] == 5:
			move_num = [5,6,7,0,1,2,3,4]
			new_num_list = random.choices(move_num, weights = [(MU)/2.0, (MU)/8.0, (1-MU-(MU*MU))/2.0, 2.0*((MU*MU))/5.0, (MU*MU)/5.0, 2.0*(MU*MU)/5.0, (1-MU-(MU)*(MU))/2.0, (MU)/8.0], k = 1)
			new_move_list.append(new_num_list[0])
		elif moves[i] == 6:
			move_num = [6,7,0,1,2,3,4,5]
			new_num_list = random.choices(move_num, weights = [(MU)/2.0, (MU)/8.0, (1-MU-(MU*MU))/2.0, 2.0*((MU*MU))/5.0, (MU*MU)/5.0, 2.0*(MU*MU)/5.0, (1-MU-(MU)*(MU))/2.0, (MU)/8.0], k = 1)
			new_move_list.append(new_num_list[0])
		elif moves[i] == 7:
			move_num = [7,0,1,2,3,4,5,6]
			new_num_list = random.choices(move_num, weights = [(MU)/2.0, (MU)/8.0, (1-MU-(MU*MU))/2.0, 2.0*((MU*MU))/5.0, (MU*MU)/5.0, 2.0*(MU*MU)/5.0, (1-MU-(MU)*(MU))/2.0, (MU)/8.0], k = 1)
			new_move_list.append(new_num_list[0])

	return new_move_list

def coordinate_finder(coordinate, new_move_list, M, N, index, coordinates): 
    
    for i in range(len(new_move_list)):
        
        
        if (new_move_list[index] == 0) and (coordinate[1] < (M-1)):
            new_coordinate = (coordinate[0], coordinate[1] + 1)
        elif (new_move_list[index] == 1) and (coordinate[0] > 0) and (coordinate[1] < (M-1)):
            new_coordinate = (coordinate[0] -1 , coordinate[1] + 1)
        elif (new_move_list[index] == 2) and (coordinate[0] > 0):
            new_coordinate = (coordinate[0] -1 , coordinate[1])
        elif (new_move_list[index] == 3) and (coordinate[0] > 0) and (coordinate[1] > 0):
            new_coordinate = (coordinate[0] -1 , coordinate[1] - 1)
        elif (new_move_list[index] == 4) and (coordinate[1] > 0):
            new_coordinate = (coordinate[0]  , coordinate[1] - 1)
        elif (new_move_list[index] == 5) and (coordinate[0] < (N-1)) and (coordinate[1] > 0):
            new_coordinate = (coordinate[0] +1 , coordinate[1] - 1)
        elif (new_move_list[index] == 6) and (coordinate[0] < (N-1)):
            new_coordinate = (coordinate[0] +1 , coordinate[1])
        elif (new_move_list[index] == 7) and (coordinate[0] < (N-1)) and (coordinate[1] < (M-1)):
            new_coordinate = (coordinate[0] +1 , coordinate[1] + 1) 
        else :
            new_coordinate = (coordinate[0], coordinate[1])

    for i in range(len(coordinates)):
        if (coordinates[i] == new_coordinate):
            return coordinate
	
    return new_coordinate

def random_infection(infection_status, LAMBDA, distance, i, j, KAPPA, mask_status):
    infection_list = ["infected","notinfected"]
    temp_infection_status = infection_status.copy()
    
    
    if mask_status[i] == 'masked' and mask_status[j] == 'masked':
        prob = min(1.0, KAPPA/((distance)*(distance)))
        prob = prob / (LAMBDA*LAMBDA)
    elif mask_status[i] == 'masked' and mask_status[j] == 'notmasked':
        prob = min(1.0, KAPPA/((distance)*(distance)))
        prob = prob / LAMBDA
    elif mask_status[i] == 'notmasked' and mask_status[j] == 'masked':
        prob = min(1.0, (KAPPA)/((distance)*(distance)))
        prob = prob / LAMBDA
    else:
        prob = min(1.0,KAPPA/((distance)*(distance)))       

    if infection_status[i] == 'infected':
        temp_infection_status[j] = random.choices(infection_list, weights = [prob, 1-prob], k = 1)[0]
    elif infection_status[j] == 'infected':
        temp_infection_status[i] = random.choices(infection_list, weights = [prob, 1-prob], k = 1)[0]
	
    return temp_infection_status

def new_infection_status(coordinates, indi_num, D, infection_status, mask_status, KAPPA, LAMBDA):

    temp_infection_status = infection_status.copy()
    indi = -1
    indj = -1
    for i in range(indi_num):
        checkInfi = []
        for j in range(i+1, indi_num):
            checkInfj = []
            distance = math.sqrt((coordinates[i][0] - coordinates[j][0])*(coordinates[i][0] - coordinates[j][0]) + (coordinates[i][1] - coordinates[j][1])*(coordinates[i][1] - coordinates[j][1]))
            if distance <= D  and infection_status[i] != infection_status[j]:
                if infection_status[i] == 'infected':
                    a = random_infection(infection_status, LAMBDA, distance, i, j, KAPPA, mask_status)
                    checkInfj.append(a[j])
                    indj = j
                else:
                    a = random_infection(infection_status, LAMBDA, distance, i, j, KAPPA, mask_status)
                    checkInfi.append(a[i])
                    indi = i
            if 'infected' in checkInfj:
                temp_infection_status[indj] = 'infected'
        if 'infected' in checkInfi:
            temp_infection_status[indi] = 'infected'


    return temp_infection_status


def new_move():
	# write here your definition. You can also define helper functions
	
	[M,N,D,KAPPA] = DATA[:4]
	LAMBDA = float(DATA[4])
	MU = float(DATA[5])
	universal_state = DATA[6]
	indi_num = len(universal_state)
	moves = []
	temp_moves = []
	
	mask_status = []
	infection_status =[]
	
	coordinates = []
	temp_coordinates = []
	
	
	

	for i in range(len(universal_state)):
		move = universal_state[i][1]
		moves.append(move)
		
	for i in range(len(universal_state)):
		temp_move = universal_state[i][1]
		temp_moves.append(temp_move)

	for i in range(indi_num):
		coordinate = universal_state[i][0]
		coordinates.append(coordinate)

	for i in range(indi_num):
		temp_coordinate = universal_state[i][0]
		temp_coordinates.append(temp_coordinate)

	for i in range(indi_num):
		mask = universal_state[i][2]
		if mask == 'masked':
			mask_status.append("masked")
		else:
			mask_status.append("notmasked")	

	for i in range(indi_num):
		infection = universal_state[i][3]
		if infection == 'infected':
			infection_status.append("infected")
		else:
			infection_status.append("notinfected")

	

	moves = random_move(moves, MU)
	
	for i in range(indi_num):
	    coordinates[i] = coordinate_finder(coordinates[i], moves, M, N, i, coordinates)

	for i in range(indi_num):
		if coordinates[i] == temp_coordinates[i]:
			moves[i] = temp_moves[i]

	infection_status = new_infection_status(coordinates, indi_num, D, infection_status, mask_status, KAPPA, LAMBDA)

	
	for i in range(indi_num):
		universal_state[i][0] = coordinates[i]
		universal_state[i][1] = moves[i]
		universal_state[i][2] = mask_status[i]
		universal_state[i][3] = infection_status[i]


	return universal_state 
