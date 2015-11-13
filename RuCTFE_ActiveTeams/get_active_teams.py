from html.parser import HTMLParser


class ScoreBoardParser(HTMLParser):

    extract_score = 0
    score = 0.0
    ip = ""
    list = open('./ips.txt', 'w')

    def handle_starttag(self, tag, attrs):
        if tag == "span" and attrs:
            if attrs[0][0] == "title":
                self.ip = attrs[0][1]
        elif tag == "td" and attrs:
            if attrs[0][1] == "team-score":
                self.extract_score = 1
            else:
                self.extract_score = 0

    def handle_data(self, data):
        if self.extract_score == 1:
            self.score = data
            if self.score != "0.00":
                self.list.write(str(self.ip) + "\n")
                print(self.ip)
                self.ip = ""
                self.score = 0.00
                self.extract_score = 0

    def handle_endtag(self, tag):
        pass

    def error(self, message):
        pass


if __name__ == "__main__":
    file = open('./scoreboard2.html', 'r')
    parser = ScoreBoardParser()
    parser.feed(file.read())
    parser.list.close()
    file.close()

    print("Start cleanup")

    index = 0
    file = open('./ips.txt', 'r')
    lines = file.readlines()
    file.close()
    file = open('./ips.txt', 'w')
    for line in lines:
        if line[0] == "1":
            file.write(line)
