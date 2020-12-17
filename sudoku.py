import pygame

WIDTH = 550
background_color = (251,247,245)


grid =[ 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 7, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ] 

def insert(win, position):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN: 
                print(event.key)
                if(0 < event.key - 48 < 10):
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0)) 
                    print(position[0]*50,position[1]*50)
                    win.blit(value, (position[0]*50 + 15 ,position[1]*50 ) )  
                    pygame.display.update()
                return



def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH)) 
    clock = pygame.time.Clock()
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    for i in range(0,10):
        #Draw horizontal and vertical lines
        if(i % 3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
            continue            
        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
        
    #Prepouplate the grid
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0 < grid[i][j] < 10 ):
                value = myfont.render(str(grid[i][j]), True, (0, 0, 0)) 
                win.blit(value, ((i+1)*50 + 15 ,(j+1)*50 ))  
            

    pygame.display.update()
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                #print(pos[0]//50, pos[1]//50)
                #block position = (row no - 1)*9 + column no
                block_pos = (pos[1]//50 -1)*9 + pos[0]//50
                print(block_pos)
                insert(win, (pos[0]//50, pos[1]//50))
                
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
main()
