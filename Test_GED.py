import jellyfish
import time


def find_correct_words(word):
    correct_words = []
    min_distance = None
    dic_path = "dict.txt"
    try:
        with open(dic_path) as dict:
            for dic_word_line in dict:
                dict_word = dic_word_line.strip()
                curr_distance = jellyfish.levenshtein_distance(word, dict_word)
                if min_distance == None:
                    min_distance = curr_distance
                    correct_words.append(dict_word)
                elif min_distance > curr_distance:
                    min_distance = curr_distance
                    correct_words=[]
                    correct_words.append(dict_word)
                elif min_distance == curr_distance:
                    correct_words.append(dict_word)
    except:
        print("file error 3")
    return correct_words

if __name__ == "__main__":
    start_time = time.time()
    #First, we need to generate a file that contains the correct words of all mispelling words. If the word is correct, then skip.
    #We only calculate the top 500 words
    file_path = "wiki_misspell.txt"
    file_path_result = "wiki_expected_result.txt"

    line_counter =0
    try:
        with open(file_path, 'r') as mis_file, open(file_path_result, 'w') as result_file:
            for word_line in mis_file:
                line_counter += 1
                word = word_line.strip()
                correct_words = find_correct_words(word)
                word_str = ""
                for correct_word in correct_words:
                    word_str += correct_word + " "
                result_file.write(word_str + '\n')
                print(word_str)
                if line_counter == 500:
                    break
    except Exception as e:
        print("File error1")

    #Generate the precision and recall
    file_path_correct = "wiki_correct.txt"
    counter_precision = 0
    counter_recall = 0
    counter_total_precision = 0
    counter_total_recall = 0

    line_counter = 0
    try:
        with open(file_path_correct, 'r') as correct_file, open(file_path_result, 'r') as result_file:
            for word_corr_line in correct_file:
                line_counter += 1
                words_expect = result_file.readline().strip()
                word_correct = word_corr_line.strip()
                if word_correct in words_expect:
                    counter_recall += 1
                    counter_precision += 1
                counter_total_precision += len(words_expect.split(' '))
                counter_total_recall += 1
                if line_counter == 500:
                    break
    except:
        print("File error 2")

    print("precision_counter: " + str(counter_total_precision))
    print("recall_counter: " + str(counter_total_recall))
    print("precision in total: " + str(counter_precision/counter_total_precision) + '\n')
    print("recall in total: " + str(counter_recall/counter_total_recall) + '\n')
    print("time elapsed: " + str(time.time() - start_time))








