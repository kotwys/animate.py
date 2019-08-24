class Graphics:
    def __init__(self, props):
        self.state = props
    
    def update(self, delta):
        pass
    
    def draw(self):
        raise NotImplementedError('draw() needs to be implemented')
