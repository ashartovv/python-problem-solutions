# Challenge 1: Word Chain
#
# Problem Statement:
#
# Given a list of four-character words, find the shortest sequence of words
# connecting a given starting word to a target word.
#
# Two words are considered adjacent if they differ by exactly one character
# at the same position.
#
# Implement the following function:
#
# find_chain_words(words, start_word, end_word, chain=None)
#
# Parameters:
#     words (list[str]): A list of four-character words.
#     start_word (str): The word at which the sequence begins.
#     end_word (str): The word at which the sequence ends.
#     chain (optional): An argument used by the function.
#
# Returns:
#     list[str]: The shortest valid sequence from start_word to end_word,
#     including both words. Return an empty list if no valid sequence exists.
#
# Example:
#
#     start_word = 'муха'
#     end_word = 'слон'
#
#     find_chain_words(words, start_word, end_word)
#
# Expected output:
#
#     ['муха', 'мура', 'тура', 'тара', 'кара', 'каре', 'кафе', 'кафр',
#      'каюр', 'каюк', 'крюк', 'урюк', 'урок', 'срок', 'сток', 'стон', 'слон']
#
# Assignment:
#
# Find the shortest valid sequence connecting 'тара' to 'сухо'.
# Store the result in a variable named chain_result.
#
# Do not print anything to the screen.

def find_neighbors(words, start_word, end_word, visited_words = []):
    found_words = []
    for word in words:
        if word in visited_words:
            continue
        counter = 0
        for index, ch in enumerate(word):
            if ch != start_word[index] and counter <= 1:
                counter += 1
            if counter > 1:
                break
        if counter == 1:
            if word == end_word:
                return [word, ]
            found_words.append(word)
    return found_words

def find_chain_words(words, start_word, end_word, chain=None):
    if start_word == end_word or start_word not in words or end_word not in words:
        return None

    visited_words = [start_word,]
    parents = [start_word,]
    children = [find_neighbors(words, start_word, end_word, visited_words),]
    count = 0
    found = False

    if end_word in children[0]:
        found = True
    elif children[0] == []:
        return None

    while not found:
        local_count = count
        for children_list in children[local_count:]:
            for child in children_list:
                visited_words.append(child)
                result_children = find_neighbors(words, child, end_word, visited_words)
                if end_word in result_children:
                    parents.append(child)
                    children.append(result_children)
                    found = True
                    break

                if result_children:
                    parents.append(child)
                    children.append(result_children)

            if found:
                break

            count += 1

    parents.reverse()
    children.reverse()


    chain = [end_word,]
    for parent_index, child in enumerate(children):
        if chain[-1] in child:
            chain.append(parents[parent_index])
    chain.reverse()

    return chain


words = ['вино', 'сука', 'срок', 'арка', 'тура', 'сова', 'жара', 'день', 'жгут', 'урна', 'заяц', 'зона', 'звук', 'гора',
         'гусь', 'руна', 'суша', 'тара', 'враг', 'арба', 'кара', 'поза', 'бобр', 'икра', 'слон', 'доза', 'знак', 'груз',
         'глаз', 'жаба', 'база', 'дока', 'губа', 'блин', 'жена', 'доля', 'роса', 'бита', 'каюк', 'друг', 'вера', 'заря',
         'дыра', 'буря', 'дача', 'вода', 'кафр', 'дума', 'драп', 'баян', 'суха', 'диво', 'грач', 'дочь', 'брат', 'дуга',
         'каюр', 'крюк', 'звон', 'пола', 'вата', 'град', 'банк', 'рука', 'сока', 'урюк', 'иней', 'дека', 'борт', 'бокс',
         'сухо', 'мура', 'балл', 'врач', 'долг', 'урок', 'стон', 'мука', 'азот', 'лука', 'кафе', 'жест', 'вход', 'волк',
         'муха', 'блок', 'гриф', 'жбан', 'двор', 'дело', 'зима', 'ваза', 'рана', 'сток', 'змея', 'каре', 'горе', 'полк',
         'роза', 'арфа', 'игра']


start_word = "тара"
end_word = "сухо"

chain = find_chain_words(words, start_word, end_word)