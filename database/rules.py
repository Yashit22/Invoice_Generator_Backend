class Rules:

    @staticmethod
    def add(data, cluster, database, collection):
        return cluster[database][collection].insert_one(data)

    @staticmethod
    def get(query, cluster, database, collection):
        return cluster[database][collection].find_one(query)
    
    @staticmethod
    def get_all(query, cluster, database, collection):
        return cluster[database][collection].find(query)
