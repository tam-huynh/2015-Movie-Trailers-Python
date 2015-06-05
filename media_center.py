import fresh_tomatoes
import movie

#Creating movies
exMachina = movie.Movie('Ex Machina',
                        'A young programmer is selected to participate in' +
                        ' a breakthrough experiment in artificial intelligence by' +
                        ' evaluating the human qualities' +
                        ' of a breathtaking female A.I.',
                        'http://ia.media-imdb.com/images/M/' +
                        'MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE' +
                        '@._V1_SX214_AL_.jpg',
                        'https://www.youtube.com/watch?v=gyKqHOgMi4g')

theHatefulEight = movie.Movie('The Hateful Eight',
                              'In post-Civil War Wyoming, bounty hunters' +
                              'try to find shelter during a blizzard but get involved' +
                              'in a plot of betrayal and deception. Will they survive?',
                              'http://ia.media-imdb.com/images/M/' +
                              'MV5BMTY4MTMxNTMxM15BMl5BanBnXkFtZTgwODcyNjMzMjE' +
                              '@._V1._CR4,4,554,751_SY317_CR10,0,214,317_AL_.jpg',
                              'https://www.youtube.com/watch?v=WSk7_I-WHV8')

missionImpossibleRogueNation = movie.Movie('Mission: Impossible - Rogue Nation',
                                           'Ethan and team take on their most impossible mission yet,' +
                                           ' eradicating the Syndicate - an International' +
                                           ' rogue organization as highly skilled as they are,' +
                                           ' committed to destroying the IMF.',
                                           'http://ia.media-imdb.com/images/M/' +
                                           'MV5BMTQ1NDI2MzU2MF5BMl5BanBnXkFtZTgwNTExNTU5NDE' +
                                           '@._V1_SX214_AL_.jpg',
                                           'https://www.youtube.com/watch?v=gOW_azQbOjw')                                           

jurassicWorld = movie.Movie('Jurassic World',
                            'Twenty-two years after the events of Jurassic Park (1993),' +
                            ' Isla Nublar now features a fully functioning dinosaur theme park,' +
                            ' Jurassic World, as originally envisioned by John Hammond.' +
                            ' After 10 years of operation and visitor rates declining,' +
                            ' in order to fulfill a corporate mandate,' +
                            ' a new attraction is created to re-spark visitor''s interest,' +
                            ' which backfires horribly.',
                            'http://ia.media-imdb.com/images/M/' +
                            'MV5BMTQ5MTE0MTk3Nl5BMl5BanBnXkFtZTgwMjczMzk2NTE' +
                            '@._V1_SX214_AL_.jpg',
                            'https://www.youtube.com/watch?v=RFinNxS5KN4')

madMax = movie.Movie('Mad Max: Fury Road',
                     'In a stark desert landscape where humanity is broken,' +
                     ' two rebels just might be able to restore order:' +
                     ' Max, a man of action and of few words, and Furiosa,' +
                     ' a woman of action who is looking to make it back' +
                     ' to her childhood homeland.',
                     'http://ia.media-imdb.com/images/M/' +
                     'MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE' +
                     '@._V1_SY209_CR2,0,140,209_AL_.jpg',
                     'https://www.youtube.com/watch?v=hEJnMQG9ev8')

avengersUltron = movie.Movie('Avengers: Age of Ultron',
                             'When Tony Stark and Bruce Banner try to jump-start' +
                             ' a dormant peacekeeping program called Ultron,' +
                             ' things go horribly wrong and it''s up to Earth''s' +
                             ' Mightiest Heroes to stop the villainous Ultron' +
                             ' from enacting his terrible plans.',
                             'http://ia.media-imdb.com/images/M/' +
                             'MV5BMTU4MDU3NDQ5Ml5BMl5BanBnXkFtZTgwOTU5MDUxNTE' +
                             '@._V1_SY209_CR1,0,140,209_AL_.jpg',
                             'https://www.youtube.com/watch?v=JAUoeqvedMo')

furious7 = movie.Movie('Furious Seven',
                       'Deckard Shaw seeks revenge against Dominic Toretto' +
                       ' and his family for his comatose brother.',
                       'http://ia.media-imdb.com/images/M/' +
                       'MV5BMTQxOTA2NDUzOV5BMl5BanBnXkFtZTgwNzY2MTMxMzE' +
                       '@._V1_SX214_AL_.jpg',
                       'https://www.youtube.com/watch?v=yISKeT6sDOg')

spectre = movie.Movie('Spectre',
                      'A cryptic message from Bond''s past' +
                      ' sends him on a trail to uncover a sinister organization.' +
                      ' While M battles political forces to keep' +
                      ' the secret service alive, Bond peels back the layers' +
                      ' of deceit to reveal the terrible truth behind SPECTRE.',
                      'http://ia.media-imdb.com/images/M/' +
                      'MV5BMjIwNTA1MDA2Ml5BMl5BanBnXkFtZTgwNzIzMTA5NDE' +
                      '@._V1_SY317_CR0,0,214,317_AL_.jpg',
                      'https://www.youtube.com/watch?v=ashLaclKCik')

#Adding movies to a list
movies = [exMachina, missionImpossibleRogueNation, jurassicWorld,
          madMax, avengersUltron, theHatefulEight, furious7, spectre]

#Start the program
fresh_tomatoes.open_movies_page(movies)
          
