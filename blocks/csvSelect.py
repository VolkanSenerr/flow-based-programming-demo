from barfi import Block
import csv

selector = Block(name='Select CSV')
selector.add_option(name='selector-msg', type='display', value='Yüklenilecek data dosyasını seçin')
selector.add_option(name='filepath-input', type='select', items=['data1.csv', 'data2.csv'], value='data1')
selector.add_output(name='data')
def selector_function(self):
    path = self.get_option(name='select-file')
    with open(path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    self.set_interface(name='data', value=data[0])
selector.add_compute(selector_function)