'''
Модуль розрахунку площі для прикладу інформаційного обміну із функціями
'''

def example_dict (in_s):
    s = (1 / 2) * in_s['triangle_parameter_a'] * in_s['triangle_parameter_h']
    output_s = dict(result=in_s['result'], triangle_parameter_a=in_s['triangle_parameter_a'], triangle_parameter_h=in_s['triangle_parameter_h'], out=s)
    return output_s
