from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import datasets

def load_iris():
    """
    This function will load iris dataset from sklearn.
    Original data is 4 dimensional. We have decompolized 
    data into 2 dimensional with PCA. So we can conduct 
    clustering and visualization on data directly.
    """
    data_iris = datasets.load_iris()
    # conduct PCA on data
    pca = PCA(n_components=2)
    pca_iris = pca.fit_transform(data_iris.data)
    # return data with x,y, since model is unsupervised, y id only for reference purpose.
    return {'x':pca_iris, "y":data_iris.target}

def kmeans(data,n_clusters=3):
    """
    This Function conduct kmeans on data inputted.
    input:  data: 2 dimensional data points.
            n_clusters: number of clusters that k-means outputs
    Default data is iris dataset, so has default 3 clusters
    """
    if type(data) == dict:
        data=data['x']
    model = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    return model.labels_

def run_default():
    data = load_iris()
    return kmeans(data)

if __name__=="__main__":
    run_default()