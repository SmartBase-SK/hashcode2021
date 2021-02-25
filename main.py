class Solution:
    def __init__(self) -> None:
        super().__init__()
        self.data = None
        self.input_file_name = './input/a.txt'
        self.output_file_name = 'main.txt'
        self.STREETS = {}
        self.CARS = {}
        self.STREETS_LENS = {}
        self.DURATION = None
        self.NUM_INTER = None
        self.NUM_STREETS = None
        self.NUM_CARS = None
        self.BONUS = None
        self.BEST_CARS_STREET = {}
        self.used_streets_by_cars = set()

    def read_input(self, file_name):
        with open(file_name) as f:
            self.data = [i.strip() for i in f.readlines()]
            line_num = 0
            self.DURATION, self.NUM_INTER, self.NUM_STREETS, self.NUM_CARS, self.BONUS = map(int, self.data[0].split(' '))
            for _ in range(self.NUM_STREETS):
                line_num += 1
                line = self.data[line_num]
                START, END, NAME, LEN = line.split(' ')
                self.STREETS[NAME] = {'start': int(START), 'end': int(END), 'len': int(LEN)}
                self.STREETS_LENS[NAME] = int(LEN)

            for i in range(self.NUM_CARS):
                line_num += 1
                line = self.data[line_num]
                CAR_STREETS = line.split(' ')[1:]
                self.CARS[i] = list(CAR_STREETS)

    def path_length(self, path):
        path_score = 0
        for street in path[1:]:
            path_score += 1 + self.STREETS_LENS[street]
        return path_score
    
    def pop_unused_streets(self):
        all_streets = set(street_name for street_name in self.STREETS)
        streets_to_remove = all_streets - self.used_streets_by_cars
        print(f'removing streets {len(streets_to_remove)}')
        for street_name in streets_to_remove:
            self.STREETS_LENS.pop(street_name)
            self.STREETS.pop(street_name)

    def run(self):
        self.read_input(self.input_file_name)
        for key, streets in self.CARS.items():
            self.used_streets_by_cars.update(streets)
            path_length = self.path_length(streets)
            if path_length <= self.DURATION:
                self.BEST_CARS_STREET[key] = path_length

        result = sorted(self.BEST_CARS_STREET, key=self.BEST_CARS_STREET.get)

        self.pop_unused_streets()

        # state = {}
        # for time in enumerate(self.DURATION):


        result_data = {}
        for CAR_ID in result:
            STREETS_TO_GO = self.CARS[CAR_ID]
            for STREET in STREETS_TO_GO:
                street = self.STREETS[STREET]
                result_data[street['end']] = {STREET: 1}

        result_lines = []
        result_lines.append(str(len(result_data)))
        for intersection_id, streets in result_data.items():
            result_lines.append(str(intersection_id))
            result_lines.append(str(len(streets)))
            for street_name, seconds in streets.items():
                result_lines.append(f'{street_name} {seconds}')
        with open(self.output_file_name, 'w') as f:
            f.writelines('\n'.join(result_lines))


s = Solution()
s.run()
