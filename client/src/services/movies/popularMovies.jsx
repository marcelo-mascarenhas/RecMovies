import api from '../api';

export async function popularMovies() {
  
    try {
      const number = 10000;
      const response = await api.get(`/popular_movies/${number}`);
      return response.data;
    } catch (err) {
      throw new Error(err.response.data);
    }
  }