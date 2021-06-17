import numpy as np
from loader import LoadData
from get_feature import split_alloy, get_feature_set

class ModelPred:
    def __init__(self):
        self.model = LoadData.get_model()
        self.element_data = LoadData.element_data()

    def predict(self, alloy_name):
        try:
            alloy_dict = split_alloy(alloy_name)
            features = get_feature_set(alloy_dict, self.element_data)
            pred = self.model.predict(features)
            c11, c22, c33 = round(pred[0][0],3), round(pred[0][1],3), round(pred[0][2],3)
            c12, c13, c23 = round(pred[0][3],3), round(pred[0][4],3), round(pred[0][5],3)
            c44, c55, c66 = round(pred[0][6],3), round(pred[0][7],3), round(pred[0][8],3)

            Cij = np.zeros(shape=(6,6))
            Cij[0][0] = c11
            Cij[1][1] = c22
            Cij[2][2] = c33
            Cij[3][3] = c44
            Cij[4][4] = c55
            Cij[5][5] = c66
            Cij[0][1], Cij[1][0] = c12, c12
            Cij[0][2], Cij[2][0] = c13, c13
            Cij[1][2], Cij[2][1] = c23, c23
            Sij = np.linalg.inv(Cij) #compliance tensor

            Bv = (1/9)*((Cij[0][0] + Cij[1][1] + Cij[2][2]) 
                + 2*(Cij[0][1] + Cij[0][2] + Cij[1][2]))
            Br = 1/((Sij[0][0] + Sij[1][1] + Sij[2][2]) 
                + 2*(Sij[0][1] + Sij[0][2] + Sij[1][2]))
            Gv = (1/15)*((Cij[0][0] + Cij[1][1] + Cij[2][2]) 
                - (Cij[0][1] + Cij[0][2] + Cij[1][2]) 
                + 3*(Cij[3][3] + Cij[4][4] + Cij[5][5]))
            Gr = 15/(4*(Sij[0][0] + Sij[1][1] + Sij[2][2]) 
                - 4*(Sij[0][1] + Sij[0][2] + Sij[1][2]) 
                + 3*(Sij[3][3] + Sij[4][4] + Sij[5][5]))
            B = round((Bv + Br)/2, 3)
            G = round((Gv + Gr)/2, 3)
            PR = round((3*B - 2*G)/(6*B + 2*G), 3)

            return f'C11: {c11:.3f}, C22: {c22:.3f}, C33: {c33:.3f}, C12: {c12:.3f}, C13: {c13:.3f}, C23: {c23:.3f}, C44: {c44:.3f}, C55: {c55:.3f}, C66: {c66:.3f}, B: {B:.3f}, G: {G:.3f}, PR: {PR:.3f}\n'

        except (IndexError, ZeroDivisionError):
            return 'ERROR:\nWrong Input! Format Example: Ni3Al, FeNiCrAl\n'

