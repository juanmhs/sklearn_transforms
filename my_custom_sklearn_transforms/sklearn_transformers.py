from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

    
class OverSampling(BaseEstimator, TransformerMixin):
    def __init__(self):
       pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        
        count_class_0, count_class_1 = data.OBJETIVO.value_counts()

        # Divide by class
        df_class_0 = data[data['OBJETIVO'] == "Aceptado"]
        df_class_1 = data[data['OBJETIVO'] == "Sospechoso"]

        #OVER
        df_class_1_over = df_class_1.sample(count_class_0, replace=True)
        df_test_over = pd.concat([df_class_0, df_class_1_over], axis=0)

        return df_test_over
