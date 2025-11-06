#==============================================================================
# --- Day 14: Reindeer Olympics ---
#==============================================================================

TIME = 2503

class Reinder:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time

    def run(self, time):
        cycle_time = self.fly_time + self.rest_time
        distance = 0
        if cycle_time > 0:
            nb_cycles = time // cycle_time
            distance += self.speed * self.fly_time * nb_cycles
            distance += self.speed * min(self.fly_time, time % cycle_time)
        return distance


def run():
    print("--- Day 14: Reindeer Olympics ---")
    puzzle = open("puzzle.txt", 'r')
    reinders = []
    for line in puzzle:
        datas = line.strip().split()
        reinders.append(Reinder(datas[0], int(datas[3]), int(datas[6]), int(datas[13])))
    puzzle.close()

    max_distance = 0
    for reinder in reinders:
        distance = reinder.run(TIME)
        if distance > max_distance:
            max_distance = distance
    print(f"1ère partie : Distance maximale parcourue par le vainqueur = {max_distance}")

    ranking = dict()
    for reinder in reinders:
        ranking[reinder.name] = 0
    for time in range(1, TIME + 1):
        distances = dict()
        max_distance = 0
        for reinder in reinders:
            distance = reinder.run(time)
            if distance > max_distance:
                max_distance = distance
            distances[reinder.name] = distance
        for rec in distances:
            if distances[rec] == max_distance:
                ranking[rec] += 1
    max_point = 0
    for rec in ranking:
        if ranking[rec] > max_point:
            max_point = ranking[rec]
    print(f"2ème partie : Nombre de points du ou des vainqueurs = {max_point}")


if __name__ == "__main__":
    run()
