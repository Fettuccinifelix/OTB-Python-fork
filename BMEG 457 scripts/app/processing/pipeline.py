# A unified processing pipeline that tracks call.

class ProcessingPipeline:
    def __init__(self):
        self.stages = []  # list of callables

    def add_stage(self, func):
        self.stages.append(func)

    def run(self, data):
        for stage in self.stages:
            data = stage(data)
        return data
