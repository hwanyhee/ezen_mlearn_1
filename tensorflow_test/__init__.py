from tensorflow_test.mammal import  Mammal
from tensorflow_test.word_sequence import WordSequence
from tensorflow_test.naive_bayes import NaiveBayes
from tensorflow_test.web_crawler import  WebCrawler
from tensorflow_test.mail_checker_ctrl import MailCheckerController

if __name__ == '__main__':
    #t = Mammal()
    #t.execute()
    #WordSequence.execute()

    #review=WebCrawler.create_model()
    #nb = NaiveBayes()
    #원래는 리뷰 글을 크롤링 해서 가져와서 train()함수에 넘겨준다.

    #nb.train('./data/review_train.csv')

    #print(nb.classify('내 인생에서 쓰레기 같은 영화'))  #0.09916030968366302
    #print(nb.classify('내 인생에서 최고의 영화')) #0.966113748742778

    ctrl = MailCheckerController()
    ctrl.run()

