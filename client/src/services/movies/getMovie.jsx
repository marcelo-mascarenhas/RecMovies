import api from '../api';

export async function getMovieInfo(movie_info) {
  
    try {
      const response = await api.get(`/movie/${movie_info}`);
      return response.data;
    } catch (err) {
      throw new Error(err.response.data);
    }
}

export async function getMovieRecommender(movie_id) {
  
    try {
      const response = await api.get(`/movie/${movie_id}/recommender`);
      return response.data;
    } catch (err) {
      throw new Error(err.response.data);
    }
}