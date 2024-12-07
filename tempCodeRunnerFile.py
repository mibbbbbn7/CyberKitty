for enemy in pygame.sprite.Group.sprites(my_enemies_non_hittable):
        if (pygame.sprite.spritecollide(enemy, my_dash_clouds, False)):
            enemy.kill()