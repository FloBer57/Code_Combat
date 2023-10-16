def cleaveOrAttack(enemy):
    # Si "cleave"  (fendre) est prêt, fends!; sinon, attaque.
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    pass

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 5:
            cleaveOrAttack(enemy)
