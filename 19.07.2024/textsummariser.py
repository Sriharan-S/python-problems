import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    """Summarize the given text."""
    sentences = sent_tokenize(text)

    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    word_freq = FreqDist(filtered_words)
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        score = sum(word_freq[word] for word in sentence_words if word in word_freq)
        sentence_scores[sentence] = score
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    return ' '.join(summary_sentences)

def main():
    text = """Your long text goes here. You can replace this with any text you want to summarize.
              The summarizer will extract the most important sentences based on word frequencies."""
    
    summary = summarize_text(text)
    print("Summary:")
    print(summary)
main()
