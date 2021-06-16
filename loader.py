import pandas as pd
import pickle

class LoadData():
    def element_data():
        df_elements = pd.read_excel("elements_data.xlsx")
        df_elements = df_elements.drop(['Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19', 'Unnamed: 20'], axis=1)
        return(df_elements)

    def get_model():
        model = pickle.load(open('rf_model_5feature.sav', 'rb'))
        return(model)

        