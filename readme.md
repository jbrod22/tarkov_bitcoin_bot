## Installing 

install python. either through Chocolatey or whatever

`pip install pyautogui`

## Configure

change the x, y coords in config.json to match
1. Windows button on bottom left of screen
2. Play button on the Tarkov Launcher
3. Hideout button on main menu
4. Generator in the hideout
5. Get All
6. Main Menu on bottom left
7. Exit button
8. Confirm Exit

sleep times are a simply way of adding delays for when the game is loading.
example: for my game the hideout button is available approx 65 seconds after I hit the play button on the launcher. so i set the `application_wait` timer to 65 seconds. your game may vary so do your due diligence and use a stop watch. it wont hurt to add 5, 10 or even 15 seconds to the delay at any point 

can add to windows task scheduler to _truly_ automate it
