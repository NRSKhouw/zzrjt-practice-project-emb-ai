from SentimentAnalysis.sentiment_analysis import sentiment_analyser
import unittest

class TestSentimentAnalyser(unittest.TestCase):
    def test_sentiment_analyser(self):
        result_1 = sentiment_analyser('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

        result_2 = sentiment_analyser('I hate working with Python')
        self.assertEqual(result_1['label'], 'SENT_NEGATIVE')

        result_1 = sentiment_analyser('I am neutral on Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')

unittest.main()