from matplotlib import pyplot as plt
import string


def process_line(line, data):
    line = line.replace('-', ' ')
    for word in line.solit():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        data[word] = data.get(word, 0) + 1


def process_file(file_path):
    data = {}
    with open('story.txt', 'r') as f:
        for line in f:  # 每次取一行
            process_line(line, data)
    hist=[]
    for key,value in data.items():
        hist.append([value,key])
    hist.sort(reverse=True)
    return(hist)

def run(n):
    hist=process_file('story.txt')
    for item in hist[:n]:
        plt.bar((item[1],),(item[0],))
    plt.legend()
    plt.xlabel('word')
    plt.ylabel('rata')
    plt.title('asdasdsa')


if __name__ == '__main__':
    run(10)
