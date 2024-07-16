from nada_dsl import *

def nada_main():
    questions = [
        "I feel sad or down most of the time.",
        "I often worry about things that might happen in the future.",
        "I find it difficult to concentrate on tasks.",
        "I often feel nervous or on edge.",
        "I have trouble falling or staying asleep."
    ]
    
    weightages = [
        {"depression": 5, "anxiety": 2, "adhd": 0},
        {"depression": 0, "anxiety": 3, "adhd": 0},
        {"depression": 0, "anxiety": 0, "adhd": 3},
        {"depression": 0, "anxiety": 5, "adhd": -3},
        {"depression": 2, "anxiety": 5, "adhd": 0}
    ]

    participant = Party(name="Party1")

    inputs = []
    for i in range(len(questions)):
        a = SecretInteger(Input(name=f"answer_{i}", party=participant))
        inputs.append(a)

    scores = {}
    for disorder in ["depression", "anxiety", "adhd"]:
        scores[disorder] = Integer(0)
        for i in range(len(questions)):
            score_i = inputs[i] * Integer(weightages[i][disorder])
            scores[disorder] += score_i

    results = []
    for disorder in ["depression", "anxiety", "adhd"]:
      disorder_max = Integer(0)
      for weights in weightages:
        disorder_max += Integer(abs(weights[disorder]))
      results.append(Output((scores[disorder]) / disorder_max, f"{disorder}_score", participant))


    return results
 