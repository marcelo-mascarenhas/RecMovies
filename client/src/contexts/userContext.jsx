import { createContext, useContext, useState, useEffect } from 'react';

export const UserContext = createContext({});

export function UserContextProvider({ children }) {

  const [moviesFavorites, setMoviesFavorites] = useState(JSON.parse(localStorage.getItem('movieRec-movies')) || [])

  function isFavorite(id) {
    const index = moviesFavorites.indexOf(id)
    const existsInLocalStorage = index != -1
    return existsInLocalStorage
  }

  useEffect(() => {
  }, [moviesFavorites])

  function setMovieFavorite(movie){

    var aux = moviesFavorites
    const index = aux.indexOf(movie)
    const existsInLocalStorage = index != -1
    
    existsInLocalStorage ?
    aux.splice(index, 1)
    :
    aux.push(movie)
    
    console.log(index)
    
    setMoviesFavorites(aux)
    console.log(moviesFavorites)
    localStorage.setItem('movieRec-movies', JSON.stringify(aux))
  }


  return (
    <UserContext.Provider value={{ 
      moviesFavorites,
      isFavorite,
      setMovieFavorite,
    }}>
      {children}
    </UserContext.Provider>
  )
}

export const useUserContext = () => {
  return useContext(UserContext);
}