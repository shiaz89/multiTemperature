import sys

from PySide2.QtWidgets import QApplication

from calculation_behind_schock_wave.presenter_bsw import ParametersBehindSchokWavePresenter

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = ParametersBehindSchokWavePresenter()
    sys.exit(app.exec_())