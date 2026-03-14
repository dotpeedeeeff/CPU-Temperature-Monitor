import psutil


def get_temps():
    temps = psutil.sensors_temperatures()

    cores = temps["coretemp"]
    cores = cores[1:]

    core_list = []

    for tuple in cores:
        core_temp = tuple[1]
        core_list.append(core_temp)

    return core_list
