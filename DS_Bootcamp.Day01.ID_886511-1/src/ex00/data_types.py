def data_types():
    #output_list = [1, 'string', 3.14, True, ['list'], {'this_is_a_':'dictionary'}, ('tuple'), {'set'}]
    #for data_type in output_list:
    #    print(type(data_type), sep=' ')
    integer = 1
    string = 'string'
    fl = 3.14159265
    boolean = True
    lst = []
    dct = {'this_is_a_':'dict'}
    tpl = (1,)
    st = {'set'}
    #print(list(integer, string, fl, boolean, lst, dct, tpl, st))
    types_list = [type(integer).__name__, type(string).__name__, type(fl).__name__, type(boolean).__name__, type(lst).__name__, type(dct).__name__, type(tpl).__name__, type(st).__name__]
    print(f"[{', '.join(types_list)}]")

if __name__ == '__main__':
    data_types()
