import datetime as dt


class Writer:
    def __init__(self):
        self.main_list = []
        self.headers = []
        self.sub_headers = []
        self.todo = []
        self.md_path = None
        self.preview = None
        self.header_var = None
        self.sub_header_var = None

    def handler(self):
        pass

    def main(self):
        running = True
        while running:

            user_input = str(input('INPUT: '))
            # print(f'Preview:\n{self.preview}')

            if user_input[:2] == '+h':
                self.header_var = user_input[3:]

            elif user_input[:2] == '+s':
                try:
                    header_index = int(user_input[:4].strip('+s=')) - 1
                    sub_header = user_input[5:]
                except ValueError:
                    header_index = self.headers.index(self.header_var)
                    sub_header = user_input[3:]

            elif user_input[:2] == '+l':
                try:
                    header_index = int(user_input[:6].strip('+l=').split(',')[0]) - 1
                    sub_header_index = int(user_input[:6].strip('+l=').split(',')[1]) - 1
                    todo = user_input[7:]
                except ValueError:
                    sub_header_index = self.sub_header_var
                    todo = user_input[3:]


# current_date = dt.datetime.now().strftime("%Y-%m-%d")
current_date = "2024-06-24"


def md_create():
    def slash_handler(string):
        if '/' in string:
            return f"{string}/"

        elif '\\' in string:
            return f"{string}\\"

    def save_path(path):
        with open('obsidian_folder_path.txt', 'w') as file_write:
            file_write.write(path)

    with open('obsidian_folder_path.txt', 'r') as file_read:
        path_str = file_read.read()
        if len(path_str) == 0:
            path_input = input("Obsidian todo list folder path: ")
            save_path(slash_handler(path_input))
            md_create()
        else:
            path_for_md = path_str
            try:
                with open(f'{path_for_md}{current_date}.md', 'r'):
                    print(f"\nTODO markdown already exists <{path_for_md}{current_date}.md>")

            except FileNotFoundError:
                with open(f'{path_for_md}{current_date}.md', 'w'):
                    print(f'\nTODO markdown for {current_date} is created in\n{path_for_md}')


md_create()
Writer().main()

