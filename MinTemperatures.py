from mrjob.job import MRJob

class MRMinTemperatures(MRJob):
    def makeFahrenheit(self, tenthOfCelsius):
        celsius = float(tenthOfCelsius)/10.0
        fahrenheit = celsius * 1.8 +32.0
        return fahrenheit
    
    def mapper(self,_,line):
        (location, date, type, data, x,y,z,w)=line.split(',')
        if (type=='TMIN'):
            temperature=self.makeFahrenheit(data)
            yield location, temperature
            
    def reducer(self, location, temps):
        yield location,min(temps)
        
if __name__ == '__main__':
    MRMinTemperatures.run()