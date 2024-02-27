from barfi import Block
import csv

loader = Block(name='CSV Loader')
loader.add_option(name='loader-msg', type='display', value='Yüklenecek CSV dosyasının adını girin')
loader.add_option(name='filepath-input', type='input')
loader.add_output(name='data')
def loader_function(self):
    path = self.get_option(name='loader-msg')
    with open(path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    self.set_interface(name='data', value=data[0])
loader.add_compute(loader_function)