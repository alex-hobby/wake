import matplotlib.pyplot as plt


def main():
	f = open("alpha_and_other.txt", "r")

	tt = []
	ff = []

	sleep = []

	time_start_sleep = 100000000
	time_delay = 5
	maybe_sleeping = False
	alpha_boundary = 15

	for line in f:
		space = line.find(" ")
		line = line[:space+1] + line[space+2:-2]
		line = line[:space] + "," + line[space:]
		sp = line.split(", ")

		time = float(sp[0])
		sp = sp[1:]
		sp = [float(i) for i in sp]
		max_f = max(sp)

		tt.append(time)
		ff.append(max_f)

		sleep_num = 0

		if max_f > alpha_boundary:
			maybe_sleeping = False
			sleep_num = 50
		elif max_f < alpha_boundary and maybe_sleeping == False:
			maybe_sleeping = True
			time_start_sleep = time
			sleep_num = 50
		elif max_f < alpha_boundary and maybe_sleeping == True and time - time_start_sleep > time_delay:
			sleep_num = 120
		else:
			sleep_num = 50

		sleep.append(sleep_num)


		# for plotting every single datapoint
		# time_arr = [time] * len(sp)

		# tt.append(time_arr)
		# ff.append(sp)

	plt.scatter(tt, ff)
	plt.scatter(tt, sleep)
	plt.show()


if __name__ == '__main__':
	main()