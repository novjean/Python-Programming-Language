from mrjob.job import MRJob

class MRAgeFriendsCounter(MRJob):
    def mapper(self, key, line):
        (userID, name, age, numberOfFriends) = line.split(',')
        yield age, float(numberOfFriends)
        
    def reducer(self, age, numberOfFriends):
        total=0
        numElements=0
        for x in numberOfFriends:
            total += x
            numElements+=1
        yield age, total/numElements
        
if __name__ == '__main__':
    MRAgeFriendsCounter.run()