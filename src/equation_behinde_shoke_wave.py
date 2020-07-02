from src.constatn_params import *
# Kap=1+(0.79*m(1)/muc(1)+0.21*m(2)/muc(2))*R/((5/2*k*(0.79+0.21)+f(1)*0.79*m(1)+f(2)*0.21*m(2)))%показатель адиабаты в набегающем потоке

class BehindShockWave():
    """Класс для расчета параметров за ударной валной гармонического оссацилятора
    , на вход падаются параметры в набегающем потоке"""
    temperature_bsw: float
    number_of_moles_bsw: int
    pressure_bsw: float
    velocity_bsw: float
    def __init__(self, t0: float, m0: int, p0: float):
        self.temperature0 = t0
        self.mach0 = m0
        self.pressure0 = p0
    def calc_shockwave(self):
        """
        Функция для расчета основных параметров за ударной волной
        """
        n0 = self.pressure0 / k / self.temperature0  # число частиц в набегающем потоке
        ro0 = 0.79 * n0 * mas['n2'] + 0.21 * n0 * mas['o2']  # плотность в набегающем потоке
        kap = 9 / 7
        self.temperature_bsw = self.temperature0 * (2 * kap / (kap + 1) * self.mach0 ** 2 - (kap - 1) / (kap + 1)) * (
                    2 / (kap + 1) / self.mach0 ** 2 + (kap - 1) / (kap + 1))  # температура за ударной волной
        p_bsw = self.pressure0 * (2 * kap / (kap + 1) * self.mach0 ** 2 - (kap - 1) / (kap + 1))  # давление за ударной волной
        self.number_of_moles_bsw = p_bsw / k / self.temperature_bsw  # число частиц за ударной волной
        # m_bsw = (((kap + 1) / 2 / kap) ** 2 / (self.mach0 ** 2 - (kap - 1) ** 2 / 2 / kap) + (
        #             kap - 1) ** 2 / 2 / kap) ** 0.5  # число маха за ударной волной
        a0 = (kap * self.pressure0 / ro0) ** 0.5  # скорость звука в набегающем потоке
        v0 = self.mach0 * a0  # скорость в набегающем потоке
        self.velocity_bsw = v0 * (2 / (kap + 1) / self.mach0 ** 2 + (kap - 1) / (kap + 1))  # скорость за ударной волной
