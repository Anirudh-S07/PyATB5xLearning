class InternalLogs:
    def __init__(self):
        print("Internal Logging has started")


class LogStart(InternalLogs):
    def __init__(self):
        super().__init__()
        print("Logging has started")


