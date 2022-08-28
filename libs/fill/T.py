from libs.fields import Fields


def fill_T(params, fn=None, fp=None):
    p_rgh = Fields(field_name='T', internal_value=params['internal_value'],
                   boundary_types=params.get('boundary_types', None),
                   boundary_name=params.get('boundary_name', None),
                   value=params.get('value', None))
    p_rgh.make_boundary_conditions(filename=fn, fp=fp)