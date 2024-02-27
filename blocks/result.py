from barfi import Block

result = Block(name='Display Result')
result.add_option(name='result-msg', type='display', value='Dönen sonucu gösterir')
result.add_option(name='result-val', type='display', value='[...]')
result.add_input(name='disp_input')

def result_function(self):
    # get the value of the input interface
    input_data = self.get_interface(name='disp_input')
    self.set_option('result-val', value=input_data)
    #self.set_option(name='result-val', value=input_data)
    #self.add_option(name='result-val', type='display', value=input_data)
    #result.add_option(name='result-val', type='display', value=input_data)

result.add_compute(result_function)
#result.set_option('result-val', input_data)