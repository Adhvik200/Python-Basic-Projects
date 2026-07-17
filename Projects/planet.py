class Planet():
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
        
        info = [name, planet_type, star]
        for i in info:
            if not isinstance(i, str):
                raise TypeError('name, planet type, and star must be strings')
            if i == '':
                raise ValueError('name, planet_type, and star must be non-empty strings')
                
        


    def orbit(self):
        
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


planet_1 = Planet('Earth', 'Terrestrial (Rocky)', 'Sun')
planet_2 = Planet('Jupiter', 'Gas Giant', 'Sun')
planet_3 = Planet('Kepler-186f', 'Terrestrial (Rocky)', 'Kepler-186')


print(planet_1)
print(planet_1.orbit())

print(planet_2)
print(planet_2.orbit())

print(planet_3)
print(planet_3.orbit())