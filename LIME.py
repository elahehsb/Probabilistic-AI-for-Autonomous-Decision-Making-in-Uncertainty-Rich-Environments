import lime
import lime.lime_tabular
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Example data
X_train = np.random.rand(100, 5)
y_train = np.random.randint(2, size=100)

# Train a random forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Create LIME explainer
explainer = lime.lime_tabular.LimeTabularExplainer(X_train, feature_names=['f1', 'f2', 'f3', 'f4', 'f5'], class_names=['no risk', 'risk'], discretize_continuous=True)

# Generate explanation for a new data point
X_test = np.random.rand(1, 5)
explanation = explainer.explain_instance(X_test[0], clf.predict_proba)
explanation.show_in_notebook()
