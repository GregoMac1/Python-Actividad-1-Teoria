first = 'Hstory of Rock - Spotify'

second = 'International football results 1872 - 2020'

function_one = lambda song: song[2] == 'Foo Fighters' and 2000 <= int(song[3]) < 2010

function_two = lambda match: (match[1] == 'Argentina' or match[2] == 'Argentina') and match[5] == 'FIFA World Cup' and (match[0].startswith('1978') or match[0].startswith('1986'))
