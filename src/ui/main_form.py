"""Главная форма для ввода параметров в набегающем потоке"""
import typing as tp

from PySide2 import QtGui
from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QLineEdit


class MainWindow(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Расчет параметров непосредственно за ударной волной")

        layout = QGridLayout()

        lable_title = QLabel("Параметры в набегающем потоке")
        lable_title.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        layout.addWidget(lable_title, 0, 0, 1, 2)

        lable_temperature0 = QLabel("Температура [К]")
        layout.addWidget(lable_temperature0, 1, 0, 1, 1)
        self.line_temperature0 = QLineEdit()
        layout.addWidget(self.line_temperature0, 1, 1, 1, 1)

        lable_mach0 = QLabel("Число Маха")
        layout.addWidget(lable_mach0, 2, 0, 1, 1)
        self.line_mach0 = QLineEdit()
        layout.addWidget(self.line_mach0, 2, 1, 1, 1)

        lable_pressure0 = QLabel("Давление [Дж]")
        layout.addWidget(lable_pressure0, 3, 0, 1, 1)
        self.line_pressure0 = QLineEdit()
        layout.addWidget(self.line_pressure0, 3, 1, 1, 1)

        lable_title_bsw = QLabel("Параметры непосредственно за ударной волной")
        lable_title_bsw.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        layout.addWidget(lable_title_bsw, 4, 0, 1, 2)

        self.lable_temperature_bsw = QLabel("Температура , К = ")
        layout.addWidget(self.lable_temperature_bsw, 5, 0, 1, 2)

        self.lable_n_bsw = QLabel("Число частиц = ")
        layout.addWidget(self.lable_n_bsw, 6, 0, 1, 2)

        self.lable_velocity_bsw = QLabel("Скорость, м/с = ")
        layout.addWidget(self.lable_velocity_bsw, 7, 0, 1, 2)

        self.calc_button = QPushButton("Расчитать")
        layout.addWidget(self.calc_button, 8, 1, 1, 1)

        self.setLayout(layout)

    def get_parameters(self) -> tp.Dict[str, float]:
        """
        Собирает параметры в набегающем потоке.

        :return: Словарь параметров, где ключи: "temperature0", "pressure0", "mach0"
        """
        output = {}

        output["temperature0"] = float(self.line_temperature0.text())
        output["pressure0"] = float(self.line_pressure0.text())
        output["mach0"] = float(self.line_mach0.text())

        return output

    def set_params_behind_schock_wave(self, temperature_bsw: float, n_bsw: float, velocity_bsw: float) -> None:
        """
        Заполняет результат расчета параметров сразу за скачком уплотнения ударной волны.

        :param temperature_bsw: Температура сразу за ударной волной.
        :param n_bsw: Число частиц сразу за ударной волной.
        :param velocity_bsw: Скорость потока сразу за ударной волной.
        """
        text_temperature = f"Температура , К = {temperature_bsw}"
        self.lable_temperature_bsw.setText(text_temperature)
        text_n = f"Число частиц = {n_bsw}"
        self.lable_n_bsw.setText(text_n)
        text_velocity = f"Скорость, м/с = {velocity_bsw}"
        self.lable_velocity_bsw.setText(text_velocity)
