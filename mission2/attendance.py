


class AttendanceManager:
    def __init__(self):
        self.player_id_list = {}
        self.id_count = 0

        # attendance_point_rawdata[사용자ID][요일]
        self.attendance_point_rawdata = [[0] * 100 for _ in range(100)]
        self.total_points = [0] * 100
        self.grade = [0] * 100
        self.names = [''] * 100
        self.wednesday_attendance_count = [0] * 100
        self.weekend_attendance_count = [0] * 100

    def process_input_data(self, input_name, input_day_of_the_week):
        if input_name not in self.player_id_list:
            self.add_new_player(input_name)

        curr_player_id = self.player_id_list[input_name]
        self.calculate_points(curr_player_id, input_day_of_the_week)


    def calculate_points(self, curr_player_id, input_day_of_the_week):
        add_point = 0
        day_of_the_week_index = 0
        if input_day_of_the_week == "monday":
            day_of_the_week_index = 0
            add_point += 1
        elif input_day_of_the_week == "tuesday":
            day_of_the_week_index = 1
            add_point += 1
        elif input_day_of_the_week == "wednesday":
            day_of_the_week_index = 2
            add_point += 3
            self.wednesday_attendance_count[curr_player_id] += 1
        elif input_day_of_the_week == "thursday":
            day_of_the_week_index = 3
            add_point += 1
        elif input_day_of_the_week == "friday":
            day_of_the_week_index = 4
            add_point += 1
        elif input_day_of_the_week == "saturday":
            day_of_the_week_index = 5
            add_point += 2
            self.weekend_attendance_count[curr_player_id] += 1
        elif input_day_of_the_week == "sunday":
            day_of_the_week_index = 6
            add_point += 2
            self.weekend_attendance_count[curr_player_id] += 1
        self.attendance_point_rawdata[curr_player_id][day_of_the_week_index] += 1
        self.total_points[curr_player_id] += add_point


    def add_new_player(self, input_name):
        self.id_count += 1
        self.player_id_list[input_name] = self.id_count
        self.names[self.id_count] = input_name


    def input_file(self, file_name):
        try:
            with open(file_name, encoding='utf-8') as f:
                for _ in range(500):
                    line = f.readline()
                    if not line:
                        break
                    parts = line.strip().split()
                    if len(parts) == 2:
                        self.process_input_data(parts[0], parts[1])
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")


    def add_bonus_point(self):
        for i in range(1, self.id_count + 1):
            if self.attendance_point_rawdata[i][2] > 9:
                self.total_points[i] += 10
            if self.attendance_point_rawdata[i][5] + self.attendance_point_rawdata[i][6] > 9:
                self.total_points[i] += 10


    def update_grade(self):
        for i in range(1, self.id_count + 1):
            if self.total_points[i] >= 50:
                self.grade[i] = 1
            elif self.total_points[i] >= 30:
                self.grade[i] = 2
            else:
                self.grade[i] = 0


    def print_points_and_grade(self):
        for i in range(1, self.id_count + 1):
            print(f"NAME : {self.names[i]}, POINT : {self.total_points[i]}, GRADE : ", end="")
            if self.grade[i] == 1:
                print("GOLD")
            elif self.grade[i] == 2:
                print("SILVER")
            else:
                print("NORMAL")


    def print_removed_player(self):
        print("\nRemoved player")
        print("==============")
        for i in range(1, self.id_count + 1):
            if self.grade[i] not in (1, 2) and self.wednesday_attendance_count[i] == 0 and self.weekend_attendance_count[i] == 0:
                print(self.names[i])


if __name__ == "__main__":
    attendance_manager = AttendanceManager()
    attendance_manager.input_file("attendance_weekday_500.txt")
    attendance_manager.add_bonus_point()
    attendance_manager.update_grade()
    attendance_manager.print_points_and_grade()
    attendance_manager.print_removed_player()
