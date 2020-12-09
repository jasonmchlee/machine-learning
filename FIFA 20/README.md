# Exploring FIFA 20 to Predict Player’s Potential
[Full Report](https://github.com/jasonmchlee/machine-learning/blob/master/FIFA%2020/FIFA%2020%20-%20A%20Guide%20to%20Ultimate%20Team.pdf)

----------------------

## Background
FIFA 2020 is one of the world's most popular video games. It is a football simulation video game
published by Electronic Arts (EA Sports) as part of the FIFA series. It is the 27th installment in
the FIFA series and was released on 27 September 2019 for Microsoft Windows, PlayStation 4,
Xbox One, and Nintendo Switch.

Historically the FIFA series has been one of the main revenue generators for Electronic Arts
(EA). According to sportbible, across all sports franchise titles, including FIFA and Madden, EA
generated a total of $1.49 billion through the Ultimate Team platform --- which is a $120 million
increase on last year's revenue total of $1.37 billion. The Ultimate team platform is a gameplay
experience that allows gamers to build their team and compete against others. The goal is to
create your dream squad with superstars from past and present. For fiscal 2020, EA's revenue
topped $5.5 billion, with $2.7 billion of that generated from players spending money on
in-game content or live services. Gamers looking to take advantage of in-game purchases by
finding hidden gems, players with high potential, or already established superstars to build their
team.

----------------------

## Goal
This document explores in-game players from the FIFA 20 database to understand how
different characteristics, traits, demographics, and more influence players' overall rating and
potential. Throughout this analysis, we will uncover insights to drive a machine learning model.

The objective of the ML model will be to predict the potential of a player in the game.
Uncovering a player's potential is vital for the gameplay experience because it gives gamers
insights on which players have the most upsell or player development opportunities. This
strategy will give EA sports the resources to price individual players higher/lower based on their
potential score, thus converting in-app purchases.

----------------------

## Report Summary
- 568 out of 18,278 players in the FIFA 20 database recorded ≥ 80 overall ratings. An 80
rating is generally seen as a sign that the player plays for a top team or is a better player
for their respective team.
- In situations where a player could be ranked higher based on their overall rating than
their overall valuation, we can find that 5,625 (31%) players have a lower valuation
ranking than their overall rating.
  - For example, Lionel Messi is ranked number #1 for the overall rating, but he is
ranked number #2 for valuation.
- Younger players generally have leaner body physiques compared to the older group.
Specifically, players under 25 years old are the only group with more lean players than
Normal or Stocky body types.
- The most common team position in FIFA 20 is a substitute (representing 58% of all
players), which means that most players are not starters for their respective clubs.
  - However, looking at the player's preferred position, which is their main position,
the most common is the ST (striker) position recording 2.1K players
(approximately 11.5% of the player database).
- Amongst the top teams, most have a spread out overall rating between their 25th and
75th quartiles of player ratings. However, 3 top teams such as Bayern Munich, Juventus,
and Real Madrid have their interquartile range of ratings much narrower, around 75 to
87 ratings.
- A player's Potential and Release Clause has a medium/high correlation coefficient at
0.60 and enables us to identify young players with the most potential for in-game play.
- There is a clear pattern where a player's shirt number and position have a strong
relationship. The GK wears #1, defenders between #2 - #6, then midfielders and strikers
#7 - #11.
- For ≥ 80 overall ratings, 80% of the top 10 countries represented are in Europe, except
Brazil and Argentina (South America region), with Spain the most represented country.

----------------------

## Model Summary
- Building a model to predict a player's potential, we can see that developing features
around a player's position, traits, and characteristics proved significant in overall
performance.
  - Regression Training Score: 0.8538
  - Regression Testing Score: 0.8487
- Some examples of the coefficients impacts on the model are below:
  - For every 1 increase in the trait 'tactician', expect a 1.3 increase in potential.
  - For every 1 increase in a players' age' expect a -2.4 decrease in potential.
- 50% of the model's prediction fell within -1 to 1 from the actual potential value.
