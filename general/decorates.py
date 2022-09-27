def ann(f):
    def wrapper():
        print("About to run the function..")
        f()
        print("Done with the function")
    return wrapper
@ann
def hello():
    print("Hello,world! This is zahidpranta")

hello()