import numpy as np

class DataRecognition:
    def __init__(self):
        """
        Initializes the DataRecognition system to treat all data as relevant to IRH.
        """
        self.relevant_data = []  # Store relevant data
        
    def process_data(self, new_data):
        """
        Process incoming data and check for relevance.
        
        :param new_data: New data point to analyze.
        :return: Processed data, ready to be integrated into the model.
        """
        # Simple example: Treat all data as relevant by default.
        print(f"Processing new data: {new_data}")
        self.relevant_data.append(new_data)
        return new_data

    def get_all_data(self):
        """
        Retrieve all relevant data accumulated so far.
        """
        return self.relevant_data


# Example usage
if __name__ == "__main__":
    data_recognition = DataRecognition()
    new_data = [1.0, 2.0, 3.0]
    processed_data = data_recognition.process_data(new_data)
    print(f"All Data: {data_recognition.get_all_data()}")