import copy

def get_score(actual, predicted):
    actual_tokens = copy.deepcopy(actual)
    predicted_tokens = copy.deepcopy(predicted)
    
    correct_tokens_count = 0
    actual_tokens_count = len(actual_tokens)

    while (len(actual_tokens) != 0) and (len(predicted_tokens) != 0):
        s1 = actual_tokens.pop(0)
        s2 = predicted_tokens.pop(0)
        
        matched = True

        while_counter = 0
        while s1 != s2 and ((len(actual_tokens) != 0) and (len(predicted_tokens) != 0)):
            matched = False
            
            if len(s1) < len(s2):
                s1 = s1 + actual_tokens.pop(0)
            elif len(s1) > len(s2):
                s2 = s2 + predicted_tokens.pop(0)
            
            while_counter += 1

            if while_counter > 10000:
                break
        
        if matched:
            correct_tokens_count += 1

    return correct_tokens_count, actual_tokens_count


def get_scores(actuals, predictions):
    assert len(actuals) == len(predictions)
   
    total_correct = 0
    total_tokens = 0
    wrong_indexes = []

    for i in range(len(actuals)):
        correct, tokens = get_score(actuals[i], predictions[i])
        total_correct += correct
        total_tokens += tokens
        if correct != tokens:
            wrong_indexes.append(i)
    
    return total_correct, total_tokens, wrong_indexes


def main():
    # test get_score()
    t1 = "Buku nya mahal .".split(" ")
    t2 = "Bukunya mahal .".split(" ")
    print(get_score(t1, t2))

    t1 = "Seharusnya kamu tidak terlambat !".split(" ")
    t2 = "Seharus nya kamu tidak terlambat !".split(" ")
    print(get_score(t1, t2))

    t1 = "Bukan kah itu benar ?".split(" ")
    t2 = "Bukankah itu benar ?".split(" ")
    print(get_score(t1, t2))

    t1 = "Punyanya membeli nya kemarin".split(" ")
    t2 = "Punya nya membelinya kemarin".split(" ")
    print(get_score(t1, t2))

    t1 = "Punyanya membeli nya kemarin".split(" ")
    t2 = "Punyanya mem belinya kemarin".split(" ")
    print(get_score(t1, t2))

    t1 = ['Wright', 'adalah', 'teman', 'sesama', 'direktur', 'Garth', 'Jennings', ',', 'dan', 'tampil', 'cameo', 'dalam', 'film', 'nya', 'The', 'Hitchhiker', "'s", 'Guide', 'to', 'the', 'Galaxy', 'dan', 'Son', 'of', 'Rambow', '.']
    t2 = ['Wright', 'adalah', 'teman', 'sesama', 'direktur', 'Garth', 'Jennings', ',', 'dan', 'tampil', 'cameo', 'dalam', 'filmnya', 'The', 'Hitchhiker', "'s ", 'Guide', 'to', 'the', 'Galaxy', 'dan', 'Son', 'of', 'Rambow', '.']
    print(get_score(t1, t2))

    t1 = ['David', 'Lyall', ',', 'penghuni', 'satu', 'nya', 'dari', 'pulau', 'Stephen', ',', 'mengirimkan', 'suatu', 'eksemplar', 'ke', 'museum', 'di', 'Wellington', '.']
    t2 = ['David', 'Lyall', ',', 'penghuni', 'satu-satunya', 'dari', 'pulau', 'Stephen', ',', 'mengirimkan', 'suatu', 'eksemplar', 'ke', 'museum', 'di', 'Wellington', '.']
    print(get_score(t1, t2))

    # test get_scores()
    gold_standard = [
        "Buku nya mahal .".split(" "),
        "Seharusnya kamu tidak terlambat !".split(" "),
        "Bukan kah itu benar ?".split(" "),
    ]
    
    tokenizer_output = [
        "Bukunya mahal .".split(" "),
        "Seharus nya kamu tidak terlambat !".split(" "),
        "Bukankah itu benar ?".split(" "),
    ]
    
    print(get_scores(gold_standard, tokenizer_output))


if __name__ == '__main__':
    main()
