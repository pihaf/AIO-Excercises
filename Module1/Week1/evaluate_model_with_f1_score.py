# Function to define metrics and use them to evaluate models
def evaluate_classification_model(tp, fp, fn):
    # Check if type int
    if not isinstance(tp, int):
        print("tp must be int")
        return 
    if not isinstance(fp, int):
        print("fp must be int")
        return 
    if not isinstance(fn, int):
        print("fn must be int")
        return
    
    # Check if greater than zero
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    
    # Calculate metrics
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)
    
    print("Precision is", precision)
    print("Recall is", recall)
    print("F1-score is", f1_score)
    return
