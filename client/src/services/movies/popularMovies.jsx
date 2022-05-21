import api from '../api';

export async function popularMovies() {
  
    try {
      const number = 500;
      const response = await api.get(`/popular_movies/${number}`);
      return response.data.data;
    } catch (err) {
      throw new Error(err.response.data);
    }
  }