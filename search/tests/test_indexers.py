# coding: utf-8

from datetime import date, datetime
import unittest

from search import indexers


class BaseTest(object):
    kwargs = {}

    def indexer(self):
        return None

    def assert_indexed(self, string, expected):
        indexer = self.indexer()
        actual = indexer(string, **self.kwargs)
        self.assertEqual(sorted(actual), sorted(expected))

    def setUp(self):
        self.kwargs = {}

    tearDown = setUp


class StartswithTest(BaseTest, unittest.TestCase):
    def indexer(self):
        return indexers.startswith

    def test_1(self):
        string = u'hello'
        expected = [
            u'h',
            u'he',
            u'hel',
            u'hell',
            u'hello',
        ]
        self.assert_indexed(string, expected)

    def test_2(self):
        string = u'HOwDy'
        expected = [
            u'H',
            u'HO',
            u'HOw',
            u'HOwD',
            u'HOwDy',
        ]
        self.assert_indexed(string, expected)

    def test_3(self):
        string = u'these are words'
        expected = [
            u'a',
            u'ar',
            u'are',
            u't',
            u'th',
            u'the',
            u'thes',
            u'these',
            u'thesea',
            u'thesear',
            u'theseare',
            u'thesearew',
            u'thesearewo',
            u'thesearewor',
            u'theseareword',
            u'thesearewords',
            u'w',
            u'wo',
            u'wor',
            u'word',
            u'words',
        ]
        self.assert_indexed(string, expected)

    def test_4(self):
        string = u'buenas días'
        expected = [
            u'b',
            u'bu',
            u'bue',
            u'buen',
            u'buena',
            u'buenas',
            u'buenasd',
            u'buenasdi',
            u'buenasdia',
            u'buenasdias',
            u'buenasdí',
            u'buenasdía',
            u'buenasdías',
            u'd',
            u'di',
            u'dia',
            u'dias',
            u'dí',
            u'día',
            u'días',
        ]
        self.assert_indexed(string, expected)

    def test_5(self):
        string = u'with-punctuation'
        expected = [
            u'p',
            u'pu',
            u'pun',
            u'punc',
            u'punct',
            u'punctu',
            u'punctua',
            u'punctuat',
            u'punctuati',
            u'punctuatio',
            u'punctuation',
            u'w',
            u'wi',
            u'wit',
            u'with',
            u'withp',
            u'withpu',
            u'withpun',
            u'withpunc',
            u'withpunct',
            u'withpunctu',
            u'withpunctua',
            u'withpunctuat',
            u'withpunctuati',
            u'withpunctuatio',
            u'withpunctuation',
        ]
        self.assert_indexed(string, expected)

    def test_6(self):
        self.kwargs['min_size'] = 2
        string = u'pomodoro'
        expected = [
            u'po',
            u'pom',
            u'pomo',
            u'pomod',
            u'pomodo',
            u'pomodor',
            u'pomodoro',
        ]

        self.assert_indexed(string, expected)
    
    def test_7(self):
        self.kwargs['max_size'] = 7
        string = u'lamentablamente, egészségére'
        expected = [
            u'e',
            u'eg',
            u'ege',
            u'eges',
            u'egesz',
            u'egeszs',
            u'egeszse',
            u'egé',
            u'egés',
            u'egész',
            u'egészs',
            u'egészsé',
            u'l',
            u'la',
            u'lam',
            u'lame',
            u'lamen',
            u'lament',
            u'lamenta',
        ]
        self.assert_indexed(string, expected)

    def test_8(self):
        self.kwargs['min_size'] = 3
        self.kwargs['max_size'] = 5
        string = u'hablamos things'
        expected = ['thing', 'hab', 'habl', 'habla', 'thi',
            'thin']

        self.assert_indexed(string, expected)


class ContainsTest(BaseTest, unittest.TestCase):
    def indexer(self):
        return indexers.contains

    def test_1(self):
        string = u'hello'
        expected = [
            u'e',
            u'el',
            u'ell',
            u'ello',
            u'h',
            u'he',
            u'hel',
            u'hell',
            u'hello',
            u'l',
            u'll',
            u'llo',
            u'lo',
            u'o',
        ]
        self.assert_indexed(string, expected)

    def test_2(self):
        string = u'HOwDy'
        expected = [
            u'D',
            u'Dy',
            u'H',
            u'HO',
            u'HOw',
            u'HOwD',
            u'HOwDy',
            u'O',
            u'Ow',
            u'OwD',
            u'OwDy',
            u'w',
            u'wD',
            u'wDy',
            u'y',
        ]

        self.assert_indexed(string, expected)

    def test_3(self):
        string = u'these are words'
        expected = [
            u'a',
            u'ar',
            u'are',
            u'arew',
            u'arewo',
            u'arewor',
            u'areword',
            u'arewords',
            u'd',
            u'ds',
            u'e',
            u'ea',
            u'ear',
            u'eare',
            u'earew',
            u'earewo',
            u'earewor',
            u'eareword',
            u'earewords',
            u'es',
            u'ese',
            u'esea',
            u'esear',
            u'eseare',
            u'esearew',
            u'esearewo',
            u'esearewor',
            u'eseareword',
            u'esearewords',
            u'ew',
            u'ewo',
            u'ewor',
            u'eword',
            u'ewords',
            u'h',
            u'he',
            u'hes',
            u'hese',
            u'hesea',
            u'hesear',
            u'heseare',
            u'hesearew',
            u'hesearewo',
            u'hesearewor',
            u'heseareword',
            u'hesearewords',
            u'o',
            u'or',
            u'ord',
            u'ords',
            u'r',
            u'rd',
            u'rds',
            u're',
            u'rew',
            u'rewo',
            u'rewor',
            u'reword',
            u'rewords',
            u's',
            u'se',
            u'sea',
            u'sear',
            u'seare',
            u'searew',
            u'searewo',
            u'searewor',
            u'seareword',
            u'searewords',
            u't',
            u'th',
            u'the',
            u'thes',
            u'these',
            u'thesea',
            u'thesear',
            u'theseare',
            u'thesearew',
            u'thesearewo',
            u'thesearewor',
            u'theseareword',
            u'thesearewords',
            u'w',
            u'wo',
            u'wor',
            u'word',
            u'words',
        ]
        self.assert_indexed(string, expected)

    def test_4(self):
        string = u'buenas días'
        expected = [
            u'a',
            u'as',
            u'asd',
            u'asdi',
            u'asdia',
            u'asdias',
            u'asdí',
            u'asdía',
            u'asdías',
            u'b',
            u'bu',
            u'bue',
            u'buen',
            u'buena',
            u'buenas',
            u'buenasd',
            u'buenasdi',
            u'buenasdia',
            u'buenasdias',
            u'buenasdí',
            u'buenasdía',
            u'buenasdías',
            u'd',
            u'di',
            u'dia',
            u'dias',
            u'dí',
            u'día',
            u'días',
            u'e',
            u'en',
            u'ena',
            u'enas',
            u'enasd',
            u'enasdi',
            u'enasdia',
            u'enasdias',
            u'enasdí',
            u'enasdía',
            u'enasdías',
            u'i',
            u'ia',
            u'ias',
            u'n',
            u'na',
            u'nas',
            u'nasd',
            u'nasdi',
            u'nasdia',
            u'nasdias',
            u'nasdí',
            u'nasdía',
            u'nasdías',
            u's',
            u'sd',
            u'sdi',
            u'sdia',
            u'sdias',
            u'sdí',
            u'sdía',
            u'sdías',
            u'u',
            u'ue',
            u'uen',
            u'uena',
            u'uenas',
            u'uenasd',
            u'uenasdi',
            u'uenasdia',
            u'uenasdias',
            u'uenasdí',
            u'uenasdía',
            u'uenasdías',
            u'í',
            u'ía',
            u'ías',
        ]
        self.assert_indexed(string, expected)

    def test_5(self):
        string = u'with-punctuation'
        expected = [
            u'a',
            u'at',
            u'ati',
            u'atio',
            u'ation',
            u'c',
            u'ct',
            u'ctu',
            u'ctua',
            u'ctuat',
            u'ctuati',
            u'ctuatio',
            u'ctuation',
            u'h',
            u'hp',
            u'hpu',
            u'hpun',
            u'hpunc',
            u'hpunct',
            u'hpunctu',
            u'hpunctua',
            u'hpunctuat',
            u'hpunctuati',
            u'hpunctuatio',
            u'hpunctuation',
            u'i',
            u'io',
            u'ion',
            u'it',
            u'ith',
            u'ithp',
            u'ithpu',
            u'ithpun',
            u'ithpunc',
            u'ithpunct',
            u'ithpunctu',
            u'ithpunctua',
            u'ithpunctuat',
            u'ithpunctuati',
            u'ithpunctuatio',
            u'ithpunctuation',
            u'n',
            u'nc',
            u'nct',
            u'nctu',
            u'nctua',
            u'nctuat',
            u'nctuati',
            u'nctuatio',
            u'nctuation',
            u'o',
            u'on',
            u'p',
            u'pu',
            u'pun',
            u'punc',
            u'punct',
            u'punctu',
            u'punctua',
            u'punctuat',
            u'punctuati',
            u'punctuatio',
            u'punctuation',
            u't',
            u'th',
            u'thp',
            u'thpu',
            u'thpun',
            u'thpunc',
            u'thpunct',
            u'thpunctu',
            u'thpunctua',
            u'thpunctuat',
            u'thpunctuati',
            u'thpunctuatio',
            u'thpunctuation',
            u'ti',
            u'tio',
            u'tion',
            u'tu',
            u'tua',
            u'tuat',
            u'tuati',
            u'tuatio',
            u'tuation',
            u'u',
            u'ua',
            u'uat',
            u'uati',
            u'uatio',
            u'uation',
            u'un',
            u'unc',
            u'unct',
            u'unctu',
            u'unctua',
            u'unctuat',
            u'unctuati',
            u'unctuatio',
            u'unctuation',
            u'w',
            u'wi',
            u'wit',
            u'with',
            u'withp',
            u'withpu',
            u'withpun',
            u'withpunc',
            u'withpunct',
            u'withpunctu',
            u'withpunctua',
            u'withpunctuat',
            u'withpunctuati',
            u'withpunctuatio',
            u'withpunctuation',
        ]
        self.assert_indexed(string, expected)

    def test_6(self):
        self.kwargs['min_size'] = 2
        string = u'pomodoro'
        expected = [
            u'do',
            u'dor',
            u'doro',
            u'mo',
            u'mod',
            u'modo',
            u'modor',
            u'modoro',
            u'od',
            u'odo',
            u'odor',
            u'odoro',
            u'om',
            u'omo',
            u'omod',
            u'omodo',
            u'omodor',
            u'omodoro',
            u'or',
            u'oro',
            u'po',
            u'pom',
            u'pomo',
            u'pomod',
            u'pomodo',
            u'pomodor',
            u'pomodoro',
            u'ro',
        ]
        self.assert_indexed(string, expected)
    
    def test_7(self):
        self.kwargs['max_size'] = 4
        string = u'forrest'
        expected = [
            u'e',
            u'es',
            u'est',
            u'f',
            u'fo',
            u'for',
            u'forr',
            u'o',
            u'or',
            u'orr',
            u'orre',
            u'r',
            u're',
            u'res',
            u'rest',
            u'rr',
            u'rre',
            u'rres',
            u's',
            u'st',
            u't',
        ]
        self.assert_indexed(string, expected)


class FirstletterTest(BaseTest, unittest.TestCase):

    def indexer(self):
        return indexers.firstletter

    def test_1(self):
        string = u'hello'
        expected = [u'h']

        self.assert_indexed(string, expected)

    def test_2(self):
        string = u'HOwDy'
        expected = [u'H']

        self.assert_indexed(string, expected)

    def test_3(self):
        string = u'the words'
        expected = [u'w']

        self.kwargs['ignore'] = ['the']
        self.assert_indexed(string, expected)

    def test_4(self):
        string = u'a the framboise'
        expected = [u'f']

        self.kwargs['ignore'] = ['a', 'the']
        self.assert_indexed(string, expected)

    def test_5(self):
        string = u'The museum'
        expected = [u'm']

        self.kwargs['ignore'] = ['the']
        self.assert_indexed(string, expected)
