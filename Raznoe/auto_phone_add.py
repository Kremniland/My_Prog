# !/usr/bin/python3
import random


class Battery:
    """Аккумулятор: тип, ёмкость в мА/ч"""
    def __init__(self):
        self.type = random.choice(
            list(
                {
                    'NiCa': 'Nickel-cadmium',
                    'NiMH': 'Nickel Metal Hydride',
                    'Li-ion': 'Lithium-ion',
                    'Li-pol': 'Lithium-Polymer'
                }.values()))

        self.capacity = random.randrange(1000, 5000)


class Display:
    """Дисплей: тип, размер в мм"""
    def __init__(self):
        self.type = random.choice(
            list(
                {
                    'TN': 'Twisted Nematic tech (LCD)',
                    'IPS': 'In-Plane Switching tech (LCD)',
                    'OLED': 'Organic Light-emitting Diode',
                    'AMOLED': 'Active Matrix Organic Light-Emitting Diode',
                }.values()))

        self.size = random.choice([
            '414 x 896',
            '375 x 812',
            '414 x 896',
            '375 x 812',
            '414 x 736',
            '412 x 732',
            '412 x 824',
            '412 x 846',
            '412 x 847',
            '412 x 824',
            '412 x 732',
            '412 x 869'
        ])


class Processor:
    """Процессор: название, частота в МГц"""
    def __init__(self):
        self.name = random.choice(
            list(
                {
                    'MediaTek': random.choice(
                        [
                            'Dimensity 9000 Plus',
                            'Helio G90T',
                            'Dimensity 1200'
                        ]),
                    'HiSilicon': 'Kirin 970',
                    'Qualcomm': 'Snapdragon 8 Plus Gen 1',
                    'Samsung': 'Exynos 2100',
                    'Apple': 'A13 Bionic',
                }.values()))

        self.cpu_freq = random.choice([
            '3240',
            '3200',
            '3050',
            '3000',
            '3100',
            '2995',
            '2800',
            '2840',
            '2850',
            '2850',
            '2800',
            '3130',
            '2900',
            '2660'
        ])


class RAM:
    """Оперативная память: объём в Гб"""
    def __init__(self):
        self.size = random.choice([2, 4, 8, 12, 16, 24])


class Memory:
    """Физическая память: объём в Гб"""
    def __init__(self):
        self.size = random.choice([8, 16, 32, 64, 128])

class Collector:
    def collect_battery(self):
        return NotImplementedError

    def collect_display(self):
        return NotImplementedError

    def collect_processor(self):
        return NotImplementedError

    def collect_ram(self):
        return NotImplementedError

    def collect_memory(self):
        return NotImplementedError

    def collect_mic(self):
        return NotImplementedError


class PhoneCollector(Collector):
    def collect_battery(self):
        battery = Battery()
        type = battery.type
        capacity = battery.capacity
        return f'{type.replace(" ", "")}_cap-{capacity}mAh'

    def collect_display(self):
        display = Display()
        type = display.type
        size = display.size
        return f'display_{type.replace(" ", "")}[{size.replace(" ", "")}mm]'

    def collect_processor(self):
        processor = Processor()
        name = processor.name
        freq = processor.cpu_freq
        return f'{name.replace(" ", "")}_freq_{freq}Mhz'

    def collect_ram(self):
        ram = RAM()
        size = ram.size
        return f'{size}_Gb'

    def collect_memory(self):
        memory = Memory()
        size = memory.size
        return f'{size}_Gb'

    def phone_collect(self):
        battery = self.collect_battery()
        display = self.collect_display()
        processor = self.collect_processor()
        ram = self.collect_ram()
        memory = self.collect_memory()
        mic = self.collect_mic()
        return Phone(battery, display, processor, ram, memory, mic)


class Phone:
    def __init__(self, battery, display, processor, ram, memory, mic):
        self.name = random.choice(['Xiaomi', 'Honor', 'Samsung', 'Iphone', 'Asus', 'Noname Taiwan product'])
        self.amount = f'{random.randrange(10000, 30000):.2f}'
        self.id = random.randrange(10000000)
        self.battery = battery
        self.display = display
        self.processor = processor
        self.ram = ram
        self.memory = memory
        self.mic = mic


def main():
    collector = PhoneCollector()
    phone = collector.phone_collect()
    phone_list = [phone.name, phone.battery, phone.display, phone.processor, phone.ram, phone.memory, phone.amount]
    return phone_list

