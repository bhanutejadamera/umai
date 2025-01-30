# src/distributed_execution/spark_executor.py
from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression

class SparkExecutor:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("UMAI Distributed Execution") \
            .getOrCreate()

    def train_model(self, data):
        """Train a simple ML model using Spark."""
        df = self.spark.createDataFrame(data, ["features", "label"])
        lr = LogisticRegression(maxIter=10, regParam=0.01)
        model = lr.fit(df)
        return model

    def stop(self):
        self.spark.stop()

# Example usage
if __name__ == "__main__":
    executor = SparkExecutor()
    data = [(Vectors.dense([1.0, 2.0]), 1.0), (Vectors.dense([3.0, 4.0]), 0.0)]
    model = executor.train_model(data)
    print("Model trained:", model)
    executor.stop()