import pygame


class Coordinates:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.get_xy = []
        self.pos_xy = []

    def run(self):
        run = True
        while run:
            pygame.time.delay(100)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False

            self.pos_xy = pygame.mouse.get_pos()
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.get_xy.append(self.pos_xy)
                print(self.pos_xy)

            with open('coords.txt', 'w') as wf:
                for itm_pos in self.get_xy:
                    for itm in itm_pos:
                        wf.write(
                            'X_Coord: {} Y_Coord: {}\n'.format(itm_pos[0], itm_pos[1]))
                        pygame.draw.circle(
                            self.screen, (255, 255, 0), (itm_pos[0], itm_pos[1]), 8, 0)
                        pygame.display.update()

        self.screen.fill((0, 0, 0))
        pygame.display.update()


pygame.quit()

get_coord = Coordinates()
get_coord.run()
