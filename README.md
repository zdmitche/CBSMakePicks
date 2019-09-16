# CBSMakePicks
A script to make your picks in CBS's NFL pool manager.

Inspiration for this came after I found myself forgetting to make my picks, especially for the Thursday game. Even in a long season, forgetting a couple of your picks can cost you victory.

This script will not override any picks that you have already made. It's purpose is to run at the beginning of each week so that if you forget to make your picks, at least you have something.

This script is currently set to choose the home team for each matchup as well as 44 points for the MNF tiebreaker. 44 points is the average over-under for NFL games.

This is best used as an automated task to run once a week (probably on Tuesday or Wednesday). For those unaware on how to schedule automated tasks, an article like [this](https://datatofish.com/python-script-windows-scheduler/) might be useful if you're on Windows. Every OS has its own way to do this.

# Requirements
## settings.json
A file named `settings.json` is required to be in the scripts directory. Currently all these fields are required.
```
{
   "email": "user@test.com",
   "password": "password",
   "picksUrl": "http://test.football.cbssports.com/office-pool/make-picks"
}
```
**Note:** the picksUrl is your url to the make-picks page for your pool.

## geckodriver
geckodriver is required to be installed. See this [repo](https://github.com/mozilla/geckodriver/releases) if it needs to be installed on your system.
