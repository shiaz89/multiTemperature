from src.calculation_behind_schock_wave.equation_behinde_shoke_wave import BehindShockWave
from src.ui.main_form import MainWindow


class ParametersBehindSchokWavePresenter:
    """Класс отвечающий за передачу сигналов в модель"""

    def __init__(self):
        self.view = MainWindow()
        self.model = BehindShockWave()
        self.view.show()
        self.connect_signals()

    def connect_signals(self) -> None:
        self.view.calc_button.clicked.connect(self.calculate)

    def calculate(self) -> None:
        parameters = self.view.get_parameters()
        self.model.set_macroscopic_parametrs(**parameters)
        parameters_bsw = self.model.calc_shockwave()

        self.view.set_params_behind_schock_wave(**parameters_bsw)

