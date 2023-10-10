import numpy as np

class LSH:
    def __init__(self, num_hash_functions, num_buckets, num_dimensions):
        # Initialize LSH parameters and data structures
        self.num_hash_functions = num_hash_functions
        self.num_buckets = num_buckets
        self.num_dimensions = num_dimensions
        self.hash_tables = [{} for _ in range(num_hash_functions)]  # Create empty hash tables
        self.random_vectors = [np.random.randn(num_dimensions) for _ in range(num_hash_functions)]  # Generate random vectors

    def hash(self, data_point):
        hash_values = []
        for i in range(self.num_hash_functions):
            # Calculate the dot product between a random vector and the data point
            dot_product = np.dot(self.random_vectors[i], data_point)
            # Assign a hash value of 1 if dot product is non-negative, else 0
            hash_value = int(dot_product >= 0)
            hash_values.append(hash_value)
        # Return a tuple of hash values
        return tuple(hash_values)

    def insert(self, data_point):
        # Calculate the hash key for the data point
        hash_key = self.hash(data_point)
        for i in range(self.num_hash_functions):
            table = self.hash_tables[i]
            if hash_key in table:
                # If hash key exists in the hash table, append data_point to the list of data points
                table[hash_key].append(data_point)
            else:
                # If hash key doesn't exist, create a new entry with hash key and data_point as a list
                table[hash_key] = [data_point]

    def query(self, query_point):
        # Calculate the hash key for the query point
        hash_key = self.hash(query_point)
        similar_points = []  # Initialize a list to store similar data points
        for i in range(self.num_hash_functions):
            table = self.hash_tables[i]
            if hash_key in table:
                # If hash key exists in the hash table, extend similar_points with the list of data points
                similar_points.extend(table[hash_key])
        return similar_points

# Example usage:
num_hash_functions = 4
num_buckets = 8
num_dimensions = 10

lsh = LSH(num_hash_functions, num_buckets, num_dimensions)

# Generating random data for demonstration
data = np.random.randn(100, num_dimensions)

# Inserting data points into LSH
for data_point in data:
    lsh.insert(data_point)

# Querying for similar points
query_point = np.random.randn(num_dimensions)
similar_points = lsh.query(query_point)

print("Query Point:")
print(query_point)
print("\nSimilar Points:")
for point in similar_points:
    print(point)
