import api from '../api';

export async function popularMovies() {
  
    try {
      const number = 100;
      const response = await api.get(`/popular_movies/${number}`);
      return response.data;
    } catch (err) {
      throw new Error(err.response.data);
    }
  }