import re
import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, ArrayDictionary, StopWordRemover
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class TextPreprocessor:
    def __init__(self):
        self.emoji_dict = {
            "❤️": "cinta", "🧡": "cinta", "💛": "cinta", "💚": "cinta",
            "💙": "cinta", "💜": "cinta", "🖤": "cinta", "🤍": "cinta",
            "🤎": "cinta", "💖": "cinta", "💗": "cinta", "💘": "cinta",
            "💝": "cinta", "💞": "cinta", "💕": "cinta", "💓": "cinta",
            "💟": "cinta", "❣️": "cinta", "♥️": "cinta",
            "😍": "cinta", "🥰": "cinta", "😘": "cinta", "😗": "cinta",
            "😙": "cinta", "😚": "cinta", "💋": "cinta",
            "🫶": "cinta", "🫶🏻": "cinta", "🫶🏼": "cinta", "🫶🏽": "cinta",
            "🫶🏾": "cinta", "🫶🏿": "cinta", "😻": "cinta", "👍": "bagus",

            "😂": "lucu",   "🤣": "lucu",   "😹": "lucu",
            "😄": "senang", "😃": "senang", "😀": "senang",
            "😁": "senang", "😆": "senang", "😊": "senang",
            "🙂": "senang", "☺️": "senang", "😇": "senang",
            "🥳": "senang", "😸": "senang",

            "😢": "sedih", "😭": "sedih", "😿": "sedih",
            "😞": "sedih", "😔": "sedih", "☹️": "sedih",
            "🙁": "sedih", "😟": "sedih", "🥺": "sedih",
            "💔": "kecewa",

            "😡": "marah", "😠": "marah", "🤬": "marah",
            "😤": "marah", "👿": "marah",

            "😱": "kaget", "😨": "takut", "😰": "takut",
            "😥": "takut", "😓": "takut",

            "😐": "netral", "😑": "netral", "😶": "diam",
            "🤔": "bingung", "😕": "bingung", "😵": "bingung",

            "👍": "bagus", "👍🏻": "bagus", "👍🏼": "bagus",
            "👍🏽": "bagus", "👍🏾": "bagus", "👍🏿": "bagus",
            "👌": "bagus", "👏": "bagus", "🙌": "bagus",
            "💪": "semangat", "🔥": "keren", "✨": "keren",

            "👎": "buruk", "👎🏻": "buruk", "👎🏼": "buruk",
            "👎🏽": "buruk", "👎🏾": "buruk", "👎🏿": "buruk",

            "🤢": "jijik", "🤮": "jijik",

            "😴": "ngantuk", "🥱": "ngantuk", "😪": "ngantuk",

            "🙏": "terima_kasih", "🙏🏻": "terima_kasih",
            "🙏🏼": "terima_kasih", "🙏🏽": "terima_kasih",
            "🙏🏾": "terima_kasih", "🙏🏿": "terima_kasih"
        }

        self.slang_dict = {
            'yg': 'yang', 'ga': 'tidak', 'gak': 'tidak',
            'lo': 'kamu', 'gw': 'saya', 'aja': 'saja',
            'bgt': 'banget', 'skr': 'sekarang', 'lg': 'lagi',
            'dll': 'dan lain-lain', 'sm': 'sama', 'cakeupp': 'cakep',

            'klo': 'kalau', 'kalo': 'kalau',
            'tp': 'tapi', 'tpi': 'tapi',
            'bkn': 'bukan',
            'udh': 'sudah', 'udah': 'sudah',
            'jd': 'jadi', 'jdi': 'jadi',
            'sdh': 'sudah',
            'dgn': 'dengan',
            'knp': 'kenapa',
            'msh': 'masih',
            'tau': 'tahu',
            'tdk': 'tidak',
            'gk': 'tidak',
            'hrs': 'harus',

            'lu': 'kamu', 'elu': 'kamu',
            'gue': 'saya', 'ane': 'saya',
            'nyah': 'nya', 'deseu': 'dia',
            'seseorang': 'orang',
            'ertong': 'artis',
            'min': 'admin', 'mimin': 'admin',

            'emg': 'emang', 'memang': 'memang', 'org': 'orang',
            'bener': 'benar',
            'skali': 'sekali', 'skr': 'sekarang',
            'bangettt': 'banget',
            'pake': 'pakai',
            'pakek': 'pakai',
            'liat': 'lihat',
            'liatnya': 'lihatnya',
            'aj': 'saja', 'ajah': 'saja', 'kmrn': 'kemarin',
            'kayakgni': 'seperti ini', 'belajaer': 'belajar',
            'permpuan': 'perempuan',

            'goblok': 'bodoh', 'goblog': 'bodoh',
            'bego': 'bodoh', 'jutek': 'cuek',
            'tolol': 'bodoh', 'geblek': 'bodoh', 'bodo':'bodoh', 'tai':'jelek',
        }

        factory_stopword = StopWordRemoverFactory()
        self.stopword    = factory_stopword.get_stop_words()

        if 'tidak' in self.stopword:
            self.stopword.remove('tidak')

        if 'bukan' in self.stopword:
            self.stopword.remove('bukan')

        dictionary = ArrayDictionary(self.stopword)
        self.stopword_remover = StopWordRemover(dictionary)

        factory_stemmer = StemmerFactory()
        self.stemmer = factory_stemmer.create_stemmer()

    def emoji_to_indonesian(self, text):
        if isinstance(text, str):
            for emo, arti in self.emoji_dict.items():
                text = text.replace(emo, f" {arti} ")
        return text    

    def clean_text(self, text):
        text = re.sub(r'@[\w]+', 'username', text)
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'(.)\1{2,}', r'\1', text)
        text = ' '.join([w for w in text.split() if 2 <= len(w) <= 15])
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)
        return text.lower()

    def normalize_text(self, text):
        return " ".join([self.slang_dict.get(word, word) for word in text.split()])
    
    def tokenize_text(self, text):
        if isinstance(text, str):
            return word_tokenize(text)
        return text

    def remove_stopword(self, tokens):
        if isinstance(tokens, list):
            return [word for word in tokens if word not in self.stopword ]
        return tokens

    def stemmer_text(self, tokens):
        if isinstance(tokens, list):
            return [self.stemmer.stem(word) for word in tokens]
        return tokens

    def preprocessed(self, text):
        text = self.emoji_to_indonesian(text)
        text = self.clean_text(text)
        text = self.normalize_text(text)
        text = self.tokenize_text(text)
        text = self.remove_stopword(text)
        text = self.stemmer_text(text)
        
        if isinstance(text, list):
            text = ' '.join(text)

        return text