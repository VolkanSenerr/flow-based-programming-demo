from barfi import Block

minmax = Block(name='Return MinMax')
minmax.add_option(name='average-msg', type='display', value='Değerlerden minimum ve maksimum değerleri döner')
minmax.add_input(name='minmax_input')
minmax.add_output(name='min')
minmax.add_output(name='max')
def min_max_function(self):
    # get the value of the input interface
    input_data = self.get_interface(name='minmax_input')

    min_out = min(input_data)
    max_out = max(input_data)

    self.set_interface(name='min', value=min_out)
    self.set_interface(name='max', value=max_out)

minmax.add_compute(min_max_function)