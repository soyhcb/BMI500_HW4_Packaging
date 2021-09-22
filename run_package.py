try:
    from BMI500HW4.cluster import Cluster
except ImportError as e:
    print(e, "package not installed properly.\n Try to import locally")
    try:
        from src.BMI500HW4.cluster import Cluster
    except ImportError as e:
        print("package not located properly")
        raise e


def run_default():
    clst = Cluster()
    print("try to print instance:", clst)
    try:
        clst.predict([[1,2,3,4]])
    except Exception as e:
        print("try to predict before fit:", str(e))
    print("Cluster Results:", clst.kmeans_sk())
    print("Predict New Points:",clst.predict([[1,2,3,4],[2,2,3,1],[10,10,10,10]]))
    print("try to print instance:", clst)
    clst.visualization()

if __name__=="__main__":
    run_default()