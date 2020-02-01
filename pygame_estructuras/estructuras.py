import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font_name = pygame.font.match_font("arial")


def draw_text(surf, text, size, color, x, y):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(
        text, True, color
    )  ## True denotes the font to be anti-aliased
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Lista:
    def __init__(self, x, y):
        self.nodo = None
        self.x = x
        self.y = y

    def agregar(self, valor):
        if self.nodo:
            self.nodo.agregar(valor)
        else:
            self.nodo = NodoLista(valor, self.x, self.y)

    def pop(self):
        if self.nodo:
            return self.nodo.pop()

    def draw(self, screen):
        if self.nodo:
            self.nodo.draw(screen)


class NodoLista:
    def __init__(self, valor, x, y):
        self.next = None
        self.valor = valor
        self.x = int(x)
        self.y = int(y)

    def agregar(self, valor):
        if self.next:
            self.next.agregar(valor)
        else:
            self.next = NodoLista(valor, self.x + 100, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 25, 2)
        if self.next:
            pygame.draw.line(
                screen, WHITE, (self.x + 25, self.y), (self.next.x - 25, self.next.y), 3
            )
        draw_text(screen, f"{self.valor}", 20, WHITE, self.x, self.y - 15)

        if self.next:
            self.next.draw(screen)

    def pop(self):
        if self.next:
            if self.next.next:
                self.next.pop()
            else:
                valor = self.next.valor
                self.next = None
                return valor


class Pila:
    pass


class NodoPila:
    pass


class BTree:
    pass


class NodoBTree:
    pass


"""
Lista:
 - nodo 0

nodo 0
 - valor
 - nodo

 nodo 1
  - valor
  - nodo

  nodo 2
  - valor
  - nodo None

"""
