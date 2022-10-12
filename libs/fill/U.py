from libs.fields import Fields


def fill_U(params, fn=None, fp=None, p=None):
    U = Fields(field_name='U', internal_value=params['internal_value'],
               boundary_types=params.get('boundary_types', None),
               boundary_name=params.get('boundary_name', None),
               value=params.get('value', None), params=p)
    U.make_boundary_conditions(filename=fn, fp=fp)

