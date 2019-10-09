code_num = {
            '3':['Cupcake','1.5'],
            '4':['Donut','1.6'], 
            '5':['Eclair','2.0-2.1'], 
            '6':['Eclair','2.0-2.1'], 
            '7':['Eclair','2.0-2.1'],
            '8':['Froyo','2.2-2.2.3'],
            '9':['Gingerbread','2.3-2.3.7'],
            '10':['Gingerbread','2.3-2.3.7'],
            '11':['Honeycomb','3.0-3.2.6'],
            '12':['Honeycomb','3.0-3.2.6'],
            '13':['Honeycomb','3.0-3.2.6'],
            '14':['Ice Cream Sandwich','4.0-4.0.4'],
            '15':['Ice Cream Sandwich','4.0-4.0.4'],
            '16':['Jelly Bean','4.1–4.3.1'],
            '17':['Jelly Bean','4.1–4.3.1'],
            '18':['Jelly Bean','4.1–4.3.1'],
            '19':['KitKat','4.4–4.4.4'],
            '20':['KitKat','4.4–4.4.4'],
            '21':['Lollipop','5.0–5.1.1'],
            '22':['Lollipop','5.0–5.1.1'],
            '23':['Marshmallow','6.0–6.0.1'],
            '24':['Nougat','7.0–7.1.2'],
            '25':['Nougat','7.0–7.1.2'],
            '26':['Oreo','8.0–8.1'],
            '27':['Oreo','8.0–8.1'],
            '28':['Pie','9.0'],
            '29':['Android 10','10.0']
}

def get_android_code(api_level):
    code,_ = code_num[api_level]
    return code

def get_android_ver_num(api_level):
    _,ver_num = code_num[api_level]
    return ver_num

def is_permission_dangerous(permission):
    pass