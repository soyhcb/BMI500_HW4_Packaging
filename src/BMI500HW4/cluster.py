from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt

class Cluster:
    def __init__(self):
        """
        This function initial lize the instance, it will load
        iris dataset from sklearn. Original data is 4 dimensional
        . We have decompolized data into 2 dimensional with PCA. 
        So we can conduct clustering and visualization on data directly.
        """
        # load iris data from sklearn
        data_iris = datasets.load_iris()
        # conduct PCA on data
        pca = PCA(n_components=2)
        pca_iris = pca.fit_transform(data_iris.data)

        # save models and parameters
        self.X= pca_iris
        self.cluster = None
        self.groundtruth = data_iris["target"]
        self.labels = data_iris["target_names"]
        self.model=None
        self.pca=pca

    def kmeans_sk(self, n_clusters=3):
        """
        This Function conduct kmeans on data.
        Input: n_clusters: number of clusters that k-means outputs
        Return: 1D-array of predictions.
        Default data is iris dataset, so has default 3 clusters
        """
        model = KMeans(n_clusters=n_clusters, random_state=0).fit(self.X)
        self.cluster = model.labels_
        self.model = model
        return self.cluster
    
    def predict(self,pos):
        """
        This function predict the cluster of the input data;
        Input: pos: 2darray [[x1, y1],[x2, y2],...,[xn, yn]] or 
                [[x11, x12,x13, x14],[x21, x22, x23, x24],...,[xn1, xn2, xn3, xn4]] for iris data.
        Return: 1D-array of predictions.
        if data has higher dimension (4 dimensional), will PCA it into 2d;
        """
        if not self.model:
            raise Exception("Model not fitted. please run `<instance>.kmeans_sk()` first")
        if len(pos[0]) == 4:
            pos = self.pca.transform(pos)
        return self.model.predict(pos)
    
    def visualization(self,groundtruth=False,save=None):
        """
        This function visualize the cluster of the iris data;
        Input:  groundtruth:    if True, will plot with labels of groundtruth;
                            if False(default), will plot the estimated result;
                save:   string of file path or None(default);
                    if has value, will save the figure to the path, or will not save
        """
        if groundtruth:
            # Plot the points
            plt.scatter(self.X[:, 0], self.X[:, 1], c=self.groundtruth, cmap=plt.cm.Set1,
                        edgecolor='k')
            # set axises
            plt.xlabel('eigenvector 1')
            plt.ylabel('eigenvector 1')
            plt.xlim(min(self.X[:, 0]), max(self.X[:, 0]))
            plt.ylim(min(self.X[:, 1]), max(self.X[:, 1]))
            plt.xticks(())
            plt.yticks(())
            norm = plt.Normalize(self.groundtruth.min(), self.groundtruth.max())
            handles = [plt.Line2D([0, 0], [0, 0], color=plt.cm.Set1(norm(i)), marker='o', linestyle='', label=label)
           for i, label in enumerate(self.labels)]
            plt.legend(handles=handles, title='Species')
        else:
            if not self.model:
                raise Exception("Model not fitted. please run `<instance>.kmeans_sk()` first") 
                        # Plot the points
            plt.scatter(self.X[:, 0], self.X[:, 1], c=self.cluster, cmap=plt.cm.Set1,
                        edgecolor='k')
            # set axises
            plt.xlabel('eigenvector 1')
            plt.ylabel('eigenvector 1')
            plt.xlim(min(self.X[:, 0])-1, max(self.X[:, 0])+1)
            plt.ylim(min(self.X[:, 1]-1), max(self.X[:, 1])+1)
            plt.xticks(())
            plt.yticks(())
        if save:
            plt.savefig(save)
        plt.show()

                
    
    def __str__(self):
        if self.model:
            return str(self.cluster)
        return "Model not fitted. please run `<instance>.kmeans_sk()` first"

def run_default():
    clst = Cluster()
    print(clst)
    try:
        clst.predict([[1,2,3,4]])
    except Exception as e:
        print(str(e))
    print(clst.kmeans_sk())
    print(clst.predict([[1,2,3,4],[2,2,3,1],[10,10,10,10]]))
    print(clst)
    clst.visualization()

if __name__=="__main__":
    run_default()