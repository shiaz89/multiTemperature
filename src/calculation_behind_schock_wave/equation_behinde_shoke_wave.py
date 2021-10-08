from src.calculation_behind_schock_wave.constatn_params import *
import typing as tp
# Kap=1+(0.79*m(1)/muc(1)+0.21*m(2)/muc(2))*R/((5/2*k*(0.79+0.21)+f(1)*0.79*m(1)+f(2)*0.21*m(2)))%показатель адиабаты в набегающем потоке

class BehindShockWave():
    """Класс для расчета параметров за ударной валной гармонического оссацилятора
    , на вход падаются параметры в набегающем потоке

    Концентрация азота N2 и O2 - 79% и 21% соответственно
    """
    temperature_bsw: float
    number_of_moles_bsw: int
    pressure_bsw: float
    velocity_bsw: float
    n_n2: float = 0.79
    n_o2: float = 0.21

    def set_macroscopic_parametrs(self, temperature0: float, mach0: int, pressure0: float) -> None:
        """
        Задание макропараметров в набегающем потоке.

        :param temperature0: Температура в набегающем потоке, К.
        :param mach0: Число Маха.
        :param pressure0: Давление в набегающем потоке, Дж.
        """
        self.temperature0 = temperature0
        self.mach0 = mach0
        self.pressure0 = pressure0

    def calc_shockwave(self) -> tp.Dict[str, float]:
        """
        Функция для расчета основных параметров за ударной волной
        """
        n0 = self.pressure0 / k / self.temperature0  # число частиц в набегающем потоке
        ro0 = self.n_n2 * n0 * mas['n2'] + self.n_o2 * n0 * mas['o2']  # плотность в набегающем потоке
        kap = 9 / 7
        self.temperature_bsw = self.temperature0 * (2 * kap / (kap + 1) * self.mach0 ** 2 - (kap - 1) / (kap + 1)) * (
                    2 / (kap + 1) / self.mach0 ** 2 + (kap - 1) / (kap + 1))  # температура за ударной волной
        p_bsw = self.pressure0 * (2 * kap / (kap + 1) * self.mach0 ** 2 - (kap - 1) / (kap + 1))  # давление за ударной волной
        self.n_bsw = p_bsw / k / self.temperature_bsw  # число частиц за ударной волной
        # m_bsw = (((kap + 1) / 2 / kap) ** 2 / (self.mach0 ** 2 - (kap - 1) ** 2 / 2 / kap) + (
        #             kap - 1) ** 2 / 2 / kap) ** 0.5  # число маха за ударной волной
        a0 = (kap * self.pressure0 / ro0) ** 0.5  # скорость звука в набегающем потоке
        v0 = self.mach0 * a0  # скорость в набегающем потоке
        self.velocity_bsw = v0 * (2 / (kap + 1) / self.mach0 ** 2 + (kap - 1) / (kap + 1))  # скорость за ударной волной

        return {"temperature_bsw": self.temperature_bsw, "n_bsw": self.n_bsw, "velocity_bsw": self.velocity_bsw}
