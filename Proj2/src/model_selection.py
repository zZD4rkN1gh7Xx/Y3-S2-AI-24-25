from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

def get_best_models(X_train, y_train):
    models = {}

    # Decision Tree
    dt_params = {'max_depth': [3, 5, 10, None]}
    dt = GridSearchCV(DecisionTreeClassifier(), dt_params, cv=5)
    dt.fit(X_train, y_train)
    models['Decision Tree'] = dt

    # Random Forest
    rf_params = {'n_estimators': [50, 100], 'max_depth': [5, 10, None]}
    rf = GridSearchCV(RandomForestClassifier(), rf_params, cv=5)
    rf.fit(X_train, y_train)
    models['Random Forest'] = rf

    # KNN
    knn_params = {'n_neighbors': [3, 5, 7]}
    knn = GridSearchCV(KNeighborsClassifier(), knn_params, cv=5)
    knn.fit(X_train, y_train)
    models['KNN'] = knn

    return models

def evaluate_models(models, X_test, y_test):
    print("\n--- Model Evaluation ---")
    for name, model in models.items():
        y_pred = model.predict(X_test)
        print(f"\n{name}:")
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Precision:", precision_score(y_test, y_pred, average='weighted'))
        print("Recall:", recall_score(y_test, y_pred, average='weighted'))
        print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))