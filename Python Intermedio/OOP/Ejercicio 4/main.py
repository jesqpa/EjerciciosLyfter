class Head:
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "Head"


class Hand:    
    def __init__(self, side: str):
        self.side = side

class Arm:
    def __init__(self, hand: Hand):
        self.hand = hand

class Foot:
    def __init__(self, side: str):
        self.side = side

class Leg:
    def __init__(self, foot: Foot):
        self.foot = foot

class Torso:
    def __init__(self, head: Head, right_arm: Arm, left_arm: Arm, right_leg: Leg, left_leg: Leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg    


class Human:
    def __init__(self, torso: Torso):
        self.torso = torso

    def __str__(self) -> str:
        return (
            "==================== Human Anatomy ====================\n"
            f"Head:       {self.torso.head}\n"
            f"Right Arm:  Contains a {self.torso.right_arm.hand.side} hand\n"
            f"Left Arm:   Contains a {self.torso.left_arm.hand.side} hand\n"
            f"Right Leg:  Contains a {self.torso.right_leg.foot.side} foot\n"
            f"Left Leg:   Contains a {self.torso.left_leg.foot.side} foot\n"
            "======================================================="
        )


def main():
    head = Head()

    right_hand = Hand("right")
    right_arm = Arm(right_hand)

    left_hand = Hand("left")
    left_arm = Arm(left_hand)
    
    right_foot = Foot("right")
    right_leg = Leg(right_foot)

    left_foot = Foot("left")
    left_leg = Leg(left_foot)

    torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

    human = Human(torso)
    
    # Mostrar la representación visual de la anatomía del ser humano
    print(human)


if __name__ == "__main__":
    main()