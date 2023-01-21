

class Battery:
    
    def __init__(self, max_capacity, current_capacity = -1):
        if(current_capacity == -1):
            self.current_capacity = max_capacity
        else:
            self.current_capacity = current_capacity
            
        self.max_capacity = max_capacity
        
    def get_capacity(self):
        return self.current_capacity
    
    def update(self, change):
        self.current_capacity += change