import api from '../api';

export async function popularMovies() {
  
    try {
    //   const response = await api.get(`/data/a1/${movie_id}`);]
      const number = 100;
      const response = await api.get(`/api/popular_movies/${number}`);
      return response.data;
    } catch (err) {
      throw new Error(err.response.data);
    }
  }