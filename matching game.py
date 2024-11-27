import pygame
import sys
screen = pygame.display.set_mode((1520,780))
pygame.display.set_caption("matching")

candy = pygame.image.load("matching game/images/candy.jpg")
ludo = pygame.image.load("matching game/images/ludo.png")
subwaysurfers = pygame.image.load("matching game/images/ssurfers.png")
temple = pygame.image.load("matching game/images/temple.png")

candy_rect = pygame.Rect(50,10,90,90)
ludo_rect = pygame.Rect(50,210,90,90)
subwaysurfers_rect = pygame.Rect(50,410,90,90)
temple_run_rect = pygame.Rect(50,610,90,90)

candy_rect_t = pygame.Rect(1150,10,270,60)
ludo_rect_t = pygame.Rect(1150,210,200,60)
subwaysurfers_rect_t = pygame.Rect(1150,410,150,60)
temple_run_rect_t = pygame.Rect(1150,610,220,60)


pygame.font.init()
font = pygame.font.SysFont("Arial",50)
text1 = font.render("subwaysurfers",True, "white")
text2 = font.render("templerun",True, "white")
text3 = font.render("ludo",True, "white")
text4 = font.render("candycrush",True, "white")



def draw():
     screen.blit(candy,(50,10))
     screen.blit(ludo,(50,210))
     screen.blit(subwaysurfers,(50,410))
     screen.blit(temple,(50,610))
     screen.blit(text1,(1150,10))
     screen.blit(text2,(1150,210))
     screen.blit(text3,(1150,410))
     screen.blit(text4,(1150,610))

rectangles =  {"candy_crush":{"name":candy_rect,"click":False},"ludo":{"name":ludo_rect,"click":False},"subwaysurfers":{"name":subwaysurfers_rect,"click":False},"templerun":{"name":temple_run_rect,"click":False}}
text =  {"candy_crush":{"name":candy_rect_t,"click":False},"ludo":{"name":ludo_rect_t,"click":False},"subwaysurfers":{"name":subwaysurfers_rect_t,"click":False},"templerun":{"name":temple_run_rect_t,"click":False}}

draw()
image_select = None

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
               if not image_select:
                 for rec in rectangles:
                   print(rec)
                   if rectangles[rec]["name"].collidepoint(pygame.mouse.get_pos()) and rectangles[rec]["click"] == False:
                       start = pygame.mouse.get_pos()
                       pygame.draw.circle(screen,"blue",start,5)
                       rectangles[rec]["click"] = True
                       image_select = rec
               elif image_select:
                   for tex in text:
                       if text[tex]["name"].collidepoint(pygame.mouse.get_pos()) and text[tex]["click"] == False:
                         end = pygame.mouse.get_pos()
                         pygame.draw.circle(screen,"blue",end,5)
                         text[tex]["click"] = True
                         pygame.draw.line(screen,"blue",start,end,3)
                         image_select = None
          '''if event.type == pygame.MOUSEBUTTONUP:
               end = pygame.mouse.get_pos()
               pygame.draw.circle(screen,"blue",end,5)
               pygame.draw.line(screen,"blue",start,end,3)'''

     pygame.display.update()