import api from '../api';

export async function popularMovies() {
  
    try {
    //   const response = await api.get(`/data/a1/${movie_id}`);
      const response = await api.get(`/data/a1`);
      return response.data;
    } catch (err) {
      throw new Error(err.response.data);
    }
  }