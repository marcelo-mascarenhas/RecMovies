import api from '../api';

export async function getMovieData(movie_id) {
  
    try {
      const response = await api.get(`/data/a1/${movie_id}`);
      return response.data;
    } catch (err) {
      throw new Error(err.response.data);
    }
  }