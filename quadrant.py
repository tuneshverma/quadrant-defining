def quadrant(x, y, H, W, qua_x, qua_y):

	part_x = int(W/qua_x)
	part_y = int(H/qua_y)

	for i in range(qua_x):
		if x > (part_x*(i)) and x < (part_x*(i+1)):
			print(i+1)

	for j in range(qua_y):
		if y > (part_y*(j)) and y < (part_y*(j+1)):
			print(j+1)

# def main():
# 	quadrant(10, 300, 400, 1000, 2, 2)

# if __name__ == '__main__':
# 	main()
	 