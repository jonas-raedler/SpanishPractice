import pygame

pygame.init()

HEIGHT, WIDTH = 720, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 56)


class Queue:

    def __init__(self, list):
        self.items = list

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            to_be_returned = self.items[0]
            self.items = self.items[1:]
            return to_be_returned
        else:
            return -1

    def is_not_empty(self):
        if len(self.items) >= 1:
            return 1
        else:
            return 0

    def print(self):
        return self.items


class Flashcard:

    def __init__(self):
        self.rect = pygame.Rect((WIDTH // 2 - 350, HEIGHT // 2 - 200), (700, 400))

        self.list_of_questions = Queue([("2 + 2", "4"), ("3 * 3", "9"), ("5 - 2", "3")])
        self.question_idx = 0

        self.display_question = True
        if self.list_of_questions.is_not_empty():
            self.current_question, self.current_answer = self.list_of_questions.dequeue()
        else:
            self.end_of_deck()


    def end_of_deck(self):
        self.current_question = "All Done!"
        self.current_answer = "Seriously. It's over, you're done."


    def turn_over(self):
        self.display_question = not self.display_question


    def change_question(self):
        self.display_question = True

        if self.list_of_questions.is_not_empty():
            self.current_question, self.current_answer = self.list_of_questions.dequeue()
        else:
            self.end_of_deck()


    def put_back(self):
        self.list_of_questions.enqueue((self.current_question, self.current_answer))


    def render(self):
        # Draw Flashcard
        pygame.draw.rect(screen, "#FFFFFF", self.rect)

        # Draw Word on Flashcard
        word_to_display = self.current_question if self.display_question else self.current_answer
        word = font.render(word_to_display, True, "#000000")
        word_width, word_height = word.get_size()
        screen.blit(word, (WIDTH // 2 - word_width // 2, HEIGHT // 2 - word_height // 2))


flashcard = Flashcard()

while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit

            if event.key == pygame.K_SPACE:
                flashcard.turn_over()

            if event.key == pygame.K_r:
                flashcard.put_back()
                flashcard.change_question()

            if event.key == pygame.K_RETURN:
                flashcard.change_question()





    #######################################################################################################
    # --------------------------------------- Screen Things --------------------------------------------- #
    #######################################################################################################
    screen.fill("purple")  # Fill the display with a solid color


    # Add Flashcard
    flashcard.render()

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)