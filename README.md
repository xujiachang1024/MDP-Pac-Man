# Design and Implementation of Pac-Man Strategies with Embedded Markov Decision Process in a Dynamic, Non-Deterministic, Fully Observable Environment

### Abstract
This project designs and implements Pac-Man strategies, whose decision-making protocol is solely based on Markov Decision Process, without the support of pathfinding algorithms nor heuristic functions, in a dynamic, non-deterministic, fully observable environment. This project provides the rare opportunity to refine the understanding of, and practice the application of Markov Decision Process in a classic arcade game setting. After significant number of hours of parameter tuning, my design achieved a win rate ranging between 50\% and 60\%. With the proven effectiveness of embedded Markov Decision Process, a spin-off Pac-Man AI project that incorporates the advantages of pathfinding algorithms, heuristic functions, and Markov Decision Process shall be on the agenda.

### Design Document
<a href="https://github.com/xujiachang1024/MDP-Pac-Man/blob/master/design/mdpAgent_design.pdf">*Design of Pac-Man Strategies with Embedded Markov Decision Process in a Dynamic, Non-Deterministic, Fully Observable Environment*</a>

### Style of Work
* Coding style complies with industry standard
* Design paper complies with IEEE Conference format

### How to run
This version of Intelligent Pac-Man is running on <b>Python 2.7</b> environment. The visibility of the agent in this Pac-Man project is extremely limited, just like someone is running through the maze for real.<br/>
Run the following command to play the game:<br/>
```
python pacman.py --pacman MDPAgent --layout mediumClassic --numGames 50
```
