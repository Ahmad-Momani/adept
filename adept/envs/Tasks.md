# Tasks implemented in the Adept Suite

Overview of the tasks in the Adept Suite
<img width="1240" alt="TasksALL" src="https://user-images.githubusercontent.com/23240128/134825260-0de32d74-e096-4ea5-906d-26302fade35f.png">


## List of the environmnets and Non-Stationarity options

|                    | **Environment**                | **Difficulty**  | **Sarcopenia**       | **Fatigue** | **Tendon-transfer** |
|--------------------|----------------------------|------------|------------------|---------|-----------------|
| Finger Joint Pose  | _FingerPoseMuscleFixed-v0_   | Easy       | √                | √       |                 |
| Finger Joint Pose  | _FingerPoseMuscleRandom-v0_  | Hard       | √                | √       |                 |
| Finger Tip Reach   | _FingerReachMuscleFixed-v0_  | Easy       | √                | √       |                 |
| Finger Tip Reach   | _FingerReachMuscleRandom-v0_ | Hard       | √                | √       |                 |
| Elbow Joint Pose   | _ElbowPose1D1MRandom-v0_     | Hard       | √                | √       |                 |
| Elbow Joint Pose   | _ElbowPose1D6MRandom-v0_     | Hard       | √                | √       |                 |
| Hand Joints Pose   | _HandPoseMuscleFixed-v0_     | Easy       | √                | √       | √               |
| Hand Joints Pose   | _HandPoseMuscleRandom-v0_    | Hard       | √                | √       | √               |
| Hand Tips Reach    | _HandReachMuscleFixed-v0_    | Easy       | √                | √       | √               |
| Hand Tips Reach    | _HandReachMuscleRandom-v0_   | Hard       | √                | √       | √               |
| Hand Key Turn      | _HandKeyTurnFixed-v0_        | Easy       | √                | √       | √               |
| Hand Key Turn      | _HandKeyTurnRandom-v0_       | Hard       | √                | √       | √               |
| Hand Object Hold   | _HandObjHoldFixed-v0_        | Easy       | √                | √       | √               |
| Hand Object Hold   | _HandObjHoldRandom-v0_       | Hard       | √                | √       | √               |
| Hand Pen Twirl     | _HandPenTwirlFixed-v0_       | Easy       | √                | √       | √               |
| Hand Pen Twirl     | _HandPenTwirlRandom-v0_      | Hard       | √                | √       | √               |
| Hand Baoding Balls | _BaodingFixed-v1_            | Easy       | √                | √       | √               |
| Hand Baoding Balls | _BaodingRandom-v1_           | Hard       | √                | √       | √               |



### Finger Joint Pose
_TODO_
In the easy version (_FingerPoseMuscleFixed-v0_) of the finger tip reach, the finger tip needs to reach a given position 
in the space while in the hard condition (_FingerPoseMuscleRandom-v0_) a random position.

### Finger Tip Reach   
_TODO_
In the easy version (_HandReachMuscleFixed-v0_) of the finger joint pose task finger needs to reach a given configuration 
of the joints while in the hard condition (_HandReachMuscleRandom-v0_) a random configuration of the joints.


### Elbow Joint Pose   
An elbow model with 6 muscles (3 flexors and 3 extensors) was simplified to have only elbow rotations. 
Although it is not a highly physiologically accurate model it can be a very simple model for troubleshooting initial control schemes. 
There are 2 versions of this task: reaching a random posture either with one muscle (_ElbowPose1D1MRandom-v0_) or 
with 6 muscles (_ElbowPose1D6MRandom-v0_)



### Hand Joints Pose 
TODO

### Hand Tips Reach    
TODO

### Hand Key Turn  
In the key turn task a simplified model of the Adept-hand with only thumb and index muscles was used. 
This model consisted of 20 muscles (all the forearm and hand muscle with the exclusion of the muscle to control middle, ring and little fingers). 
The goal of the task is to coordinate finger movements to rotate a key.
There are two versions of this task of different difficulty: easy, to reach a fixed rotation of the key (_HandKeyTurnFixed-v0_), 
and difficult, to reach a random position (_HandKeyTurnRandom-v0_)

### Hand Object Hold 
TODO

### Hand Pen Twirl   
A full forearm-wrist-hand rotate a pen in the hand to a given orientation without making if falling off. 
The complexity of this task is due to the intermittent contacts between the object and multiple fingers while trying to stabilize the object. 
The goal of this task is to rotate the object to reach a given orientation (indicated by the green object in the scene) without dropping it. 
There are two versions of this task of different difficulty: easy, target in a fixed orientation of the target (_HandPenTwirlFixed-v0_), and difficult, 
target in a random orientation (_HandPenTwirlRandom-v0_).
 
### Hand Baoding Balls 
A baoding ball task involving simultaneous rotation of two free-floating spheres over the palm. This task requires both dexterity and coordination. 
The goal of this task is to achieve relative rotation of the balls around each other without dropping them. 
There are two versions of this task of different difficulty: easy, (_BaodingFixed-v1_) - and difficult - (_BaodingRandom-v1_).



