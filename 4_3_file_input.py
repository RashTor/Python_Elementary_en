from collections import Counter


def word_freq(file_name):
    file_input = open(file_name)
    file_dict = file_input.read().replace('\n', ' ').replace('\t', ' ').split(' ')
    file_input.close()
    for word_num in xrange(len(file_dict)-1,0,-1):
        if file_dict[word_num] == '':
            file_dict.pop(word_num)
    return len(file_dict),Counter(file_dict).most_common(1)

def char_count_fun(file_name):
    file_input = open(file_name)
    char_count = len(file_input.read())
    file_input.close()
    return char_count

def main():
    text_file_name = 'test_text.txt'
    char_count = char_count_fun(text_file_name)
    num_word,most_freq_word = word_freq(text_file_name)
    print "\t\t\t\tStatistics of a {} file\n".format(text_file_name), \
        "Number of characters is : {}\nNumber of word is : {}\nMost" \
        " frequent word is : '{}'".format(char_count, num_word, most_freq_word[0][0])


if __name__ == '__main__':
    main()