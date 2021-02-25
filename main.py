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

    def run(self):
        self.read_input(self.input_file_name)
        for key, streets in self.CARS.items():
            self.BEST_CARS_STREET[key] = self.path_length(streets)

        result = sorted(self.BEST_CARS_STREET, key=self.BEST_CARS_STREET.get)

        result_data = {}
        for CAR_ID in result[:1]:
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
