import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler

class ProblemSolvingTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.mapping = {"Buruk": 1, "Cukup": 2, "Kurang Memuaskan": 3, "Baik": 4, "Sangat Baik": 5}

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()
        X_copy['problem_solving'] = X_copy['problem_solving'].map(self.mapping).astype(int)
        return X_copy

class FeedbackTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.mapping = {"Buruk": 1, "Cukup": 2, "Kurang Memuaskan": 3, "Baik": 4, "Sangat Baik": 5}

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()
        X_copy['debtor_feedback'] = X_copy['debtor_feedback'].map(self.mapping).astype(int)
        return X_copy

class RPCTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()
        X_copy['total_contact'] = X_copy['total_contact'].astype(float)
        X_copy['contact_connected'] = X_copy['contact_connected'].astype(float)
        # Handle division by zero
        X_copy['RPC_rate'] = np.where(X_copy['total_contact'] > 0, 
                                    (X_copy['contact_connected'] / X_copy['total_contact']) * 100, 
                                    0)
        return X_copy

class CEITransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()
        X_copy['total_debt'] = X_copy['total_debt'].astype(float)
        X_copy['total_debt_payment_recieved'] = X_copy['total_debt_payment_recieved'].astype(float)
        # Handle division by zero
        X_copy['recovery_rate'] = np.where(X_copy['total_debt'] > 0,
                                         (X_copy['total_debt_payment_recieved'] / X_copy['total_debt']) * 100,
                                         0)
        return X_copy

class PTPTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()
        X_copy['call_to_ptp'] = X_copy['call_to_ptp'].astype(float)
        # Handle division by zero
        X_copy['PTP_rate'] = np.where(X_copy['contact_connected'] > 0,
                                     (X_copy['call_to_ptp'] / X_copy['contact_connected']) * 100,
                                     0)
        return X_copy

class ZScoreTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        self.scaler = StandardScaler()
        self.is_fitted = False

    def fit(self, X, y=None):
        # Ensure we have all required columns
        available_columns = [col for col in self.columns if col in X.columns]
        if available_columns:
            self.scaler.fit(X[available_columns])
            self.is_fitted = True
        return self

    def transform(self, X):
        X_copy = X.copy()
        # Check if all required columns exist
        available_columns = [col for col in self.columns if col in X_copy.columns]
        
        if available_columns and self.is_fitted:
            X_copy[available_columns] = self.scaler.transform(X_copy[available_columns])
        return X_copy

class DataTypeTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, numeric_columns=None):
        self.numeric_columns = numeric_columns

    def fit(self, X, y=None):
        if self.numeric_columns is None:
            self.numeric_columns = X.select_dtypes(include=['number']).columns.tolist()
        return self
        
    def transform(self, X):
        X_copy = X.copy()
        for col in self.numeric_columns:
            if col in X_copy.columns:
                X_copy[col] = X_copy[col].astype(float)
        return X_copy