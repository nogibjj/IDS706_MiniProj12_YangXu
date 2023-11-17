import unittest
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


class TestMLModel(unittest.TestCase):
    def setUp(self):
        # Load the Iris dataset
        X, y = datasets.load_iris(return_X_y=True)
        self.X_tr, self.X_te, self.y_tr, self.y_te = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Define the model hyperparameters
        self.params = {
            "solver": "lbfgs",
            "max_iter": 1000,
            "multi_class": "auto",
            "random_state": 8888,
        }

    def test_model_training(self):
        # Train the model
        lr = LogisticRegression(**self.params)
        lr.fit(self.X_tr, self.y_tr)
        self.assertIsNotNone(lr, "Model should not be None after training.")

    def test_model_prediction(self):
        # Train the model and predict
        lr = LogisticRegression(**self.params)
        lr.fit(self.X_tr, self.y_tr)
        y_pred = lr.predict(self.X_te)

        # Check if the prediction length matches test data length
        self.assertEqual(
            len(y_pred),
            len(self.y_te),
            "Prediction length should match test labels length.",
        )

    def test_prediction_accuracy(self):
        # Train the model and predict
        lr = LogisticRegression(**self.params)
        lr.fit(self.X_tr, self.y_tr)
        y_pred = lr.predict(self.X_te)

        # Check if accuracy score is computable
        accuracy = accuracy_score(self.y_te, y_pred)
        self.assertIsInstance(accuracy, float, "Accuracy should be a float value.")


if __name__ == "__main__":
    unittest.main()
