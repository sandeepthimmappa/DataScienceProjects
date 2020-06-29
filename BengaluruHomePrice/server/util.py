import json
import pickle
import numpy as np

__locations = None
__columns = None
__model = None




def load_saved_artifacts():
    print('loading artifact start')
    global __locations
    global __columns

    with open('./artifacts/column.json', 'r') as f:
        __columns = json.load(f)['columns']
        __locations = __columns[9:]

    global __model
    with open('./artifacts/bengaluru_home_price.pickle', 'rb') as f:
        __model = pickle.load(f)

    print('loading artifacts stop')

def get_estimated_price(location, bhk, bath, sqft):
    loc_index = __columns.index(location.lower())

    x = np.zeros(len(__columns))
    x[2] = sqft
    x[5] = bhk
    x[3] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

if __name__ =='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',2, 2, 1000))
    print(get_estimated_price('Indira Nagar',3, 3, 1000))