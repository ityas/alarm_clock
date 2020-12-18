from PyQt5 import QtWidgets
from GUI.exit_alarm_tool import Ui_MainWindow
import help_file


class WinOfNotice(QtWidgets.QMainWindow):
    def __init__(self):
        super(WinOfNotice, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        table_data = help_file.database.pull_data(help_file.active_path)
        active_data = table_data[0]

        self.ui.name.setText(active_data[1])
        self.ui.date.setText(active_data[2])
        self.ui.time.setText('время: {}:{}'.format(active_data[3], active_data[4]))

        self.ui.pushButton.clicked.connect(self.close_win)

    # функция закрытие окна
    def close_win(self):
        query = f"""
                    UPDATE data SET
                        name = NULL,
                        days = NULL,
                        hour = NULL,
                        minutes = NULL
                    WHERE id = {int(help_file.active_id)}
                """
        help_file.database.update_data(help_file.active_path, query)

        raise NameError  # вызов исключения для закрытия окна
