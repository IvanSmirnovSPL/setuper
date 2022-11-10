from libs.fields import Fields


def fill_alpha_water(params, fn=None, fp=None, p=None):
    types = params.get('boundary_types', None)
    for idt, type in enumerate(types):
        if 'out_with_value' == type:
            types[idt] = 'out_with_value_alpha'
        if 'in_with_value' == type:
            types[idt] = 'in_with_value_alpha'
    alpha_water = Fields(field_name='alpha.water', internal_value=params['internal_value'],
                         boundary_types=types,
                         boundary_name=params.get('boundary_name', None),
                         value=params.get('value', None), params=p)
    alpha_water.make_boundary_conditions(filename=fn, fp=fp)