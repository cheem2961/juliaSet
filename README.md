# juliaSet
first time using guthib so this is kind of a test.


An attempt at the Julia Set using Python + Pygame


google definition of a Julia Set : a set of complex numbers which do not converge to any limit when a given mapping is repeatedly applied to them

a friend did the maths and I programmed it 

what each thing does:
  res: changes the resolution of the program
  c:  changing the complex value
  yMove and xMove: moves around the screen
  zoom: doesent really work but was to zoom in and out the fractal, alternatively, res also zooms in and out the fractal
  
 controls:
  keys[pygame.K_RIGHT]:
		res += 1
  keys[pygame.K_LEFT]:
		res -= 1
	keys[pygame.K_UP]:
		c += 0.001
	if keys[pygame.K_DOWN]:
		c -= 0.001
	keys[pygame.K_w]:
		yMove -= 0.01
	keys[pygame.K_s]:
		yMove += 0.01
	keys[pygame.K_a]:
		xMove -= 0.01
	keys[pygame.K_d]:
		xMove += 0.01
	keys[pygame.K_SPACE]:
		zoom += 0.01
	keys[pygame.K_LCTRL]:
		zoom += 0.01
