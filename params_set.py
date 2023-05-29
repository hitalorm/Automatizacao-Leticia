class parameters:
    def __init__(self, age, z_distance, energy, seed1, seed2):
        self.age = age
        self.z_distance = z_distance
        self.energy = energy
        self.seed1 = seed1
        self.seed2 = seed2
        self.geo = 0
        self.result = 0
        self.error = 0

    def set_files(self):
        #string_mat = str(int(self.gland_prop*100))
        #self.gland_mat = 'breast_g'+string_mat+'.mat'
        string_age = str(int(self.age))
        self.geo = 'geometry'+string_age+'.geo'
        
