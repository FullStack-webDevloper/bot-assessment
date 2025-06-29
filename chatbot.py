# import pickle

# # Load trained model (if any)
# with open("chatbot_model.pkl", "rb") as f:
#     model = pickle.load(f)
# user_input = "What is the capital of France?"
# def get_response(user_input):
#     # Example: return model prediction
#     return model.predict([user_input])[0]
def get_response(message):
    if "capital" in message.lower():
        return "The capital of France is Paris."
    elif "cloud" in message.lower():
        return "They use AWS."
    elif "database" in message.lower():
        return "They use MongoDB."
    else:
        return "Sorry, I don't have that information."