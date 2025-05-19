'''
Evan's workspace.

May 20: Shooting Mechanism (upon pressing key, bow releases arrow at constant velocity at wheel)

May 23: Incorporate with rest of project

May 26: Lives or chances (game can restart and show previous high scores) - - incorporated

May 29: Modulate speed of wheel spinning - - incorporated
    -increase/decrease speed of nob
    - ties in with the difficulty settings) 

    -> Also consider obstacles for shooters (birds, clouds, etc...)

June 2: Final done, with as many nice to haves as possible incorporated

Shooting Mechanism 
    bow
        stationary at bottom of screen
            - create pygame art for this
            -position it
    arrow
        arrowhead placed at tip of bow
            - create pygame art for arrow
            - position it
        upon click/press key, one arrow fires at wheel w constant v
            - velocity vector
        as soon as arrow hits wheel, next arrow loaded in same spot
        stop kinematics for arrow once hits the wheel
        stick the arrow to the wheel by reorienting it in polar coordinates/rotation around a fixed center
'''
