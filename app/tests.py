from django.test import SimpleTestCase

# Create your tests here.

class TestStringTimes(SimpleTestCase):
    def test_hi_5_times(self):
        response = self.client.get("/Warmup-2/String-times/hi/5")
        self.assertContains(response, "hihihihihi")
    
    def test_this_10_times(self):
        response = self.client.get("/Warmup-2/String-times/this/10")
        self.assertContains(response, "thisthisthisthisthisthisthisthisthisthis")

    def test_one_1_time(self):
        response = self.client.get("/Warmup-2/String-times/one/1")
        self.assertContains(response, "one")

class TestCountHi(SimpleTestCase):
    def test_hi_alone(self):
        response = self.client.get("/String-2/count_hi/hi")
        self.assertContains(response, 1)
    
    def test_hi_in_gibberish(self):
        response = self.client.get("/String-2/count_hi/heqwtoidhsakfjehihqweroi")
        self.assertContains(response, 1)

    def test_hi_several_times_in_gibberish(self):
        response = self.client.get("/String-2/count_hi/hehiqwtoidhsakfjehihqwhierhioi")
        self.assertContains(response, 4)

class TestCountCode(SimpleTestCase):
    def test_code_alone(self):
        response = self.client.get("/String-2/count-code/code")
        self.assertContains(response, 1)

    def test_code_in_gibberish(self):
        response = self.client.get("/String-2/count-code/alhseiohqweohfocxcodeh3ewqori")
        self.assertContains(response, 1)

    def test_several_inexact_codes_in_gibberish(self):
        response = self.client.get("/String-2/count-code/alhseicoleohqweohfocxcomeh3ewqocoperi")
        self.assertContains(response, 3)