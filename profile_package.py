import os
try:
    from BMI500HW4.cluster import Cluster, run_default
except ImportError as e:
    print(e, "package not installed properly.\n Try to import locally")
    try:
        from src.BMI500HW4.cluster import Cluster, run_default
    except ImportError as e:
        print("Package not located properly")
        raise e

test_usage = True
try:
    import psutil
except ImportError as e:
    print("`psutils` is required to test cpu and memory usage;\n this package is not required by main program.\n will run without test usage.")
    test = False

def test():
    clt = Cluster()
    clt.kmeans_sk()
if test_usage:
    test()
    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_info()[0]/2.**30  # memory use in GB...I think
    print('memory use:', memoryUse, '. CPU use:', psutil.cpu_percent())
else:
    run_default()