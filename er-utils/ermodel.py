class ERModel:
    '''
    Interface for Entity Resolution models
    '''

    def __init__(self):
        self.name = ''

    def predict(self, x, **kwargs):
        pass

    def train(self, label_train, label_valid, dataset_name, **kwargs):
        pass

    def save(self, path, **kwargs):
        pass

    def load(self, path, **kwargs):
        pass

    def evaluation(self, test_set, **kwargs):
        pass

    def predict_proba(self, x, **kwargs):
        pass

