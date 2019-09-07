class BreastCancer:
    def __init__(self):
        pass
    def execute(self):
        import sklearn
        from sklearn.tree import DecisionTreeClassifier
        import sklearn.datasets
        from sklearn.datasets import load_breast_cancer

        from sklearn.model_selection import train_test_split

        cancer = load_breast_cancer()
        X_train,X_test,y_train,y_test = train_test_split(
            cancer.data,cancer.target,stratify=cancer.target,random_state=42

        )