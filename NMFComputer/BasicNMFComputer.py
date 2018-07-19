'''
Created on Jul 16, 2018

@author: daniel
'''

from NMFComputer.NMFComputer import NMFComputer
from sklearn.decomposition import NMF


class BasicNMFComputer(NMFComputer):
    nmf_model = None

    def __init__(self, block_size = 400, num_hist_bins = 256, num_components = 5):
        super().__init__(block_size, num_hist_bins, num_components)
        self.creatNMFModel(num_components)

        
        
    def computeNMF(self, V):
        W = self.nmf_model.fit_transform(V)
        H = self.nmf_model.components_
        return W, H
    
        
    def creatNMFModel(self, num_components):
        self.nmf_model = NMF(n_components=num_components, init='random', random_state=0, solver='cd')
            
