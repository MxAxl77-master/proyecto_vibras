vibra_genero(estudio, lofi).
vibra_genero(estudiar, lofi).
vibra_genero(chill, ambient).
vibra_genero(relajado, chillout).
vibra_genero(concentracion, classical).
vibra_genero(lectura, jazz).
vibra_genero(cafe, 'bossa-nova').

vibra_genero(ejercicio, trap).
vibra_genero(gym, phonk).
vibra_genero(correr, synthwave).
vibra_genero(motivacion, rock).
vibra_genero(energia, electronic).
vibra_genero(limpiar, pop).

vibra_genero(fiesta, reggaeton).
vibra_genero(baile, dance).
vibra_genero(reunion, house).
vibra_genero(antro, techno).
vibra_genero(carretera, 'indie-rock').

vibra_genero(triste, acoustic).
vibra_genero(melancolia, slowcore).
vibra_genero(feliz, upbeat).
vibra_genero(enojado, metal).
vibra_genero(nostalgia, '80s').
vibra_genero(romance, bachata).
vibra_genero(amor, soul).

vibra_genero(gaming, 'glitch-hop').
vibra_genero(videojuegos, chiptune).
vibra_genero(cyberpunk, industrial).
vibra_genero(espacio, 'space-ambient').

obtener_genero(Vibra, Genero) :-
    vibra_genero(Vibra, Genero).