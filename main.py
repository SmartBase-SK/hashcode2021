class Solution:
    def __init__(self) -> None:
        super().__init__()
        self.data = None
        self.input_file_name = './input/main.txt'
        self.output_file_name = 'main.txt'

    def read_input(self, file_name):
        with open(file_name) as f:
            self.data = f.readlines()
            for line in self.data:
                print(line)

    def run(self):
        self.read_input(self.input_file_name)
        with open(self.output_file_name, 'w') as f:
            f.writelines(self.data)


s = Solution()
s.run()
