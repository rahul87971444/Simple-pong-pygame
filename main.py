import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pong")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 10
PADDLE_SPEED = 5
BALL_SPEED_X, BALL_SPEED_Y = 4, 4

# Define paddle positions
left_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Define ball position and velocity
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_velocity = [BALL_SPEED_X, BALL_SPEED_Y]

# Main loop
def main():
   clock = pygame.time.Clock()
   running = True
   left_paddle_velocity = 0
   right_paddle_velocity = 0

   while running:
       # Handle events
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_w:
                   left_paddle_velocity = -PADDLE_SPEED
               elif event.key == pygame.K_s:
                   left_paddle_velocity = PADDLE_SPEED
               elif event.key == pygame.K_UP:
                   right_paddle_velocity = -PADDLE_SPEED
               elif event.key == pygame.K_DOWN:
                   right_paddle_velocity = PADDLE_SPEED
           elif event.type == pygame.KEYUP:
               if event.key in (pygame.K_w, pygame.K_s):
                   left_paddle_velocity = 0
               elif event.key in (pygame.K_UP, pygame.K_DOWN):
                   right_paddle_velocity = 0

       # Update paddle positions
       left_paddle.y += left_paddle_velocity
       right_paddle.y += right_paddle_velocity

       # Keep paddles within the screen
       left_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, left_paddle.y))
       right_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, right_paddle.y))

       # Update ball position
       ball.x += ball_velocity[0]
       ball.y += ball_velocity[1]

       # Ball collision with top and bottom edges
       if ball.top <= 0 or ball.bottom >= HEIGHT:
           ball_velocity[1] = -ball_velocity[1]

       # Ball collision with paddles
       if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
           ball_velocity[0] = -ball_velocity[0]

       # Ball goes off the screen (reset to center)
       if ball.left <= 0 or ball.right >= WIDTH:
           ball.x = WIDTH // 2 - BALL_RADIUS
           ball.y = HEIGHT // 2 - BALL_RADIUS
           ball_velocity[0] = BALL_SPEED_X if ball.left <= 0 else -BALL_SPEED_X

       # Drawing
       screen.fill(BLACK)  # Clear the screen with black
       pygame.draw.rect(screen, WHITE, left_paddle)  # Draw left paddle
       pygame.draw.rect(screen, WHITE, right_paddle)  # Draw right paddle
       pygame.draw.ellipse(screen, WHITE, ball)  # Draw the ball
       pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))  # Draw center line

       # Update display
       pygame.display.flip()

       # Cap the frame rate
       clock.tick(60)

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()
 
