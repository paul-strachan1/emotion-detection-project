# This is a mock test for the emotion_detection.py file

import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetectorMock(unittest.TestCase):
    @patch('requests.post')
    def test_emotion_detector(self, mock_post):
        # Mock the API response for joy emotion
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.1,"disgust":0.1,"fear":0.1,"joy":0.6,"sadness":0.1}}]}'
        
        # Test case for the joy emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Mock the API response for anger emotion
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.6,"disgust":0.1,"fear":0.1,"joy":0.1,"sadness":0.1}}]}'
        
        # Test case for the anger emotion
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Mock the API response for disgust emotion
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.1,"disgust":0.6,"fear":0.1,"joy":0.1,"sadness":0.1}}]}'
        
        # Test case for the disgust emotion
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # Mock the API response for sadness emotion
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.1,"disgust":0.1,"fear":0.1,"joy":0.1,"sadness":0.6}}]}'
        
        # Test case for the sadness emotion
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
        # Mock the API response for fear emotion
        mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.1,"disgust":0.1,"fear":0.6,"joy":0.1,"sadness":0.1}}]}'
        
        # Test case for the fear emotion
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')
        
        # Test case for empty text (status code 500)
        mock_post.return_value.status_code = 500
        
        # Test case for empty text
        result_6 = emotion_detector('')
        self.assertIsNone(result_6['dominant_emotion'])
        
        # Test case for API error (status code 404)
        mock_post.return_value.status_code = 404
        
        # Test case for API error
        result_7 = emotion_detector('This should cause an API error')
        self.assertIsNone(result_7['dominant_emotion'])

if __name__ == '__main__':
    unittest.main() 