print("Once upon a time...")
class TreeNode():
    def __init__(self, story_pieces):
        self.story_piece = story_pieces
        self.choises = []

    def add_child(self, node):
        self.choises.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while story_node.choises != []:
            choise = input("Enter 1 or 2 to continue your jouney: ")
            if choise not in ["1", "2"]:
                print("Wrong input")
            if choise == "1" or "2":
                chosen_index = int(choise)
                chosen_index -= 1
                chosen_child = story_node.choises[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child



user_choise = input("""What's your name ?
""")
print(user_choise)





story_root = TreeNode("""You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")
choise_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")
choise_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")
choise_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choise_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")
choise_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")
choise_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")



story_root.add_child(choise_a)
story_root.add_child(choise_b)
choise_a.add_child(choise_a_1)
choise_a.add_child(choise_a_2)
choise_b.add_child(choise_b_1)
choise_b.add_child(choise_b_2)
story_root.traverse()
