from code.entity import Entity
from code.enemy import Enemy
from code.player import AnimatedEntity, PlayerMagic, Player
from code.Const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerMagic):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if isinstance(ent1, AnimatedEntity) and isinstance(ent2, Enemy):
            if EntityMediator.__rects_collide(ent1.rect, ent2.rect):
                ent2.health -= ent1.damage
                ent1.collided = True  # a magia para de andar
        elif isinstance(ent2, AnimatedEntity) and isinstance(ent1, Enemy):
            if EntityMediator.__rects_collide(ent1.rect, ent2.rect):
                ent1.health -= ent2.damage
                ent2.collided = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            if EntityMediator.__rects_collide(ent1.rect, ent2.rect):
                ent1.health -= ent2.damage

        elif isinstance(ent2, Player) and isinstance(ent1, Enemy):
            if EntityMediator.__rects_collide(ent1.rect, ent2.rect):
                ent2.health -= ent1.damage

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]) -> int:
        killed = 0
        for ent in entity_list:
            if hasattr(ent, 'health') and ent.health <= 0 and not getattr(ent, 'finished', False):
                ent.finished = True
                if 'Enemy' in ent.name or getattr(ent, 'is_enemy', False):
                    killed += 1
        return killed

    @staticmethod
    def __rects_collide(r1, r2):
        return (
            r1.right >= r2.left and
            r1.left <= r2.right and
            r1.bottom >= r2.top and
            r1.top <= r2.bottom
        )