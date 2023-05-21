import {setMovieFavorite} from '../movie';

describe('setMovieFavorite', () => {
  let favorites;

  beforeEach(() => {
    favorites = {};
  });

  it('should add a movie to favorites if it is not already favorited', () => {
    const movieId = 123;
    const movie = { id: movieId, title: 'The Avengers' };

    favorites = setMovieFavorite(favorites, movie);

    expect(favorites[movieId]).toEqual(movie);
  });

  it('should remove a movie from favorites if it is already favorited', () => {
    const movieId = 123;
    const movie = { id: movieId, title: 'The Avengers' };
    favorites[movieId] = movie;

    favorites = setMovieFavorite(favorites, movie);

    expect(favorites[movieId]).toBeUndefined();
  });

  it('should add a different movie to favorites if it is not already favorited', () => {
    const movieId1 = 123;
    const movie1 = { id: movieId1, title: 'The Avengers' };
    const movieId2 = 456;
    const movie2 = { id: movieId2, title: 'The Shawshank Redemption' };

    favorites = setMovieFavorite(favorites, movie1);
    favorites = setMovieFavorite(favorites, movie2);

    expect(favorites[movieId2]).toEqual(movie2);
  });

  it('should remove a movie from favorites without affecting other favorited movies', () => {
    const movieId1 = 123;
    const movie1 = { id: movieId1, title: 'The Avengers' };
    const movieId2 = 456;
    const movie2 = { id: movieId2, title: 'The Shawshank Redemption' };
    favorites[movieId1] = movie1;
    favorites[movieId2] = movie2;

    favorites = setMovieFavorite(favorites, movie1);

    expect(favorites[movieId1]).toBeUndefined();
    expect(favorites[movieId2]).toEqual(movie2);
  });

  it('should return the favorites object', () => {
    const movieId = 123;
    const movie = { id: movieId, title: 'The Avengers' };
    const result = setMovieFavorite(favorites, movieId, movie);

    expect(result).toBe(favorites);
  });

  it('should not modify favorites if the movie is not provided', () => {
    const movieId = 123;
    const movie = { id: movieId, title: 'The Avengers' };
    favorites[movieId] = movie;

    favorites = setMovieFavorite(favorites);

    expect(favorites[movieId]).toEqual(movie);
  });

  it('should not modify favorites if the movie ID is null', () => {
    const movieId = 123;
    const movie = { id: movieId, title: 'The Avengers' };
    favorites[movieId] = movie;

    favorites = setMovieFavorite(favorites, null);

    expect(favorites[movieId]).toEqual(movie);
  });

  it('should not modify favorites if the movie ID is undefined', () => {
    const movieId = 123;
    const movie = { id: movieId, title: 'The Avengers' };
    favorites[movieId] = movie;

    setMovieFavorite(favorites, undefined);

    expect(favorites[movieId]).toEqual(movie);
  });
});