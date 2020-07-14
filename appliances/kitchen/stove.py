from appliances import Appliance


class Stove(Appliance):

    def __init__(self, color, heat_method="electric"):
        super().__init__(color)

    def bake_cookies(self):
        print("Your cookies are warm and chewy!")
