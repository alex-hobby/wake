from pylsl import StreamInlet, resolve_stream





def main():
    time_start_sleep = 0
    time_delay = 3
    maybe_sleeping = False
    alpha_boundary = 16

    sampling_every = 10
    sample_count = 0

    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    print("found stream")
    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, time = inlet.pull_sample()

        sample_count += 1
        if sample_count % sampling_every != 0:
            continue
        else:
            sample_count = 0


        time = float(time)
        sample = [float(i) for i in sample]
        max_f = max(sample)

        asleep = False

        if max_f > alpha_boundary:
            maybe_sleeping = False
            asleep = False
        elif max_f < alpha_boundary and not maybe_sleeping:
            maybe_sleeping = True
            time_start_sleep = time
            asleep = False
        elif max_f < alpha_boundary and maybe_sleeping and time - time_start_sleep > time_delay:
            asleep = True
        else:
            asleep = False

        if asleep:
            print("Asleep!" + str(max_f))
        else:
            print("Awake!"  + str(max_f))

if __name__ == '__main__':
    main()