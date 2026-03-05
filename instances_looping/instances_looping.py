class Post:
    """ Post class for representing and manipulating posts. """

    caption = "hahahahha" # Class Variable.
    instances = []
    def __init__(self, image: str) -> None: # Constructor (with parameters). # storing part
        """ Create a new post. """
        self.image = image
        self.caption = self.caption
        Post.instances.append(self)

    # Methods
    def get_caption(self) -> str:
        return self.caption

    def get_image(self) -> str:
        return self.image

    def set_caption(self, caption: str) -> None:
        self.caption = caption

    def set_image(self, image: str) -> None:
        self.image = image

    def __str__(self) -> str: # Overrides the __str__ method.  # translating part
        return ("Image directory = {}, Caption = {}".format(self.image, self.caption))

if __name__ == "__main__":
    post_1 = Post('fit1045_group.jpg')
    Post('fit1053_group.jpg')
    for instance in Post.instances:
        print(instance)