from app import *
import unittest

class Test_home_page(unittest.TestCase):
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"Hello, this is the homepage. To find a random recipe, go type /number after the current URL where number is the amount of random recipes you want.", response.data)

class Test_get_random(unittest.TestCase):
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/1', follow_redirects=True)
        self.assertEqual(b'''9220 - Sweet Ricotta Pastries - Bring milk and zest to a simmer in a small heavy saucepan, then remove from heat. Whisk together yolk, sugar, cornstarch, and a pinch of salt in a bowl. Whisk in milk, then transfer mixture to saucepan.\nBring to a boil over medium heat, whisking constantly, and boil 1 minute. Stir in vanilla, then transfer to a clean bowl and chill custard, its surface covered with parchment paper (to prevent a skin from forming), until cold, at least 1 hour. Discard zest.\nPulse ricotta in a food processor until smooth. Whisk into custard. Stir in orange-flower water and citron. Chill until ready to use.\nPulse flour, sugar, and salt in cleaned food processor until combined. Add butter and zest and pulse until mixture resembles coarse meal with some roughly pea-size butter lumps. Add yolks and water and pulse until just incorporated and dough begins to form large clumps.\nTurn out dough onto a work surface and divide into 4 portions. With heel of your hand, smear each portion once or twice in a forward motion to help distribute fat. Gather dough together, using a pastry or bench scraper if you have one, and form into a ball.\nGenerously butter muffin cups and top of pan. Press 2 tablespoon dough over bottom and up side of each muffin cup in an even layer with well-floured fingers. Chill until firm, about 30 minutes.\nMeanwhile, roll out remaining dough between 2 sheets of parchment paper into a 9-inch round (about 1/8 inch thick) and transfer to a baking sheet, discarding top sheet of paper. Cut 12 (1/2-inch-wide) strips, then cut in half crosswise to make 24 strips total. Chill until ready to use.\nSpoon a scant 2 tablespoons filling into each muffin cup and smooth, then crisscross 2 strips on top of filling, trimming to fit. Brush pastry cross with egg wash. Bake until filling is puffed and starting to crack and edges are golden, 25 to 30 minutes.\nCool in pan on a rack 10 minutes. Invert a rack on top of pan, then flip pan and remove. Turn pastries right side up and cool completely. - ['1/2 cup whole milk', '2 (3-by 1-inch) strips orange zest', '1 large egg yolk', '3 tablespoons sugar', '1 tablespoon cornstarch', '1/2 teaspoon pure vanilla extract', '1/2 pound fresh ricotta', '3/4 teaspoon orange-flower water', '2 tablespoons finely chopped candied citron', '2 1/4 cups all-purpose flour', '6 tablespoons sugar', '1/2 teaspoon salt', '2 sticks cold unsalted butter, cut into pieces', '1/2 teaspoon grated orange zest', '2 large egg yolks', '2 tablespoons cold water', '1 large egg beaten with 1 tablespoon water', 'Equipment: a nonstick muffin pan with 12 (1/2-cup) cups', 'Garnish: confectioners sugar for dusting']''', response.data)
class test_route_404(unittest.TestCase):
    def test_route_404(self):
        self.app = app.test_client()
        response = self.app.get('/0/1/2', follow_redirects=True)
        self.assertEqual(b'Sorry, wrong format. Type /number after the current URL where number is the amount of random recipes you want.', response.data)

class test_route_500(unittest.TestCase):
    def test_route_500(self):
        self.app = app.test_client()
        response = self.app.get('/a', follow_redirects=True)
        self.assertEqual(b'Eek, a bug!', response.data)

if __name__ == '__main__':
    unittest.main()

