version = "dev 0.0"

running = False

def init():
    global running
    if not running:
        print("JFUtils-python \"" + version + "\" by jonnelafin")
        running = True
