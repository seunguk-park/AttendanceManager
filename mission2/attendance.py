from grade import GradeFactory
from weekday import WeekdayFactory


class AttendanceManager:
    def __init__(self):
        self.player_id_list = {}
        self.id_count = 0

        # attendance_point_rawdata[사용자ID][요일]
        self.attendance_point_rawdata = [[0] * 100 for _ in range(100)]
        self.total_points = [0] * 100
        self.grade = [0] * 100
        self.names = [''] * 100
        self.training_attendance_count = [0] * 100
        self.weekend_attendance_count = [0] * 100

        self.point_table = []
        self.point_table.append(WeekdayFactory.create_weekday("monday"))
        self.point_table.append(WeekdayFactory.create_weekday("tuesday"))
        self.point_table.append(WeekdayFactory.create_weekday("wednesday"))
        self.point_table.append(WeekdayFactory.create_weekday("thursday"))
        self.point_table.append(WeekdayFactory.create_weekday("friday"))
        self.point_table.append(WeekdayFactory.create_weekday("saturday"))
        self.point_table.append(WeekdayFactory.create_weekday("sunday"))

        self.grade_table = []
        self.grade_table.append(GradeFactory.create_grade("GOLD"))
        self.grade_table.append(GradeFactory.create_grade("SILVER"))
        self.grade_table.append(GradeFactory.create_grade("NORMAL"))


    def process_input_data(self, input_name, input_day_of_the_week):
        if input_name not in self.player_id_list:
            self.add_new_player(input_name)

        curr_player_id = self.player_id_list[input_name]
        self.calculate_points(curr_player_id, input_day_of_the_week)


    def calculate_points(self, curr_player_id, input_day_of_the_week):
        add_point = 0
        day_of_the_week_index = 0
        for x in self.point_table:
            if input_day_of_the_week == x.day_of_the_week:
                day_of_the_week_index = x.index
                add_point += x.point
                if x.is_training_day:
                    self.training_attendance_count[curr_player_id] += 1
                if x.is_weekend:
                    self.weekend_attendance_count[curr_player_id] += 1
                break

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
        self.grade_table.sort(key=lambda x: -x.cut_line)
        for i in range(1, self.id_count + 1):
            for x in self.grade_table:
                if self.total_points[i] >= x.cut_line:
                    self.grade[i] = x.key
                    break

    def print_points_and_grade(self):
        #self.grade_table.sort(key=lambda x: x.key)
        for i in range(1, self.id_count + 1):
            print(f"NAME : {self.names[i]}, POINT : {self.total_points[i]}, GRADE : ", end="")
            for x in self.grade_table:
                if self.grade[i] == x.key:
                    print(x.name)


    def print_removed_player(self):
        print("\nRemoved player")
        print("==============")
        for i in range(1, self.id_count + 1):
            if self.grade[i] not in (1, 2) and self.training_attendance_count[i] == 0 and self.weekend_attendance_count[i] == 0:
                print(self.names[i])


if __name__ == "__main__":
    attendance_manager = AttendanceManager()
    attendance_manager.input_file("attendance_weekday_500.txt")
    attendance_manager.add_bonus_point()
    attendance_manager.update_grade()
    attendance_manager.print_points_and_grade()
    attendance_manager.print_removed_player()
